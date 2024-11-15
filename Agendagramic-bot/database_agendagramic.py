import mysql.connector
from datetime import datetime
import uuid
from database_connection import connection

cursor = connection.cursor()

def insert_task(username, task_name, due_datetime, priority, status, group_id):
    
    task_id = str(uuid.uuid4())
    info_task = "Sem info"
    responsaveis = ""

    # debug
    print(f"Task ID: {task_id}")
    print(f"Task Name: {task_name}")
    print(f"Info Task: {info_task}")
    print(f"Due Date: {due_datetime}")
    print(f"Status: {status}")
    print(f"Priority: {priority}")
    print(f"Group ID: {group_id}")
    print(f"Username: {username}")
    group_id = "525ff911-c56b-41da-aee4-bbd33784b19a"


    cursor.execute('''INSERT INTO Tarefas (task_id, titulo, info_task,data, esta_completa, prioridade, group_id, responsaveis, criado_por, criado_em)
                      VALUES (UUID(),%s, %s, %s, %s, %s, %s, %s, %s, NOW())''', 
                   (task_name, info_task,due_datetime, status, priority, group_id, responsaveis, username))
    
    connection.commit() 
    connection.close()  
    connection.close()  



def save_task(task,username,group,priority,status):
    try:
        parts = task.split(", ",1)
        if len(parts) != 2:
            raise ValueError("Formato inválido. Por favor use: Nome da Tarefa, DD/MM/AAAA, HH:MM")

        task_name = parts[0] 
        datetime_str = parts[1]  
        due_datetime = datetime.strptime(datetime_str, "%d/%m/%Y, %H:%M")

        
        group_id = "Nenhum"
        if isinstance(group, tuple) and group:
            group_id = group[0] 
        
        insert_task(username, task_name, due_datetime, priority, status, group_id)

    except ValueError as e:
        print(str(e))  
        raise  g


def get_user_groups(user_id):

    cursor.execute("SELECT nome FROM Grupos WHERE admin = %s", (user_id,))
    groups = cursor.fetchall()  
    connection.close()
    return [group[0] for group in groups] 

def query_group_id(user_id,group):

    cursor.execute('SELECT group_id FROM Grupos WHERE admin = %s AND nome = %s',(user_id,group))
    group_id = cursor.fetchall()  
    connection.close()
    return group_id