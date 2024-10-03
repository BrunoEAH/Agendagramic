import os
import telebot 
from processing_schedule import processar_task,processar_event
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

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


# Mantém o bot em funcionamento
bot.infinity_polling()
