import os
import re
from dateutil import parser
from dataclasses import dataclass,asdict
import json 

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


combined_data = [] #Lista para combinar arquivos JSON.


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

    salvar_json(task,'tasks.json')

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

    salvar_json(event,'events.json')

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
    
    with open(filename, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)


def carrega_json(caminho):
        with open(caminho,'r') as c:
            return json.load(c)


def combinacao(events_file, tasks_files):
    data_task = load_json(tasks_files)
    data_event = load_json(events_file)

    for item in data_task:
        combined_data.append({
            "data": item["Data"],
            "horario": item["Horario"],
            "info": item["info"]
        })

    for item in data_event:
        comeco_fim_str = f"{item['comeco']} - {item['fim']} "
        combined_data.append({
            "data": item["event"],
            "horario": comeco_fim_str,
            "info": item["info"]
        })

    

def create_task(data:str,horario:str,info:str) -> Task:
    return Task(data=data,horario=horario,info=info)

def create_event(data:str,comeco:str,fim:str,info:str) -> Event:
    return Event(data=data,comeco=comeco,fim=fim,info=info)