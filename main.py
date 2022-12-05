from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.malbuner.ch/25-jubilaeum-gewinnspiel")

browser.maximize_window()

# Remove Cookie Warning
sleep(.5)
cookie = browser.find_element(By.XPATH, value="/html/body/div/div/div/div/div/button")
cookie.click()


# Scroll to Form like a Human
sleep(5)
jetzt_teilnehmen = browser.find_element(By.XPATH, value="/html/body/div/div/div/div/div/div/div/section/div/button")
jetzt_teilnehmen.click()

# Fill out the Form, start with the correct answer
sleep(5)

input = browser.find_elements(By.XPATH, value="/html/body/div/div/div/div/div/div/div/section/div/div/div/form/div/div/label/span/input")
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

# Accept Conditions
sleep(.1)
input[3].click()

sleep(.2)
input[4].click()

sleep(.2)
send = browser.find_element(By.XPATH, value="/html/body/div/div/div/div/div/div/div/section/div/div/div/form/div/div/button")
send.click()

sleep(5)


browser.quit()

exit(0)