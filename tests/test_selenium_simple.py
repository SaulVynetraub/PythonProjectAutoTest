import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import pytest


def test_search_example(selenium):
    """Ищет предмет запроса и делает скриншот страницы."""
    selenium.get('https://google.com')  # открыть стартовую страницу Гугл
    time.sleep(5)  # для просмотра процесса теста
    search_input = selenium.find_element(By.NAME, 'q')  # найти поле для ввода поискового запроса
    search_input.clear()  # очистить поле
    search_input.send_keys('last test')  # ввести поисковый запрос
    time.sleep(5)
    search_button = selenium.find_element(By.NAME, 'btnK')  # найти кнопку "Начать поиск"
    search_button.submit()  # нажать/команда "Ввод"
    time.sleep(5)
    selenium.save_screenshot('result.png')  # сохранить скриншот с результатами

# python -m pytest -v --driver Chrome --driver-path C:\chromedriver\chromedriver.exe tests\test_selenium_simple.py
