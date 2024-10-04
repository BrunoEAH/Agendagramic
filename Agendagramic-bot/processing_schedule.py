import os
import re
from dateutil import parser
from dataclasses import dataclass,asdict
import json 
from datetime import datetime

event_path = '../Agendagramic-Nuxt/static/events.json'
task_path = '../Agendagramic-Nuxt/static/tasks.json'
os.makedirs(os.path.dirname(event_path), exist_ok=True)
os.makedirs(os.path.dirname(task_path), exist_ok=True)

@dataclass
class Task:
    data: str
    horario: str
    info: str


@dataclass
class Event:
    data:str
    comeco:str
    fim:str
    info:str


def processar_task(message) -> Task:
    
    msg = message.text

    #DD/MM/YY HH:MM Info
    #Regex para o formato acima.
    date_pattern = r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b"
    time_pattern = r"\b(\d{1,2}:\d{2}(?:\s?[APMapm]{2})?)\b"
    date_match = re.search(date_pattern, msg)
    time_match = re.search(time_pattern, msg)

    date = None
    time = None
    if date_match:
        try:
            date = parser.parse(date_match.group(0), fuzzy=True).date()
        except Exception as e:
            print(f"Error parsing date: {e}")
    
    if time_match:
        try:
            time = parser.parse(time_match.group(0), fuzzy=True).time()
        except Exception as e:
            print(f"Error parsing time: {e}")
    
    text = re.sub(date_pattern, "", msg)
    text = re.sub(time_pattern, "", text).strip()

    task = create_task(date,time,text)

    salvar_json(task,task_path)

    return task


def processar_event(message) -> Event:
    
    msg = message.text

    # DD/MM/YY HH:MM-HH:MM Info 
    #Regex para o formato acima.
    pattern = r"(\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2})-(\d{2}:\d{2})\s+(.+)"
    
    match = re.search(pattern, msg)
    
    if not match:
        raise ValueError("String nao faz parte da regex.")
    
    date_str = match.group(1)
    start_time_str = match.group(2)
    end_time_str = match.group(3)
    text = match.group(4)
 
    event = create_event(date_str,start_time_str,end_time_str,text)

    salvar_json(event,event_path)

    return event

def salvar_json(instance, filename: str):

    if isinstance(instance, Task):
        data_dict = {
            "Data": str(instance.data),
            "Horario": str(instance.horario),  
            "info": instance.info
        }
    elif isinstance(instance, Event):
        data_dict = {
            "Data": str(instance.data),
            "Horario": f"{instance.comeco}-{instance.fim}",
            "Info": instance.info
        }
    else:
        raise TypeError(f"Unsupported instance type: {type(instance)}")
    
    try:
        with open(filename, 'r') as json_file:
            existing_data = json.load(json_file)
            if not isinstance(existing_data, list):
                existing_data = [] 
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []  

    existing_data.append(data_dict)

    with open(filename, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)


def create_task(data:str,horario:str,info:str) -> Task:
    return Task(data=data,horario=horario,info=info)

def create_event(data:str,comeco:str,fim:str,info:str) -> Event:
    return Event(data=data,comeco=comeco,fim=fim,info=info)