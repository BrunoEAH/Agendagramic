import json
import os
import requests
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

"""
POR ENQUANTO SEM UTILIDADE.

Esse programa serve para constantemente visualizar os arquivos JSON, assim quando há mudança, ele posta diretamente na
API.
"""


class JsonFileHandler(FileSystemEventHandler):
    """Handles file system events related to the JSON file."""
    
    def __init__(self, json_file_path, api_url):
        self.json_file_path = json_file_path
        self.api_url = api_url
    
    def on_modified(self, event):
        """Called when the watched file is modified."""
        if event.src_path == self.json_file_path:
            print(f"Mudanca detectada em {self.json_file_path}")
            self.post_data_from_json()
    
    def post_data_from_json(self):
        """Load data from the JSON file and post it to the API."""
        try:
            with open(self.json_file_path, 'r') as json_file:
                data = json.load(json_file)
            
            if isinstance(data, list):
                for entry in data:
                    self.post_data_to_api(entry)
            else:
                self.post_data_to_api(data)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Error processing file: {e}")

    def post_data_to_api(self, data):
        """Post the given data to the API."""
        try:
            response = requests.post(self.api_url, json=data)
            if response.status_code == 201:
                print(f"Data posted successfully: {data}")
            else:
                print(f"Failed to post data: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error posting data to the API: {e}")

def start_monitoring(json_file_path, api_url):
    """Start monitoring the JSON file for changes."""
    event_handler = JsonFileHandler(json_file_path, api_url)
    observer = Observer()
    observer.schedule(event_handler, path=json_file_path, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
