import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_have_photo(go_to_my_pets):
    """Проверить, что на странице со списком питомцев пользователя хотя бы у половины питомцев есть фото."""
    # установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    # сохранение элементов статистики в statis
    statis = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    # сохранение элементов с img в images
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')
    # получение количества питомцев из данных статистики
    number = statis[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # нахождение половины от количества питомцев
    half = number // 2
    # нахождение количества питомцев с фотографией
    number_of_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_of_photos += 1
    # проверка, что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_of_photos >= half
    print(f'Количество фото: {number_of_photos}')
    print(f'Половина от числа питомцев: {half}')
