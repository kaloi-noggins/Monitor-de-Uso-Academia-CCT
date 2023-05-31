from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json

# url do cia
url = "https://sistemas.joinville.udesc.br/cia/"

# carregamento dos dados de login do arquivo json.
# há um arquivo chamado login_template.json, basta copiar ele,
# mudar o nome para login.json e inserir seus dados do CIA.

# CUIDADO PARA NÃO VAZAR SEUS DADOS!!!!

with open("login.json","r") as f:
    temp = json.load(f)
    login = temp["username"]
    senha = temp["password"]

# inicialização do driver do selenium
driver = webdriver.Firefox()

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
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

# pega o numero de pessoas na academia atulamente
result = driver.find_element("id","autoloading").find_element(By.TAG_NAME,"b")
print(result.text)