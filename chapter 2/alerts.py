import math
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()

alert = browser.switch_to.alert
alert.accept()

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
