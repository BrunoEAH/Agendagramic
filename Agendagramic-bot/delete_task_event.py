import mysql.connector
from datetime import datetime
import mariadb
from database_connection import connection

cursor = connection.cursor()


def query_event(username,event_name):
    query = """
    SELECT event_id 
    FROM Eventos 
    WHERE criado_por = %s AND titulo = %s
    """
    cursor.execute(query, (username, event_name))
    event = cursor.fetchone()

    return event

def deletedb_event(event_id):
    delete_query = "DELETE FROM Eventos WHERE event_id = %s"
    cursor.execute(delete_query, (event_id,))
    connection.commit()

def deletedb_task(task_id):
    delete_query = "DELETE FROM Tarefas WHERE task_id = %s"
    cursor.execute(delete_query, (task_id,))
    connection.commit()

def query_task(username,task_name):
    query = """
    SELECT task_id 
    FROM Tarefas 
    WHERE criado_por = %s AND titulo = %s
    """
    cursor.execute(query, (username,task_name))
    task = cursor.fetchone()

    return task