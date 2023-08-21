from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json

def get_lotacao():
    # url do cia
    url = "https://sistemas.joinville.udesc.br/cia/"

    # carregamento dos dados de login do arquivo json.
    # há um arquivo chamado login_template.json, basta copiar ele,
    # mudar o nome para login.json e inserir seus dados do CIA.

    # CUIDADO PARA NÃO VAZAR SEUS DADOS!!!!

    with open("./resources/login.json","r") as f:
        temp = json.load(f)
        login = temp["username"]
        senha = temp["password"]

    # inicialização do driver do selenium
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)

    # login no CIA
    driver.get(url)

    for element in driver.find_elements(By.TAG_NAME, "input"):
        if element.get_attribute("name") == "login":
            element.send_keys(login)
        if element.get_attribute("name") == "senha":
            element.send_keys(senha)

    for element in driver.find_elements(By.TAG_NAME,"button"):
        if element.get_attribute("type") == "submit":
            element.click()

    # Espera página carregar
    WebDriverWait(driver=driver, timeout=1).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    # pega o numero de pessoas na academia atulamente
    lotacao = int(driver.find_element(By.ID,"autoloading").find_element(By.TAG_NAME,"b").text)

    driver.close()

    return lotacao

