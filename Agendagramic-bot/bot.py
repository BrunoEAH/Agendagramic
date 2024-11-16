import os
import telebot 
from dotenv import load_dotenv
from database_agendagramic import get_user_groups,query_group_id,insert_task,insert_event
from listar_database import listar_db
from lista_prioridade import listar_prioridade_db
from poll_database import verificar_grupo,armazenar_task,armazenar_evento
from telebot.types import Poll

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Token nao encontrado")

bot = telebot.TeleBot(BOT_TOKEN)

#Dicionario para armazenar detalhes da votacao
poll_data = {}
completed_polls = {}
user_data = {}

tipo = ""  #Variavel global para checar se é um evento ou tarefa


def handle_poll_results(poll: Poll, poll_type: str):
    global tipo
    poll_id = poll.id
    question = poll.question
    options = poll.options

    top_option = max(options, key=lambda opt: opt.voter_count)
    top_option_text = top_option.text
    top_votes = top_option.voter_count

    tipo = "" # Global vazia

    username_poll = completed_polls[poll_id]["username"]
    group_poll = completed_polls[poll_id]["group_name"]
    group_id_poll = completed_polls[poll_id]["group_id"]
    chat_id = completed_polls[poll_id]["chat_id"]

    
    if poll_type == 'event':
        titulo_poll = completed_polls[poll_id]["question"]
    elif poll_type == 'task':
        titulo_poll = completed_polls[poll_id]["question"]
    
    total_eleitores = sum(opt.voter_count for opt in options)
    expected_voters = int(completed_polls[poll_id]["voters"])

    if total_eleitores >= expected_voters:
        if poll_type == 'event':
            armazenar_evento(group_id_poll, username_poll, group_poll, titulo_poll, top_option_text)
        elif poll_type == 'task':
            armazenar_task(group_id_poll, username_poll, group_poll, titulo_poll, top_option_text)

        bot.send_message(chat_id, f"Resultado da votacao: {question}\n"
                    f"Vencedor: {top_option_text} com {top_votes} votos.")
        del completed_polls[poll_id]
    else:
        bot.send_message(chat_id, f"Aguardando mais votos. {total_eleitores}/{expected_voters} votaram até agora.")


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
        "/list - Listar eventos e tarefas em ordem de data\n"
        "/list_task_priority - Lista tarefas em ordem de prioridade\n"
        "/create_poll_task - Criar votação para tarefa\n"
        "/create_poll_event - Criar votação para evento\n"
        # Adicione outros comandos conforme necessário
    )
    bot.reply_to(message, menu_message)






#################################
#                               #
#                               #
#   INSERIR TAREFAS             #
#                               #
#################################


@bot.message_handler(commands=['task'])
def task_handler(message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    text = "Escreva a tarefa da seguinte maneira: Nome da Tarefa, DD/MM/AAAA, HH:MM"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,ask_priority)

def ask_priority(message):
    user_id = message.from_user.id
    task = message.text.strip()
    user_data[user_id]['task'] = task

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Baixa', 'Media', 'Alta')
    sent_msg = bot.send_message(message.chat.id, "Selecione a prioridade da tarefa:", reply_markup=markup)
    bot.register_next_step_handler(sent_msg, ask_status)


def ask_status(message):
    user_id = message.from_user.id
    priority = message.text.strip()
    user_data[user_id]['priority'] = priority

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Pendente', 'Em progresso', 'Completa')
    sent_msg = bot.send_message(message.chat.id, "Selecione o status da tarefa:", reply_markup=markup)
    bot.register_next_step_handler(sent_msg, ask_username)

def ask_username(message):
    user_id = message.from_user.id
    status_map = {'Pendente': 0, 'Em progresso': 1, 'Completa': 2}
    status = status_map.get(message.text.strip(), 1)
    
    user_data[user_id]['status'] = status
    
    sent_msg = bot.send_message(message.chat.id, "Escreva o seu username com o @", parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, ask_group)

def ask_group(message):
    user_id = message.from_user.id
    username = message.text.strip()
    user_data[user_id]['username'] = username

    user_groups = get_user_groups(username)

    if not user_groups:
        bot.send_message(message.chat.id, "Você não faz parte de um grupo.")
        user_data[user_id]['group'] = "Nenhum"

        group = user_data[user_id]['group']
        task = user_data[user_id]['task']
        priority = user_data[user_id]['priority']
        status = user_data[user_id]['status']
        username = user_data[user_id]['username']

        insert_task(username,task,priority,status,group)
        bot.send_message(message.chat.id, "Tarefa salva com sucesso!")

        return

    group_buttons = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    
    for grp in user_groups:
        group_buttons.add(grp)

    group_buttons.add(f"Nenhum")

    sent_msg = bot.send_message(message.chat.id, "Selecione o grupo:", reply_markup=group_buttons)
    bot.register_next_step_handler(sent_msg, handle_group_selection)

def handle_group_selection(message):
    user_id = message.from_user.id
    group = message.text.strip()
    user_data[user_id]['group'] = group

    group = user_data[user_id]['group']
    task = user_data[user_id]['task']
    priority = user_data[user_id]['priority']
    status = user_data[user_id]['status']
    username = user_data[user_id]['username']

    insert_task(username,task,priority,status,group)

    bot.send_message(message.chat.id, "Tarefa salva com sucesso!")





#################################
#                               #
#                               #
#   INSERIR EVENTOS             #
#                               #
#################################


@bot.message_handler(commands=['event'])
def event_handler(message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    text = "Escreva a data inicial (DD/MM/YYYY), o horário de comeco (HH:MM), a data final, o horario final e o evento que será realizada."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg,ask_username_event)

def ask_username_event(message):
    user_id = message.from_user.id
    event = message.text.strip()
    user_data[user_id]['event'] = event

    sent_msg = bot.send_message(message.chat.id, "Escreva o seu username com o @", parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, ask_group_event)

def ask_group_event(message):
    user_id = message.from_user.id
    username = message.text.strip()
    user_data[user_id]['username'] = username

    user_groups = get_user_groups(username)

    if not user_groups:
        bot.send_message(message.chat.id, "Você não faz parte de um grupo.")
        user_data[user_id]['group'] = "Nenhum"

        group = user_data[user_id]['group']
        event = user_data[user_id]['event']
        username = user_data[user_id]['username']

        insert_event(username,event,group)
        bot.send_message(message.chat.id, "Evento salva com sucesso!")

        return

    group_buttons = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    
    for grp in user_groups:
        group_buttons.add(grp)

    group_buttons.add(f"Nenhum")

    sent_msg = bot.send_message(message.chat.id, "Selecione o grupo:", reply_markup=group_buttons)
    bot.register_next_step_handler(sent_msg, handle_group_event)

def handle_group_event(message):
    user_id = message.from_user.id
    group = message.text.strip()
    user_data[user_id]['group'] = group

    group = user_data[user_id]['group']
    event = user_data[user_id]['event']
    username = user_data[user_id]['username']

    insert_event(username,event,group)

    bot.send_message(message.chat.id, "Evento salvo com sucesso!")





#################################
#                               #
#                               #
#   LISTAR EVENTOS E TAREFAS    #
#                               #
#################################

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



######################################
#                                    #
#                                    #
#   LISTAR TAREFAS POR PRIORIDADE    #
#                                    #
######################################


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




#################################
#                               #
#                               #
#   CRIAR ENQUETE - TAREFAS     #
#                               #
#################################

@bot.message_handler(commands=['create_poll_task'])
def ask_username_poll_task(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    msg = bot.send_message(chat_id, "Escreva o seu usuario com o @.")
    bot.register_next_step_handler(msg, receive_username_task)

def receive_username_task(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.text
    
    if not username.startswith("@"):
        msg = bot.send_message(chat_id, "Por favor entre um usuario valido comecando com '@'.")
        bot.register_next_step_handler(msg, receive_username_task)
        return

    poll_data[user_id] = {"username": username, "group_name": "","group_id": "", "type": "Tarefa", "question": "", "options": []}
    msg = bot.send_message(chat_id, "Por favor, entre o nome do grupo.")
    bot.register_next_step_handler(msg, receive_group_name_task)

def receive_group_name_task(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    group_name = message.text
    
    poll_data[user_id]["group_name"] = group_name
    username = poll_data[user_id]["username"]
    group_name = poll_data[user_id]["group_name"]

    grupo_id = verificar_grupo(group_name,username)

    if not grupo_id:
        bot.send_message(chat_id, "Você não é admin deste grupo.")
        
        return

    poll_data[user_id]["group_id"] = grupo_id

    msg = bot.send_message(chat_id, "Escreva o número de pessoas que poderão votar. ")
    bot.register_next_step_handler(msg, receive_number_voters_task)

def receive_number_voters_task(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    poll_data[user_id]["voters"] = message.text

    msg = bot.send_message(chat_id, "Escreva o título da tarefa e a prioridade (TITULO - PRIORIDADE)  para ser decidido na votacao:")
    bot.register_next_step_handler(msg, receive_poll_question_task)

def receive_poll_question_task(message):

    chat_id = message.chat.id
    user_id = message.from_user.id

    poll_data[user_id]["question"] = message.text
    
    msg = bot.send_message(chat_id, "Escreva a data e o horario para a tarefa (DD/MM/AAAA - HH:MM). Envie /done quando acabar de adicionar os horarios.")
    bot.register_next_step_handler(msg, recebe_opcao_task)

def recebe_opcao_task(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if message.text.lower() == "/done":
        # Ve se duas opcoes foram adicionadas
        if len(poll_data[user_id]["options"]) < 2:
            msg = bot.send_message(chat_id, "Por favor escreva pelo menos duas opcoes.")
            bot.register_next_step_handler(msg, recebe_opcao_task)
        else:
            criar_poll_task(chat_id, user_id)
        return
    
    # Adicionando opcoes
    poll_data[user_id]["options"].append(message.text)
    msg = bot.send_message(chat_id, "Envie outra opcao ou envie /done para terminar.")
    bot.register_next_step_handler(msg, recebe_opcao_task)

def criar_poll_task(chat_id, user_id):
    global tipo
    question = poll_data[user_id]["question"]
    options = poll_data[user_id]["options"]

    # Envia a votacao para o chat
    votacao = bot.send_poll(chat_id, question=question, options=options, is_anonymous=False)

    completed_polls[votacao.poll.id] = {
        "user_id": user_id, 
        "question": question,
        "group_name": poll_data[user_id]["group_name"],
        "group_id": poll_data[user_id]["group_id"],
        "username": poll_data[user_id]["username"],
        "voters": poll_data[user_id]["voters"]
    }

    completed_polls[votacao.poll.id]["chat_id"] = chat_id

    tipo = "Task"

    del poll_data[user_id]

@bot.poll_handler(func=lambda poll: True)
def resultados_polls_task(poll: Poll):
    global tipo
    if tipo == "Task":
        handle_poll_results(poll, poll_type='task')
    else:
        handle_poll_results(poll, poll_type='event')

#################################
#                               #
#                               #
#   CRIAR ENQUETE - EVENTOS     #
#                               #
#################################

@bot.message_handler(commands=['create_poll_event'])
def ask_username_poll_event(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    msg = bot.send_message(chat_id, "Escreva o seu usuario com o @.")
    bot.register_next_step_handler(msg, receive_username_event)

def receive_username_event(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.text
    
    if not username.startswith("@"):
        msg = bot.send_message(chat_id, "Por favor entre um usuario valido comecando com '@'.")
        bot.register_next_step_handler(msg, receive_username_event)
        return

    poll_data[user_id] = {"username": username, "group_name": "","group_id": "", "type": "Tarefa", "question": "", "options": []}
    msg = bot.send_message(chat_id, "Por favor, entre o nome do grupo.")
    bot.register_next_step_handler(msg, receive_group_name_event)

def receive_group_name_event(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    group_name = message.text
    
    poll_data[user_id]["group_name"] = group_name
    username = poll_data[user_id]["username"]
    group_name = poll_data[user_id]["group_name"]

    grupo_id = verificar_grupo(group_name,username)

    if not grupo_id:
        bot.send_message(chat_id, "Você não é admin deste grupo.")
        
        return

    poll_data[user_id]["group_id"] = grupo_id

    msg = bot.send_message(chat_id, "Escreva o número de pessoas que poderão votar. ")
    bot.register_next_step_handler(msg, receive_number_voters_event)

def receive_number_voters_event(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    poll_data[user_id]["voters"] = message.text

    msg = bot.send_message(chat_id, "Escreva o título do evento para ser decidido na votacao:")
    bot.register_next_step_handler(msg, receive_poll_question_event)

def receive_poll_question_event(message):

    chat_id = message.chat.id
    user_id = message.from_user.id

    poll_data[user_id]["question"] = message.text
    
    msg = bot.send_message(chat_id, "Escreva a data e o horario de começo e a data e o horario de termino (DD/MM/AAAA, HH:MM, DD/MM/AAAA, HH:MM). Envie /done quando acabar de adicionar os horarios.")
    bot.register_next_step_handler(msg, recebe_opcao_event)

def recebe_opcao_event(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if message.text.lower() == "/done":
        # Ve se duas opcoes foram adicionadas
        if len(poll_data[user_id]["options"]) < 2:
            msg = bot.send_message(chat_id, "Por favor escreva pelo menos duas opcoes.")
            bot.register_next_step_handler(msg, recebe_opcao_event)
        else:
            criar_poll_event(chat_id, user_id)
        return
    
    # Adicionando opcoes
    poll_data[user_id]["options"].append(message.text)
    msg = bot.send_message(chat_id, "Envie outra opcao ou envie /done para terminar.")
    bot.register_next_step_handler(msg, recebe_opcao_event)

def criar_poll_event(chat_id, user_id):
    global tipo
    question = poll_data[user_id]["question"]
    options = poll_data[user_id]["options"]

    # Envia a votacao para o chat
    votacao = bot.send_poll(chat_id, question=question, options=options, is_anonymous=False)

    completed_polls[votacao.poll.id] = {
        "user_id": user_id, 
        "question": question,
        "group_name": poll_data[user_id]["group_name"],
        "group_id": poll_data[user_id]["group_id"],
        "username": poll_data[user_id]["username"],
        "options": options,
        "voters": poll_data[user_id]["voters"]
    }

    completed_polls[votacao.poll.id]["chat_id"] = chat_id

    tipo = "Evento"

    del poll_data[user_id]

""" def resultados_polls_event(poll: Poll):
    poll_id = poll.id
    question = poll.question
    options = poll.options

    # Opcao com mais votacao
    top_option = max(options, key=lambda opt: opt.voter_count)
    top_option_text = top_option.text
    top_votes = top_option.voter_count


    username_poll = completed_polls[poll_id]["username"]
    group_poll = completed_polls[poll_id]["group_name"]
    titulo_poll = completed_polls[poll_id]["question"]
    group_id_poll = completed_polls[poll_id]["group_id"]
    chat_id = completed_polls[poll_id]["chat_id"]


    total_eleitores = sum(opt.voter_count for opt in options)
    expected_voters = int(completed_polls[poll_id]["voters"])

    if total_eleitores >= expected_voters:
        armazenar_evento(group_id_poll,username_poll,group_poll,titulo_poll,top_option_text)

        bot.send_message(chat_id, f"Resultado da votacao: {question}\n"
                    f"Vencedor: {top_option_text} com {top_votes} votos.")
    
        del completed_polls[poll_id]

    else:
        bot.send_message(chat_id, f"Aguardando mais votos. {total_eleitores}/{expected_voters} votaram até agora.")
 """

# Mantém o bot em funcionamento
bot.infinity_polling()