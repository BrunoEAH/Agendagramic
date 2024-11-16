import mysql.connector
from datetime import datetime
import mariadb
import uuid
from database_connection import connection

def verificar_grupo(group_name, username):
    query = "SELECT group_id FROM Grupos WHERE nome = %s AND admin = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (group_name, username))
        result = cursor.fetchone() 

    return result[0] if result else None



def armazenar_task(group_id_poll,username_poll,group_poll,titulo_prioridade_poll,data_poll):
    
    parts = [part.strip() for part in titulo_prioridade_poll.split(" - ")]

    titulo = parts[0] if len(parts) > 0 else ""
    prioridade = parts[1] if len(parts) > 1 else ""

    info_task = ""
    status = 0 #Nao esta completa por padrao

    responsaveis = ""

    due_datetime = datetime.strptime(data_poll, "%d/%m/%Y - %H:%M")

    due_datetime_formatted = due_datetime.strftime('%Y-%m-%d %H:%M:%S')


    with connection.cursor() as cursor:
        cursor.execute('''INSERT INTO Tarefas (task_id, titulo,info_task, data, esta_completa, prioridade, group_id, responsaveis, criado_por, criado_em)
                        VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s,%s, NOW())''', 
                    (titulo, info_task, due_datetime_formatted, status, prioridade,group_id_poll, responsaveis, username_poll))
        print("Sucesso")

def armazenar_evento(group_id_poll,username_poll,group_poll,titulo,data_poll):
    
    parts = data_poll.split(", ",3)
    if len(parts) != 4:
        raise ValueError("Formato inválido. Por favor use: DD/MM/AAAA, HH:MM, DD/MM/AAAA, HH:MM")

    comeco_datastr = parts[0] + ", " + parts[1]
    fim_datastr = parts[2] + ", " + parts[3]

    comeco = datetime.strptime(comeco_datastr, "%d/%m/%Y, %H:%M")
    fim = datetime.strptime(fim_datastr, "%d/%m/%Y, %H:%M")
    info_evento = ""
    status = 0  #Nao esta completa por padrao

    responsaveis = ""


    with connection.cursor() as cursor:
        cursor.execute('''INSERT INTO Eventos (event_id, titulo,info_evento,comeco,fim,group_id,criado_por,esta_completa,criada_em)
                        VALUES (UUID(), %s, %s, %s, %s, %s, %s,%s, NOW())''', 
                    (titulo, info_evento,comeco,fim,group_id_poll,username_poll,status))
        print("Sucesso")
