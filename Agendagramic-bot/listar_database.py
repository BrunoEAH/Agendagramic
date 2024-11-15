import mysql.connector
from datetime import datetime
import mariadb
import uuid
from database_connection import connection


cursor = connection.cursor()


def listar_db(user_id):
    cursor.execute("SELECT titulo,comeco,fim FROM Eventos WHERE criado_por = ? ORDER BY comeco ASC", (user_id,))
    events = cursor.fetchall()

    cursor.execute("SELECT titulo, data FROM Tarefas WHERE criado_por = ? ORDER BY data ASC", (user_id,))
    tasks = cursor.fetchall()

    connection.close()

    combined_data = [
        {
            "tipo": "Evento", 
            "Titulo": event[0], 
            "comeco": event[1], 
            "fim": event[2]
        } for event in events
    ] + [
        {
            "tipo": "Tarefa", 
            "Titulo": task[0], 
            "comeco": task[1],
            "fim": None
        } for task in tasks
    ]

    combined_data.sort(key=lambda x: x["comeco"])
    message = f"Lista de eventos e tarefas do usuário {user_id}:\n"

    for item in combined_data:
        if item["tipo"] == "Evento":
            message += (f"{item['tipo']}: {item['Titulo']} - "
                        f"{item['comeco'].strftime('%Y-%m-%d %H:%M')} to "
                        f"{item['fim'].strftime('%Y-%m-%d %H:%M') if item['fim'] else 'N/A'}\n")
        else:
            message += f"{item['tipo']}: {item['Titulo']} - {item['comeco'].date()}\n"
        
    return message