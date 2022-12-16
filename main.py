from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from time import sleep
import logging
import sys

logging.basicConfig(format='%(asctime)s %(message)s', filename='malbuner.log', encoding='utf-8', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
chrome_options = Options()
chrome_options.add_argument("--headless")

logging.info("open browser")
#browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)
browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver', options=chrome_options)

logging.info("open https://www.malbuner.ch/25-jubilaeum-gewinnspiel")
browser.get("https://www.malbuner.ch/25-jubilaeum-gewinnspiel")


browser.maximize_window()
logging.info("maximized window")
logging.info("on Page " + browser.title)

# Remove Cookie Warning
sleep(.5)
cookie = browser.find_element(By.XPATH, value="/html/body/div/div/div/div/div/button")
cookie.click()
logging.info("Clicked on Cookie Warning")

# Scroll to Form like a Human
sleep(5)
jetzt_teilnehmen = browser.find_element(By.XPATH, value="/html/body/div/div/div/div/div/div/div/section/div/button")
jetzt_teilnehmen.click()
logging.info("clicked on jetzt teilnehmen")

# Fill out the Form, start with the correct answer
sleep(5)

input = browser.find_elements(By.XPATH,
                              value="/html/body/div/div/div/div/div/div/div/section/div/div/div/form/div/div/label/span/input")
input[2].click()

sleep(3)
surname = browser.find_element(By.ID, value="surname")
surname.send_keys("Thiévent")

sleep(.5)
name = browser.find_element(By.ID, value="name")
name.send_keys("Florian")

sleep(.5)
email = browser.find_element(By.ID, value="email")
email.send_keys("florianjeremias@gmail.com")

sleep(.5)
street = browser.find_element(By.ID, value="street")
street.send_keys("Höhenweg 15")

sleep(.5)
plz = browser.find_element(By.ID, value="plz")
plz.send_keys("5222")

sleep(.5)
city = browser.find_element(By.ID, value="city")
city.send_keys("Umiken")

logging.info("filled the form")

# Accept Conditions
sleep(.1)
input[3].click()

sleep(.2)
input[4].click()

logging.info("accepted the conditions")

sleep(.2)
send = browser.find_element(By.XPATH,
                            value="/html/body/div/div/div/div/div/div/div/section/div/div/div/form/div/div/button")
send.click()

logging.info("sent form to server")

sleep(5)

browser.quit()

logging.info("closed browser")

exit(0)
