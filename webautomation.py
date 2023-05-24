import pandas as pd

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

tabela = pd.read_excel("commodities.xlsx")

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

navegador.get("https://www.melhorcambio.com/milho-hoje")
cotacao = navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
cotacao = cotacao.replace(".", "").replace(",", ".")
cotacao = float(cotacao)
tabela.loc[0, "Preço Atual"] = cotacao
print(tabela)
