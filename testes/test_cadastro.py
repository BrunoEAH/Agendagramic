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
    # Configurações para rodar o Chrome em modo headless
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
def test_cadastro_submit(driver):
    
    # Navega para a página inicial
    driver.get("http://localhost:3000")
    
    # Aguarda o botão de cadastro na página inicial e clica
    signup_button = wait_for_element(driver, By.XPATH, '//*[@id="__nuxt"]/div/div/div/main/div[3]/button[2]')
    signup_button.click()
    print("Navegou para a página de cadastro com sucesso!")
    
    # Aguarda o campo de login (email/username) estar visível
    name_input = wait_for_element(driver, By.XPATH, '//*[@id="nome"]')  # Ajuste o XPath conforme necessário
    name_input.send_keys("Teste")  
    
    # Aguarda o campo de login (email/username) estar visível
    telegram_user_input = wait_for_element(driver, By.XPATH, '//*[@id="tgUser"]') 
    telegram_user_input.send_keys("@teste") 

    # Aguarda o campo de login (email/username) estar visível
    email_input = wait_for_element(driver, By.XPATH, '//*[@id="email"]') 
    email_input.send_keys("teste@email.com") 

    # Aguarda o campo de senha estar visível
    password_input = wait_for_element(driver, By.XPATH, '//*[@id="password"]')  # Ajuste o XPath conforme necessário
    password_input.send_keys("senha")  # Substitua por uma senha válida
    
    # Aguarda o campo de senha estar visível
    confirm_password_input = wait_for_element(driver, By.XPATH, '//*[@id="confirmPassword"]')  # Ajuste o XPath conforme necessário
    confirm_password_input.send_keys("senha")  # Substitua por uma senha válida

    # Aguarda o botão de submit estar clicável e clica
    submit_button = wait_for_element(driver, By.XPATH, '//*[@id="__nuxt"]/div/div/div/div[2]/form/button[1]')  # Ajuste o XPath conforme necessário
    submit_button.click()
    
    success_message = wait_for_element(driver, By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/form/h2')  # Ajuste o XPath
    assert success_message.is_displayed(), "Mensagem de sucesso não encontrada!"


    # Adiciona uma verificação (opcional)
    print("Cadastro submetido com sucesso!")
