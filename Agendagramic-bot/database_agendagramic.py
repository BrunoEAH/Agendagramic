import mysql.connector
from datetime import datetime
import uuid



def connect_to_database():
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='teste',
        password='teste',
        database='agendagramic',
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    return connection


def insert_task(username, task_name, due_datetime, priority, status, group_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    
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


    cursor.execute('''INSERT INTO Tarefas (task_id, titulo, info_task, esta_completa, prioridade, group_id, responsaveis, criado_por, criado_em)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())''', 
                   (task_id, task_name, info_task, status, priority, group_id, responsaveis, username))
    
    conn.commit() 
    cursor.close()  
    conn.close()  



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
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM Grupos WHERE admin = %s", (user_id,))
    groups = cursor.fetchall()  
    conn.close()
    return [group[0] for group in groups] 

def query_group_id(user_id,group):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT group_id FROM Grupos WHERE admin = %s AND nome = %s',(user_id,group))
    group_id = cursor.fetchall()  
    conn.close()
    return group_id[0]