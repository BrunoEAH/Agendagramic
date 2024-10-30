import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Fixture para inicializar o WebDriver antes de cada teste e fechar após o teste
@pytest.fixture
def driver():
    driver_path = ChromeDriverManager().install()  # Instala e fornece o caminho do ChromeDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

# Teste para verificar a navegação para a página de Testes
def test_navigation_to_profile(driver):
    print("Iniciando test_navigation_to_profile")
    driver.get("http://localhost:3000")
    time.sleep(2)  # Espera para garantir que a página está carregada
    profile_button = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/div/div/div[2]/div[3]/button[1]")
    profile_button.click()
    time.sleep(3)  # Espera 3 segundos antes de fechar a janela

# Teste para verificar a navegação para a página de Login
def test_navigation_to_login(driver):
    print("Iniciando test_navigation_to_login")
    driver.get("http://localhost:3000")
    time.sleep(2)  # Espera para garantir que a página está carregada
    login_button = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/div/div/div[2]/div[3]/button[2]")
    login_button.click()
    time.sleep(3)  # Espera 3 segundos antes de fechar a janela

# Teste para verificar a navegação para a página de Cadastro
def test_navigation_to_register(driver):
    print("Iniciando test_navigation_to_register")
    driver.get("http://localhost:3000")
    time.sleep(2)  # Espera para garantir que a página está carregada
    
    # Localiza o botão de cadastro e tenta clicar diretamente ou com JavaScript
    register_button = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/div/div/div[2]/div[3]/button[3]")
    try:
        register_button.click()
    except:
        driver.execute_script("arguments[0].click();", register_button)
    
    time.sleep(3)  # Espera 3 segundos antes de fechar a janela

# Teste para verificar o link para o Telegram
def test_navigation_to_telegram(driver):
    print("Iniciando test_navigation_to_telegram")
    driver.get("http://localhost:3000")
    time.sleep(2)  # Espera para garantir que a página está carregada
    telegram_button = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/div/div/div[2]/div[3]/a")
    telegram_button.click()
    time.sleep(3)  # Espera 3 segundos antes de fechar a janela
