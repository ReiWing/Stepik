from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_css_selector('[id="input_value"]')
x_str = x_element.text
x = int(x_str)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)

answer = browser.find_element_by_css_selector('[id="answer"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(y)

robotCheckbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
robotCheckbox.click()

robotsRule = browser.find_element_by_css_selector('[for="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
robotsRule.click()

button = browser.find_element_by_css_selector('[type="submit"]').click()
