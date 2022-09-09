'''

Juraj Glatz
9.9.2022
Labuzo Zadanie

'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#options that keep window opened
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#chrome window opening with using defined options
window = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
window.get("https://www.gmail.com")

#insert username and click "next"
window.find_element(By.NAME, "identifier").send_keys("labuzo.uloha@gmail.com")
window.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()

window.implicitly_wait(5)

#insert password and log in
window.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys("8765labuzo1234")
window.find_element(By.XPATH, "//*[@id='passwordNext']/div/button/span").click()


#print("Hello world")

