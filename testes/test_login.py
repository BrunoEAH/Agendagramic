import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Fixture para inicializar o WebDriver antes de cada teste e fechar após o teste
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

# Função auxiliar para esperar elementos
def wait_for_element(driver, by, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    )
def test_login_submit(driver):
    print("Iniciando test_login_submit")
    
    # Navega para a página inicial
    driver.get("http://localhost:3000")
    
    # Aguarda o botão de login na página inicial e clica
    login_button = wait_for_element(driver, By.XPATH, '//*[@id="__nuxt"]/div/div/div/main/div[3]/button[1]')
    login_button.click()
    print("Navegou para a página de login com sucesso!")
    
    # Aguarda o campo de login (email/username) estar visível
    email_input = wait_for_element(driver, By.XPATH, '//*[@id="email"]') 
    email_input.send_keys("teste@email.com") 
    
    # Aguarda o campo de senha estar visível
    password_input = wait_for_element(driver, By.XPATH, '//*[@id="password"]')  
    password_input.send_keys("senha")  
    
    # Aguarda o botão de submit estar clicável e clica
    submit_button = wait_for_element(driver, By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/form/button[1]') 
    submit_button.click()

    success_message = wait_for_element(driver, By.XPATH, '//*[@id="__nuxt"]/div/div/main/div/header/h1') 
    assert success_message.is_displayed(), "Mensagem de sucesso não encontrada!"


    # Adiciona uma verificação (opcional)
    print("Login submetido com sucesso!")
