import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_no_duplicate_pets(go_to_my_pets):
    """Проверить, что на странице со списком питомцев пользователя нет повторяющихся питомцев."""
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    # сохранение элементов с данными о питомцах в data
    data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    list_data = []
    for i in range(len(data)):
        data_pet = data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)
    # склеиваются имя, возраст и порода; получившиеся слова добавляются в строку
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '
    # получение списка из line
    list_line = line.split(' ')
    # превращение списка в множество
    set_list_line = set(list_line)
    # нахождение количества элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)
    # из элементов списка вычитается количество элементов множества
    result = a - b
    # если количество элементов == 0, то карточки с одинаковыми данными отсутствуют
    assert result == 0
