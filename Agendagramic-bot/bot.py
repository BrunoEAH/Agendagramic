import os
import telebot 
from dotenv import load_dotenv
from processing_schedule import processar_task,processar_event
import json

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Token nao encontrado")

bot = telebot.TeleBot(BOT_TOKEN)

json_task_path = '../Agendagramic-Nuxt/static/tasks.json'
json_event_path = '../Agendagramic-Nuxt/static/events.json'
api_url = 'http://localhost:3000/api/'



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
    text = "Escreva a data (DD/MM/YYYY), o horário (HH:MM) e a tarefa que será realizada."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,resposta_task)


@bot.message_handler(commands=['event'])
def event_handler(message):
    text = "Escreva a data (DD/MM/YYYY), o horário (HH:MM - HH:MM) e o evento que será realizada."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,resposta_event)


def resposta_task(message):
    
    task = processar_task(message)

    bot.send_message(message.chat.id, "Tarefa agendada com sucesso!")
    bot.send_message(message.chat.id, f"Data: {task.data}", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"Horario: {task.horario}", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"Tarefa: {task.info}", parse_mode="Markdown")


def resposta_event(message):

    event = processar_event(message)
    bot.send_message(message.chat.id, "Evento agendado com sucesso!")
    bot.send_message(message.chat.id, f"Data: {event.data}", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"Começo: {event.comeco}", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"Fim: {event.fim}", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"Evento: {event.info}", parse_mode="Markdown")

@bot.message_handler(commands=['list'])
def listar_tudo(message):
    
    lista = ""
    with open(json_task_path) as tasks_file:
        data_task = json.load(tasks_file)

    with open(json_event_path) as events_file:
        data_event = json.load(events_file)

    if not data_task and not data_event:
        bot.send_message(message.chat.id, "Lista vazia.")
    else:
        lista = "Tarefas:\n\n"

        for count,item in enumerate(data_task, start=1):
            lista_text = f"Tarefa {count}: {item['info']}\n"
            lista_text += f"Data: {item['Data']}\n"
            lista_text += f"Horario: {item['Horario']}\n\n"
            lista += lista_text

        lista+= "\nEventos:\n\n "

        for count,item in enumerate(data_event  , start=1):
            lista_text = f"Evento {count}: {item['Info']}\n"
            lista_text += f"Data: {item['Data']}\n"
            lista_text += f"Horario: {item['Horario']}\n\n"
            lista += lista_text
   
        bot.send_message(message.chat.id, f"{lista}", parse_mode="Markdown")
    


# Mantém o bot em funcionamento
bot.infinity_polling()
