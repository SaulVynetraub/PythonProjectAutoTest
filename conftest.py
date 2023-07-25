import pytest
import uuid
import pytest
import selenium
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_email, valid_password
from selenium import webdriver


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # this function helps to detect that some test failed and pass this information to teardown
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, 'rep_' + rep.when, rep)
#     return rep
#
#
# @pytest.fixture
# def web_browser(request, selenium):
#     browser = selenium
#     browser.set_window_size(1400, 1000)
#     # return browser instance to test case
#     yield browser
#     # do tear down (this code will be executed after each test)
#     if request.node.rep_call.failed:
#         # make the screenshot if test failed
#         try:
#             browser.execute_script("document.body.bgColor = 'white';")
#             # make screenshot for local debug
#             browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#             # for happy debugging
#             print('URL: ', browser.current_url)
#             print('Browser logs: ')
#             for log in browser.get_log('browser'):
#                 print(log)
#         except:
#             pass

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    pytest.driver.maximize_window()
    pytest.driver.get('http://petfriends.skillfactory.ru/login')  # переход на страницу авторизации
    yield
    pytest.driver.quit()


@pytest.fixture()
def go_to_my_pets():
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.ID, 'email')))
    # ввод электронной почты
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.ID, 'pass')))
    # ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    # нажатие на кнопку "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    # нажатие на раздел "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
