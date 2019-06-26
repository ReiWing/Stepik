import pytest
from selenium import webdriver
import math
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.mark.parametrize('step', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
@pytest.mark.parametrize('step', ["236895"])
def test_guest_should_see_login_link(browser, step):
    link = "https://stepik.org/lesson/{}/step/1".format(step)
    browser.get(link)
    time.sleep(2)

    answer = math.log(int(time.time()))
    answer = str(answer)
    print(answer)
    # WebDriverWait(browser, 12).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@data-type="string-quiz"]'), 'Type your answer here...')
    # )
    browser.find_element_by_css_selector('[data-type="string-quiz"]').send_keys(answer)
    # time.sleep(2)
    # browser.find_elementc_by_css_selector('[class="submit-submission "]').click()
    time.sleep(100)
