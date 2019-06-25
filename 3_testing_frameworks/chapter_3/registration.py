import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_registration_1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name = "Rei"
        surname = "Wing"
        email = "reiwing@6400.com"

        browser.find_element_by_xpath("//input[@placeholder='Введите имя']").send_keys(name)
        browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']").send_keys(surname)
        browser.find_element_by_xpath("//input[@placeholder='Введите Email']").send_keys(email)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

    def test_registration_2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name = "Rei"
        surname = "Wing"
        email = "reiwing@6400.com"

        browser.find_element_by_xpath("//input[@placeholder='Введите имя']").send_keys(name)
        browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']").send_keys(surname)
        browser.find_element_by_xpath("//input[@placeholder='Введите Email']").send_keys(email)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


if __name__ == "__main__":
    unittest.main()
