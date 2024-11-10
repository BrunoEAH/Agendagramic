import os
import telebot 
from dotenv import load_dotenv
from database_agendagramic import get_user_groups,query_group_id,save_task
from listar_database import listar_db
from lista_prioridade import listar_prioridade_db
from poll_database import verficiar_grupo,armazenar_task

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Token nao encontrado")

bot = telebot.TeleBot(BOT_TOKEN)

#Dicionario para armazenar detalhes da votacao
poll_data = {}
completed_polls = {}
 
#Variaveis globais
user_id = None
username = None
task = None
group = None
priority = None
status = None

agenda_type = None #Variavel para definir se é uma tarefa ou evento


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
        "/list - Listar eventos e tarefas em ordem\n"
        "/list_task_priority - Lista tarefas em ordem de prioridade\n"
        "/create_poll_task - Criar votação para tarefa\n"
        "/create_poll_event - Criar votação para evento\n"
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

@bot.message_handler(commands=['list_task_priority'])
def pergunta_username(message):
    msg = bot.send_message(message.chat.id, "Escreva o seu username com o @.")
    bot.register_next_step_handler(msg, listar_prioridade)

def listar_prioridade(message):
    username = message.text 
    if username.startswith("@"):
        list_message = listar_prioridade_db(username)
        bot.reply_to(message, list_message)
    else:
        bot.send_message(message.chat.id, "Eu preciso do seu usuário. Envie novamente.")


@bot.message_handler(commands=['create_poll_task'])
def ask_username(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    msg = bot.send_message(chat_id, "Escreva o seu usuario com o @.")
    bot.register_next_step_handler(msg, receive_username)

def receive_username(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.text
    
    if not username.startswith("@"):
        msg = bot.send_message(chat_id, "Por favor entre um usuario valido comecando com '@'.")
        bot.register_next_step_handler(msg, receive_username)
        return

    poll_data[user_id] = {"username": username, "group": "","group_id": "", "type": "Tarefa", "question": "", "options": []}
    msg = bot.send_message(chat_id, "Por favor, entre o nome do grupo.")
    bot.register_next_step_handler(msg, receive_group_name)

def receive_group_name(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    group_name = message.text
    
    poll_data[user_id]["group"] = group_name

    grupo_id = verficiar_grupo(poll_data)
    if not existe_grupo:
        bot.send_message(chat_id, "Você não é admin deste grupo.")
        return

    poll_data[user_id]["group_id"]

    msg = bot.send_message(chat_id, "Escreva o título da tarefa e a prioridade (TITULO - PRIORIDADE)  para ser decidido na votacao:")
    bot.register_next_step_handler(msg, receive_poll_question)


def receive_poll_question(message):

    chat_id = message.chat.id
    user_id = message.from_user.id

    poll_data[user_id]["question"] = message.text
    
    msg = bot.send_message(chat_id, "Escreva os horarios para a tarefa. Envie /done quando acabar de adicionar os horarios.")
    bot.register_next_step_handler(msg, recebe_opcoes)

def recebe_opcao(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if message.text.lower() == "/done":
        # Ve se duas opcoes foram adicionadas
        if len(poll_data[user_id]["options"]) < 2:
            msg = bot.send_message(chat_id, "Por favor escreva pelo menos duas opcoes.")
            bot.register_next_step_handler(msg, recebe_opcao)
        else:
            criar_poll(chat_id, user_id)
        return
    
    # Adicionando opcoes
    poll_data[user_id]["options"].append(message.text)
    msg = bot.send_message(chat_id, "Envie outra opcao ou envie /done para terminar.")
    bot.register_next_step_handler(msg, recebe_opcao)


def criar_poll(chat_id, user_id):
    question = poll_data[user_id]["question"]
    options = poll_data[user_id]["options"]

    # Envia a votacao para o chat
    votacao = bot.send_poll(chat_id, question=question, options=options, is_anonymous=False)

    completed_polls[sent_poll.id] = {
        "user_id": user_id, 
        "question": question,
        "group": poll_data[user_id]["group"],
        "group_id": poll_data[user_id]["group_id"],
        "username": poll_data[user_id]["username"],
        "options": options
    }

    del poll_data[user_id]

@bot.poll_handler(func=lambda poll: True)
def resultados_polls(poll: Poll):
    poll_id = poll.id
    question = poll.question
    options = poll.options

    # Opcao com mais votacao
    top_option = max(options, key=lambda opt: opt.voter_count)
    top_option_text = top_option.text
    top_votes = top_option.voter_count

    completed_polls[poll_id] = {
        "Tarefa": question,
        "Data": top_option_text,
        "Autor": poll_data[user_id]["username"],
        "Grupo": poll_data[user_id]["group"],
        "group_id": poll_data[user_id]["group_id"]
    }

    username_poll = completed_polls[poll_id]["Autor"]
    group_poll = completed_polls[poll_id]["Grupo"]
    titulo_prioridade_poll = completed_polls[poll_id]["Tarefa"]
    data_poll = completed_polls[poll_id]["Data"]
    group_id_poll = completed_polls[poll_id]["group_id"]

    armazenar_task(group_id_poll,username_poll,group_poll,titulo_prioridade_poll,data_poll)

    bot.send_message(poll.chat.id, f"Resultado da votacao: {question}\n"
                    f"Vencedor: {top_option_text} com {top_votes} votos.")
    
    del completed_polls[poll_id]


# Mantém o bot em funcionamento
bot.infinity_polling()