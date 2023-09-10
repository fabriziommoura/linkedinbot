#importando selenium e webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#Abrindo Chrome
options = Options()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

(navegador) = webdriver.Chrome(options=options)

#Abrindo linkedin --> PERSONALIZE!

navegador.get("https://www.linkedin.com/feed/")

navegador.find_element('xpath','/html/body/div[1]/main/div/p/a').click()
navegador.find_element('xpath','//*[@id="username"]').send_keys('meuemail@gmail.com')
navegador.find_element('xpath','//*[@id="password"]').send_keys('SENHA')
navegador.find_element('xpath','//*[@id="organic-div"]/form/div[3]/button').click()

navegador.get("https://www.linkedin.com/search/results/people/?keywords=programador&origin=SWITCH_SEARCH_VERTICAL&sid=Tcg")
navegador.find_element('xpath','//*[@id="custom-message"]').send_keys('mensagem para a conexão')
#Developed by @fabriziommoura
