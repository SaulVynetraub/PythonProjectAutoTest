import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_all_pets_from_my_pets(go_to_my_pets):
    """Проверить, что на странице "Мои питомцы" присутствуют все питомцы."""
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    # сохранение элементов статистики в переменную "statis"
    statis = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    # сохранение карточек питомцев в переменную "pets"
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # получение количества питомцев из данных статистики
    number = statis[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # получение количества карточек питомцев
    number_of_pets = len(pets)
    # проверка, что количество питомцев из статистики совпадает с количеством карточек
    assert number == number_of_pets
