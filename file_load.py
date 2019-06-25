from selenium import webdriver
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element_by_css_selector('[name="firstname"]').send_keys('Rei')
browser.find_element_by_css_selector('[name="lastname"]').send_keys('Wing')
browser.find_element_by_css_selector('[name="email"]').send_keys('email@gmal.com')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element_by_css_selector('[id="file"]').send_keys(file_path)

browser.find_element_by_css_selector('[type="submit"]').click()
