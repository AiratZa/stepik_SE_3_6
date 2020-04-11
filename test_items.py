from selenium.webdriver.common.by import By
# import time

def test_has_add_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    # time.sleep(30)
    browser.implicitly_wait(5)
    try:
        #если не найдет ни одного элемента, то длина (len) списка будет равна 0
        add_to_basket_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    finally:
        assert len(add_to_basket_button) > 0, "Can not find 'ADD TO BASKET' button"
