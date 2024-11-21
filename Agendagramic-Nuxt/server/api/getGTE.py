"""
API para recuperar os Eventos, Tarefas e Grupos do banco de dados.

"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import mariadb
from conexao_db import connection
from datetime import datetime
app = Flask(__name__)
CORS(app)



#Nome dos grupos - ADMIN
@app.route('/api/groups', methods=['GET'])
def get_groups():
    try:
        cursor = connection.cursor()
        user_telegram = request.args.get('userTelegram')
        if not user_telegram:
            return jsonify({"success": False, "message": "userTelegram esta faltando"}), 400

        cursor.execute("SELECT nome AS group_name FROM Grupos WHERE admin = ?", (user_telegram,))
        groups = cursor.fetchall()

        return jsonify({"success": True, "groups": groups})

    finally:
        if 'connection' in locals():
            connection.close()


#Nome dos grupos - MEMBRO
@app.route('/api/groups_membro', methods=['GET'])
def get_groups_member():

    try:
        cursor = connection.cursor()
        user_telegram = request.args.get('userTelegram')
        if not user_telegram:
            return jsonify({"success": False, "message": "userTelegram está faltando"}), 400

        query = """
            SELECT g.nome
            FROM Grupos g
            JOIN Membros gm ON g.group_id = gm.group_id
            WHERE gm.user_telegram = %s AND g.admin != %s
        """
        cursor.execute(query, (user_telegram, user_telegram))
        groups = cursor.fetchall()
        return jsonify({"success": True, "groups": [{"name": group[0]} for group in groups]})
    finally:
        if 'connection' in locals():
            connection.close()

#Tarefas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():

    try:
        cursor = connection.cursor()
        user_telegram = request.args.get('userTelegram')
        if not user_telegram:
            return jsonify({"success": False, "message": "userTelegram esta faltando"}), 400

        cursor.execute("SELECT group_id FROM Grupos WHERE admin = ?", (user_telegram,))
        group = cursor.fetchone()


        if group and group[0] is not None:
            group_id = group[0]
        else:
            group_id = None

        tasks = []
        if group_id:
            cursor.execute("""
                SELECT task_id, titulo AS name, info_task AS description, data AS date, 
                    esta_completa AS status, prioridade AS priority, group_id AS id_group, 
                    responsaveis AS t_members 
                FROM Tarefas 
                WHERE group_id = ?
            """, (group_id,))
                
            #Convertendo tuplas para dicionario
            columns = [column[0] for column in cursor.description]
            group_tasks = [dict(zip(columns, task)) for task in cursor.fetchall()]

            for task in group_tasks:
                cursor.execute("SELECT nome FROM Grupos WHERE group_id = ?", (task['id_group'],))
                group_name = cursor.fetchone()
                if group_name:
                    task['group_name'] = group_name[0]

            tasks.extend(group_tasks)

        cursor.execute("""
            SELECT task_id, titulo AS name, info_task AS description, data AS date, 
                esta_completa AS status, prioridade AS priority, group_id AS id_group, 
                responsaveis AS t_members 
            FROM Tarefas 
            WHERE criado_por = ? AND group_id IS NULL
        """, (user_telegram,))
        columns = [column[0] for column in cursor.description]
        no_group_tasks = [dict(zip(columns, task)) for task in cursor.fetchall()]

        for task in no_group_tasks:
            task['group_name'] = None

        tasks.extend(no_group_tasks)

        return jsonify({"success": True, "tarefas": tasks})
    finally:
        if 'connection' in locals():
            connection.close()


#Eventos
@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        cursor = connection.cursor()
        user_telegram = request.args.get('userTelegram')
        
        if not user_telegram:
            return jsonify({"success": False, "message": "userTelegram esta faltando"}), 400

        cursor.execute("SELECT group_id FROM Grupos WHERE admin = ?", (user_telegram,))
        group = cursor.fetchone()

        if group and group[0] is not None:
            group_id = group[0]
        else:
            group_id = None

        events = []

        if group_id:
            cursor.execute("""
                SELECT event_id, titulo AS name, info_evento AS description, comeco AS date_begin, fim AS date_end,
                    group_id AS id_group, esta_completa AS status 
                FROM Eventos 
                WHERE group_id = ?
            """, (group_id,))
            #Convertendo tuplas para dicionario
            columns = [column[0] for column in cursor.description]
            group_events = [dict(zip(columns, event)) for event in cursor.fetchall()]

            for event in group_events:
                cursor.execute("SELECT nome FROM Grupos WHERE group_id = ?", (event['id_group'],))
                group_name = cursor.fetchone()
                if group_name:
                    task['group_name'] = group_name[0]

            events.extend(group_events)

        cursor.execute("""
                SELECT event_id, titulo AS name, info_evento AS description, comeco AS date_begin, fim AS date_end,
                    esta_completa AS status, group_id AS id_group
                FROM Eventos 
                WHERE criado_por = ? AND group_id IS NULL
        """, (user_telegram,))

        columns = [column[0] for column in cursor.description]
        no_group_events = [dict(zip(columns, event)) for event in cursor.fetchall()]

        for event in no_group_events:
            event['group_name'] = None

        events.extend(no_group_events)
        return jsonify({"success": True, "eventos": events})
    finally:
        if 'connection' in locals():
            connection.close()

#Retorna eventos e tarefas
@app.route('/api/eventsetask', methods=['GET'])
def get_events_tasks():
    try:
        cursor = connection.cursor()
        user_telegram = request.args.get('userTelegram')
        ano = request.args.get('year')
        mes = request.args.get('month')
        dia = request.args.get('day')



        if not user_telegram:
            return jsonify({"success": False, "message": "userTelegram esta faltando"}), 400

        if not (ano and mes and dia):
            return jsonify({"success": False, "message": "Year, month, or day is missing"}), 400


        try:
            selected_date = datetime(int(ano), int(mes), int(dia))

            #Organizando o formato da data e colocando intervalo de horario
            date_start = selected_date.strftime('%Y-%m-%d 00:00:00')
            date_end = selected_date.strftime('%Y-%m-%d 23:59:59')
        except ValueError:
            return jsonify({"success": False, "message": "Invalid date provided"}), 400

        # Query events
        cursor.execute(
            """
            SELECT 
                event_id, 
                titulo AS name,
                info_evento AS description,
                comeco AS date_begin,
                fim AS date_end,
                group_id AS id_group,
                esta_completa AS status 
            FROM 
                Eventos 
            WHERE 
                criado_por = ? AND 
                comeco BETWEEN ? AND ?
            """, 
            (user_telegram, date_start, date_end)
        )

        # Convertendo events para um dicionario
        columns = [column[0] for column in cursor.description]
        events = [dict(zip(columns, row)) for row in cursor.fetchall()]

        for event in events:
            group_id = event['id_group']
            if group_id:
                cursor.execute("SELECT nome FROM Grupos WHERE group_id = ?", (group_id,))
                group_name = cursor.fetchone()
                if group_name:
                    event['group_name'] = group_name[0]

        cursor.execute(
            """
            SELECT 
                task_id,
                titulo AS name,
                info_task AS description,
                data AS due_date,
                prioridade AS priority,
                esta_completa AS status,
                group_id AS id_group,
                responsaveis AS responsible
            FROM 
                Tarefas 
            WHERE 
                criado_por = ? AND 
                data BETWEEN ? AND ?
            """, 
            (user_telegram, date_start, date_end)
        )

        # Convertendo tarefas para um dicionario
        columns = [column[0] for column in cursor.description]
        tasks = [dict(zip(columns, row)) for row in cursor.fetchall()]

        for task in tasks:
            group_id = task['id_group']
            if group_id:
                cursor.execute("SELECT nome FROM Grupos WHERE group_id = ?", (group_id,))
                group_name = cursor.fetchone()
                if group_name:
                    task['group_name'] = group_name[0]

        return jsonify({"success": True, "events": events, "tasks": tasks})

    finally:
        if 'connection' in locals():
            connection.close()


if __name__ == '__main__':
    app.run(debug=True)
