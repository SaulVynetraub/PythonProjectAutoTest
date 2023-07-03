import pytest
import selenium
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_email, valid_password
from selenium import webdriver


@pytest.fixture(autouse=True)
def pytest_testing():
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
