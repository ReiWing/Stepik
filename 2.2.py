from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/selects2.html")

num1_element = browser.find_element_by_css_selector('[id="num1"]')
num1_str = num1_element.text
num1 = int(num1_str)
print(num1)

num2_element = browser.find_element_by_css_selector('[id="num2"]')
num2_str = num2_element.text
num2 = int(num2_str)
print(num2)

result_int = num1+num2
result = str(result_int)
print(result)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(result)

# browser.find_element_by_css_selector('[type="submit"]').click()
browser.execute_script("document.title='Script executing';alert('Robots at work');")
