import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_all_info_my_pets(go_to_my_pets):
    """Проверка, что на странице "Мои питомцы" у всех питомцев есть фото, имя, возраст и порода."""
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    # сохранение элементов с данными питомцев в data
    data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    for i in range(len(data)):
        data_pet = data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3

# python -m pytest -v --driver Chrome --driver-path C:\chromedriver\chromedriver.exe tests_2\test_all_info_my_pets.py