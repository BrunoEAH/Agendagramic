import mysql.connector
from datetime import datetime
import uuid
from database_connection import connection

def insert_task(username,task,priority,status,group):
    
    info_task = "Sem info"
    responsaveis = ""

    parts = task.split(", ",1)
    if len(parts) != 2:
        raise ValueError("Formato inválido. Por favor use: Nome da Tarefa, DD/MM/AAAA, HH:MM")

    task_name = parts[0] 
    datetime_str = parts[1]  
    due_datetime = datetime.strptime(datetime_str, "%d/%m/%Y, %H:%M")

    group_id = query_group_id(username,group)

    
    print(f"Task Name: {task_name}")
    print(f"Info Task: {info_task}")
    print(f"Due Date: {due_datetime}")
    print(f"Status: {status}")
    print(f"Priority: {priority}")
    print(f"Group ID: {group}")
    print(f"Username: {username}")


    
    sql_insert = """
    INSERT INTO Tarefas (task_id, titulo, info_task, data, esta_completa, prioridade, group_id, responsaveis, criado_por, criado_em)
    VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s, %s, NOW())
    """
    values = (task_name, info_task,due_datetime, status, priority, group_id, responsaveis, username)
    
    with connection.cursor() as cursor:
        cursor.execute(sql_insert, values)
        connection.commit()


def get_user_groups(user_id):
    query = "SELECT nome FROM Grupos WHERE admin = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (user_id,))
        groups = cursor.fetchall()
    return [group[0] for group in groups] 

def query_group_id(user_id,group):
    query = "SELECT group_id FROM Grupos WHERE admin = %s AND nome = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (user_id, group))
        result = cursor.fetchone()
    return result[0] if result else None



def insert_event(username,event,group):

    info_event = "Sem info"
    responsaveis = ""
    esta_completa = 0

    parts = event.split(", ",4)
    if len(parts) != 5:
        raise ValueError("Formato inválido. Por favor use: DD/MM/AAAA, HH:MM, DD/MM/AAAA, HH:MM")

    comeco_datastr = parts[0] + ", " + parts[1]
    fim_datastr = parts[2] + ", " + parts[3]
    event_name = parts[4] 
      
    comeco_data = datetime.strptime(comeco_datastr, "%d/%m/%Y, %H:%M")
    fim_data = datetime.strptime(fim_datastr, "%d/%m/%Y, %H:%M")

    group_id = query_group_id(username,group)

    
    print(f"Event Name: {event_name}")
    print(f"Info Event: {info_event}")
    print(f"Due Date: {comeco_data}")
    print(f"End Date: {fim_data}")
    print(f"IsComplete: {esta_completa}")
    print(f"Group ID: {group}")
    print(f"Username: {username}")


    
    sql_insert = """
    INSERT INTO Eventos (event_id, titulo, info_evento, comeco,fim,group_id, criado_por,esta_completa, criada_em)
    VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s, NOW())
    """
    values = (event_name, info_event,comeco_data,fim_data,group_id,username,esta_completa)
    
    with connection.cursor() as cursor:
        cursor.execute(sql_insert, values)
        connection.commit()