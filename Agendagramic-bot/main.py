import subprocess
import time
import threading

def nuxt_aplicacao():
    print("Iniciando o servidor...")
    web_server_process = subprocess.Popen(["npm","run","dev","--","-o"], cwd="/Agendagramic-Nuxt/")
    time.sleep(5)  # Tempo de sleep
    return web_server_process

def bot_telegram():
    print("Rodando o bot...")
    bot_process = subprocess.Popen(["python3", "bot.py"], cwd="/Agendramic-bot/bot.py")
    time.sleep(2)  # Tempo de sleep
    return bot_process

def main():
    try:
        
        nuxt_process = nuxt_aplicacao()

        
        bot_process = bot_telegram()


    finally:
        # Para tudo
        nuxt_process.terminate()
        bot_process.terminate()
        print("Fim da automacao.")

if __name__ == "__main__":
    
    main()

"""     json_tasks = 'tasks.json'
    api_task = 'http://localhost:3000/api/tasks'

    json_events = 'events.json'
    api_events = 'http://localhost:3000/api/events'

    #Threads para observar os dois arquivos JSON.

    thread_task = threading.Thread(target=start_monitoring, args=(json_tasks, api_task))
    thread_events = threading.Thread(target=start_monitoring, args=(json_events, api_events))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
 """