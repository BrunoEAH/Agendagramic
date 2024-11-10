import mysql.connector
from datetime import datetime
import mariadb
import uuid

connection = mariadb.connect(
    user="teste",
    password="teste",
    host="localhost",
    port=3306,
    database="teste"
)

cursor = connection.cursor()

def verficiar_grupo(poll_data):
    query = "SELECT group_id FROM Grupos WHERE nome = %s AND admin = %s"
    cursor.execute(query, (poll_data["grupo"], poll_data["username"]))
    result = cursor.fetchone()

    if result: 
        group_id = result[0]
    else:
        return None
    
    connection.close()


def armazenar_task(group_id_poll,username_poll,group_poll,titulo_prioridade_poll,data_poll):
    
    parts = input_string.split(" - ")

    if len(parts) == 2:
        titulo = parts[0].strip()
        prioridade = parts[1].strip()
    else:
        print("String does not match expected format 'TITLE - PRIORITY'")
    
    info_taks = ""
    status = 0 #Nao esta completa por padrao

    responsaveis = ""

    cursor.execute('''INSERT INTO Tarefas (task_id, titulo,info_task, data, esta_completa, prioridade, group_id, responsaveis, criado_por, criado_em)
                      VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s, NOW())''', 
                   (titulo, info_task, data_poll, status, prioridade,group_id_poll, responsaveis, username_poll))
    print("Sucesso")

    connection.close()