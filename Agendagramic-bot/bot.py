import os
import telebot 

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
        # Adicione outros comandos conforme necessário
    )
    bot.reply_to(message, menu_message)

# Mantém o bot em funcionamento
bot.infinity_polling()
