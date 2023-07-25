from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email("adadad@jjaag.com")
    page.enter_pass("1234")
    page.btn_click()

    assert page.get_relative_link() == '/all_pets', 'login_error'
    time.sleep(5)

# python -m pytest -v --driver Chrome --driver-path C:\chromedriver\chromedriver.exe test_auth_page.py
