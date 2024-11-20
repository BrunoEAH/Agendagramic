"""
API para recuperar os Eventos, Tarefas e Grupos do banco de dados.

"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import mariadb
from conexao_db import connection

app = Flask(__name__)
CORS(app)


cursor = connection.cursor()


#Nome dos grupos
@app.route('/api/groups', methods=['GET'])
def get_groups():
    user_telegram = request.args.get('userTelegram')
    if not user_telegram:
        return jsonify({"success": False, "message": "userTelegram esta faltando"}), 400

    cursor.execute("SELECT nome AS group_name FROM Grupos WHERE admin = ?", (user_telegram,))
    groups = cursor.fetchall()

    return jsonify({"success": True, "groups": groups})


#Tarefas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    user_telegram = request.args.get('userTelegram')
    if not user_telegram:
        return jsonify({"success": False, "message": "userTelegram esta faltando"}), 400

    cursor.execute("SELECT task_id, titulo AS name, info_task AS description, data as date, esta_completa AS status, prioridade AS priority, group_id as id_group, responsaveis as t_members FROM Tarefas WHERE criado_por = ?", (user_telegram,))
    
    #Convertendo tuplas para dicionario
    columns = [column[0] for column in cursor.description]
    tasks = [dict(zip(columns, task)) for task in cursor.fetchall()]

    for task in tasks:
        group_id = task['id_group']
        if group_id:
            cursor.execute("SELECT nome FROM Grupos WHERE group_id = ?", (group_id,))
            group_name = cursor.fetchone()
            if group_name:
                task['group_name'] = group_name[0]

    return jsonify({"success": True, "tarefas": tasks})

#Eventos
@app.route('/api/events', methods=['GET'])
def get_events():
    user_telegram = request.args.get('userTelegram')
    
    if not user_telegram:
        return jsonify({"success": False, "message": "userTelegram esta faltando"}), 400

    cursor.execute("SELECT event_id, titulo AS name,info_evento AS description,comeco AS date_begin,fim AS date_end, group_id AS id_group,esta_completa as status FROM Eventos WHERE criado_por = ?", (user_telegram,))
    
    #Convertendo tuplas para dicionario
    columns = [column[0] for column in cursor.description]
    events = [dict(zip(columns, events)) for events in cursor.fetchall()]

    for event in events:
        group_id = event['id_group']
        if group_id:
            cursor.execute("SELECT nome FROM Grupos WHERE group_id = ?", (group_id,))
            group_name = cursor.fetchone()
            if group_name:
                event['group_name'] = group_name[0]

    return jsonify({"success": True, "eventos": events})


if __name__ == '__main__':
    app.run(debug=True)
