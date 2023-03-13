from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from fastapi import FastAPI, Request

app = FastAPI()

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")


def fb():

    browser = webdriver.Chrome(executable_path="C:/Users/Kachouri/Desktop/AI/Patient/geckodriver-v0.31.0-win32/chromedriver.exe", options=option)
    browser.get("http://facebook.com")
    browser.maximize_window()
    wait = WebDriverWait(browser, 15)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys('95116095')
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
    pass_field.send_keys('A4KHqcQLxvzCS9K')
    pass_field.send_keys(Keys.RETURN)

    time.sleep(5)
    browser.get("https://www.facebook.com/DiscoverTunisiacom")
    time.sleep(5)
    soup=bs(browser.page_source,"html.parser")
    time.sleep(5)
    with open('C:/Users/Kachouri/Desktop/facebookdata.csv', 'w') as result:
        writer = csv.writer(result, delimiter=",")
        writer.writerow(('Data_page',))
        writer.writerow(((str(soup))[:35000],))
    browser.quit()

    return "Done"

@app.get('/fb/')
def fastfb():
    return fb()
