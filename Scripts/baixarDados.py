from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from os.path import exists
import caminhosArquivos as path
import processarDados as prod

hoje = prod.dataHoje()
ontem = prod.dataOntem()

def baixarDessem():
    print("\nINICIANDO CHROME DRIVER - BAIXAR DESSEM\n")
    try:
        driver = webdriver.Chrome(executable_path=path.caminhoChromeDriver())
        driver.get("https://www.ccee.org.br/web/guest/acervo-ccee")
        driver.maximize_window()
        time.sleep(5)
    except Exception as e:
        print("\nNÃO FOI POSSÍVEL INICIAR O CHROME DRIVER\n"+str(e))

    driver.find_element(By.XPATH, "//*[contains(text(),'Aceitar cookies')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "keyword").send_keys("DESSEM")
    driver.find_element(By.XPATH, "(//span[@id='search-key'])[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@class='card-title']").send_keys(Keys.ENTER)
    time.sleep(30)
    driver.close()
    file_exists = exists(path.caminhoDiretorio()+path.nomeArquivoDessem())

    if file_exists == True:
        print("\nDOWNLOAD DESSEM CONCLUÍDO - CHROME DRIVER\n")
    else:
        print("\nARQUIVO DESSEM NÃO ENCONTRADO\n")

def baixarPreco():
    print("\nINICIANDO CHROME DRIVER - BAIXAR PREÇOS DIÁRIOS\n")
    try:
        driver = webdriver.Chrome(executable_path=path.caminhoChromeDriver())
        driver.get("https://www.ccee.org.br/web/guest/precos/painel-precos")
        driver.maximize_window()
        time.sleep(5)
    except Exception as e:
        print("\nNÃO FOI POSSÍVEL INICIAR O CHROME DRIVER\n"+str(e))

    driver.find_element(By.XPATH, "//*[contains(text(),'Aceitar cookies')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "inputInitialDate").send_keys(ontem)
    driver.find_element(By.ID, "inputFinalDate").send_keys(hoje)
    driver.find_element(By.ID, "tipoPreco").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "tipoPreco").send_keys(Keys.ARROW_DOWN)
    driver.find_element(By.ID, "tipoPreco").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "filtrarHistoricoPreco").send_keys(Keys.ENTER)
    time.sleep(10)
    driver.close()
    file_exists = exists(path.caminhoDiretorio()+path.nomeArquivoPreco())

    if file_exists == True:
        print("\nDOWNLOAD PREÇOS CONCLUÍDO - CHROME DRIVER\n")
    else:
        print("\nARQUIVO PREÇOS NÃO ENCONTRADO\n")