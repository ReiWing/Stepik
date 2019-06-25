from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )

button = browser.find_element_by_css_selector('[id="book"]')
button.click()

x_element = browser.find_element_by_css_selector('[id="input_value"]')
x_str = x_element.text
x = int(x_str)

x_element = browser.find_element_by_css_selector('[id="input_value"]')
x_str = x_element.text
x = int(x_str)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)
answer = browser.find_element_by_css_selector('[id="answer"]')
answer.send_keys(y)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()
