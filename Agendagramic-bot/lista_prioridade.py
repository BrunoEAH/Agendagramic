import mysql.connector
from datetime import datetime
import mariadb
import uuid
from enum import IntEnum
from database_connection import connection

cursor = connection.cursor()

class Prioridade(IntEnum):
    Alta = 0
    Media = 1
    Baixa = 2



def listar_prioridade_db(user_id):
    cursor.execute("SELECT titulo, data, prioridade FROM Tarefas WHERE criado_por = ?", (user_id,))
    tasks = cursor.fetchall()


    tasks_data = [
        {
            "Titulo": task[0], 
            "comeco": task[1],
            "fim": None,
            "prioridade" : task[2]
        } for task in tasks
    ]

    tasks_ordenadas = sorted(tasks_data, key=lambda task: Prioridade[task["prioridade"]])
    message = f"Lista de tarefas por prioridade do usuário {user_id}:\n"

    for item in tasks_ordenadas:
         message += f"{item['prioridade']}: {item['Titulo']} - {item['comeco'].date()}\n"

        
    return message