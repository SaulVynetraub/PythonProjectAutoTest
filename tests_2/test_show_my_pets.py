import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from settings_2 import valid_email, valid_password


def test_show_my_pets():
    """Проверить, что осуществляется переход на страницу со списком питомцев пользователя."""
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.ID, 'email')))
    # ввод почты
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
    # клик по ссылке "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
    # проверка, что переход на страницу "Мои питомцы" осуществлен
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

# python -m pytest -v --driver Chrome --driver-path C:\chromedriver\chromedriver.exe tests\test_show_my_pets.py