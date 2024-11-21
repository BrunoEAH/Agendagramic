import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Fixture para inicializar o WebDriver antes de cada teste e fechar após o teste
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(r"--user-data-dir=C:\Users\vitor\AppData\Local\Google\Chrome\User Data")  # Caminho do perfil
    chrome_options.add_argument("--profile-directory=Default")  # Nome do perfil
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver  # Garante que o WebDriver será finalizado após o teste
    driver.quit()

# Função auxiliar para esperar elementos
def wait_for_element(driver, by, locator, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    )

# Teste para enviar comandos no chat do bot no Telegram
def test_login_submit(driver):
    print("Iniciando test_login_submit")

    # Navega para o chat do bot no Telegram
    driver.get("https://web.telegram.org/k/#@agendagramic_bot")

    # Aguarda o campo de entrada de texto e envia o comando "/start"
    start_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    start_input.send_keys("/start")

    # Aguarda o botão de envio e clica
    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

    # Espera alguns segundos para garantir que o comando "/start" foi processado
    time.sleep(3)

    # Aguarda o campo de entrada de texto novamente e envia o comando "/menu"
    menu_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    menu_input.send_keys("/menu")

    # Aguarda o botão de envio e clica
    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

    # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)

        # Aguarda o campo de entrada de texto novamente e envia o comando "/menu"
    task_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    task_input.send_keys("/task")

        # Aguarda o botão de envio e clica
    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

    # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)

    add_task_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    add_task_input.send_keys("Teste Apresentação, 21/11/2024, 19:20")

    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

    # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)

    task_priority_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    task_priority_input.send_keys("Alta")

    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

    # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)

    task_status_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    task_status_input.send_keys("Em progresso")

    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

        # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)


    username_task_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    username_task_input.send_keys("@FestaZumbi")

    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

        # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)

    task_group_input = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    task_group_input.send_keys("Grupo de teste")

    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

        # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)

    list_task_priority = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    list_task_priority.send_keys("/list_task_priority")

    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

        # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)

    username_task_priority = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    username_task_priority.send_keys("@FestaZumbi")

    send_button = wait_for_element(driver, By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div')
    send_button.click()

        # Espera para garantir que o comando "/menu" foi processado antes de fechar o navegador
    time.sleep(3)



    

    



