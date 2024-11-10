import os
import telebot 
from dotenv import load_dotenv
from database_agendagramic import get_user_groups,query_group_id,save_task
from listar_database import listar_db

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Token nao encontrado")

bot = telebot.TeleBot(BOT_TOKEN)

user_id = None
username = None
task = None
group = None
priority = None
status = None


# Função para exibir a mensagem de boas-vindas
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    welcome_message = (
        "Olá! Seja bem-vindo ao AgendaGramic!\n\n"
        "Veja nossa lista de comandos digitando /menu"
    )
    bot.reply_to(message, welcome_message)

# Função para exibir o menu com a lista de comandos
@bot.message_handler(commands=['menu'])
def send_menu(message):
    menu_message = (
        "Aqui estão os comandos disponíveis:\n"
        "/start - Exibe a mensagem de boas-vindas\n"
        "/menu - Exibe este menu de comandos\n"
        "/event - Marcar um evento\n"
        "/task - Marcar uma tarefa\n"
        "/list - Listar eventos e tarefas em ordem"
        # Adicione outros comandos conforme necessário
    )
    bot.reply_to(message, menu_message)


@bot.message_handler(commands=['task'])
def task_handler(message):
    global task
    text = "Escreva a tarefa da seguinte maneira: Nome da Tarefa, DD/MM/AAAA, HH:MM"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,ask_priority)

def ask_priority(message):
    global priority,task 
    task = message.text.strip()

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Baixa', 'Media', 'Alta')
    bot.send_message(message.chat.id, "Selecione a prioridade da tarefa:", reply_markup=markup)
    bot.register_next_step_handler(message, ask_status)


def ask_status(message):
    global status,priority
    priority = message.text.strip()


    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Pendente', 'Em progresso', 'Completa')
    bot.send_message(message.chat.id, "Selecione o status da tarefa:", reply_markup=markup)
    bot.register_next_step_handler(message, ask_username)

def ask_username(message):
    global user_id,username,status
    
    status = message.text.strip()
    status_map = {'Pendente': 0, 'Em progresso': 1, 'Completa': 2}
    status = status_map.get(message.text,1) # Default em progresso
    
    print(status)
    user_id = message.from_user.id
    text = "Escreva o seu username com o @"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,ask_group)

def ask_group(message):
    global group,username  
    username = message.text.strip()
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)

    user_groups = get_user_groups(username)

    if not user_groups:
        bot.send_message(message.chat.id, "Você não faz parte de um grupo.")
        group = "Nenhum" 
        save_task(task,username,group,priority,status)
        return

    group_buttons = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
   
    for grp in user_groups:
        group_buttons.add(f"Grupo {grp}")

    group_buttons.add(f"Nenhum")

    bot.send_message(message.chat.id, "Selecione o grupo:", reply_markup=markup)
    bot.register_next_step_handler(message, handle_group_selection)

def handle_group_selection(message):
    global group
    group = message.text 

    if group == "Nenhum":
        bot.send_message(message.chat.id, "Você selecionou nenhum grupo.")
        
        group_id = None  
        save_task(task,username,group_id,priority,status) 
    else:
        group_id = query_group_id(message.from_user.id, group)
        save_task(task,username,group_id,priority,status) 


@bot.message_handler(commands=['event'])
def event_handler(message):
    text = "Escreva a data (DD/MM/YYYY), o horário (HH:MM - HH:MM) e o evento que será realizada."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,resposta_event)

@bot.message_handler(commands=['list'])
def pergunta_username(message):
    msg = bot.send_message(message.chat.id, "Escreva o seu username com o @.")
    bot.register_next_step_handler(msg, listar_tudo)

def listar_tudo(message):
    username = message.text 
    if username.startswith("@"):
        list_message = listar_db(username)
        bot.reply_to(message, list_message)
    else:
        bot.send_message(message.chat.id, "Eu preciso do seu usuário. Envie novamente.")

# Mantém o bot em funcionamento
bot.infinity_polling()
