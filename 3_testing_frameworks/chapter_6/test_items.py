import time


def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    browser.find_element_by_css_selector('[id="add_to_basket_form"]')
    time.sleep(3)
