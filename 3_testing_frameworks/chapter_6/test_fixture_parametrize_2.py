import pytest
import math
import time


@pytest.mark.parametrize('step', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, step):
    link = "https://stepik.org/lesson/{}/step/1".format(step)
    browser.get(link)

    answer_f = math.log(int(time.time()))
    answer = str(answer_f)

    browser.find_element_by_tag_name('textarea').send_keys(answer)
    browser.find_element_by_css_selector('[class="submit-submission "]').click()

    correct_text_el = browser.find_element_by_css_selector('[class="smart-hints__hint"]')
    correct_text = correct_text_el.text

    print(correct_text)

    assert correct_text == "Correct!", "Should be an exact match"
