import pytest
import requests
from settings import valid_email, valid_password
from app.api import PetFriends

# def python_string_slicer(str):  # функция для возврата подходящей строки
#     if len(str) < 50 or "python" in str:
#         return str
#     else:
#         return str[0:50]
#
#
# @pytest.fixture(scope="function", params=[  # идс - ид (тестовые случаи, 4), парамс - возможные параметры
#     ("Короткая строка", "Короткая строка"),
#     ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#      , "Длинная строка, не то чтобы прям очень длинная, но"),
#     ("Короткая строка со словом python", "Короткая строка со словом python"),
#     ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#      , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"),
# ], ids=["len < 50", "len > 50", "len < 50 contains python", "len > 50 contains python"])
# def param_fun(request):  # фикстура для параметризации тестов
#     return request.param
#
#
# def test_python_string_slicer(param_fun):  # тестовая функция, аргумент - своя фикстура param_fun
#     (input, expecter_output) = param_fun
#     result = python_string_slicer(input)
#     print(
#         "Входная строка: {0}\r\nВыходная строка: {1}\r\nОжидаемое значение: {2}".format(input, result, expecter_output))
#     assert result == expecter_output

# def ids_x(val):
#     return "x=({0})".format(str(val))
#
#
# def ids_y(val):
#     return "y=({0})".format(str(val))
#
#
# @pytest.mark.parametrize("x", [-1, 0, 1], ids=ids_x)  # параметризация с помощью спец. фикстуры
# @pytest.mark.parametrize("y", [100, 1000], ids=ids_y)
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True

pf = PetFriends()


def generate_string(n):  # генерирует строку нужной длины
    return "x" * n


def russian_chars():  # возвращает кириллические символы
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():  # возвращает китайские символы
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():  # возвращает специальные символы
    return '|\/!@#$%^&*()-_=+`~?"№;:[]{}'


@pytest.fixture(autouse=True)  # постоянная фикстура для получения апи-ключа и подстановки в тесты для других методов
def get_api_key():
    status, pytest.key = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert 'key' in pytest.key
    yield


@pytest.mark.parametrize("filter", [  # фикстура для загона параметров для негативных тестов метода
    generate_string(255),
    generate_string(1001),
    russian_chars(),
    russian_chars().upper(),
    special_chars(),
    special_chars(),
    123
], ids=[
    '255 symbols',
    'more than 1000 symbols',
    'russian',
    'RUSSIAN',
    'chinese',
    'specials',
    'digit'
])
def test_get_all_pets_with_negative_filter(filter):  # негативный тест для метода
    pytest.status, result = pf.get_list_pets(pytest.key, filter)
    assert pytest.status == 200


# @pytest.mark.parametrize("filter", ['', 'my_pets'], ids=['empty string', 'only my_pets'])  # фикстура для позит. тестов
# def test_get_all_pets_with_valid_key(filter):  # позитивный тест для метода
#     pytest.status, result = pf.get_list_pets(pytest.key, filter)
#     assert pytest.status == 200
#     assert len(result['pets']) > 0


@pytest.mark.parametrize("name", [  # тест post-метода только с позитивными (валидными) параметрами
    generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(),
    chinese_chars(), special_chars(), '123'], ids=[
    '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("animal_type", [
    generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(),
    chinese_chars(), special_chars(), '123'], ids=[
    '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("age", ['1'], ids=['min'])
def test_add_pet_information(name, animal_type, age):
    """Проверяем добавление питомца с различными данными."""
    pytest.status, result = pf.post_pet_information(pytest.key, name, animal_type, age)  # добавляем питомца
    assert pytest.status == 200  # сверяем полученный ответ с ожидаемым результатом
    assert result['name'] == name
    assert result['age'] == age
    assert result['animal_type'] == animal_type


@pytest.mark.parametrize("name", [''], ids=['empty'])  # тест с негативными параметрами
@pytest.mark.parametrize("animal_type", [''], ids=['empty'])
@pytest.mark.parametrize("age", [
    '', '-1', '0', '100', '1.5', '2147483647', '2147483648',
    special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()], ids=[
    'empty', 'negative', 'zero', 'greater than max',
    'float', 'int_max', 'int_max + 1', 'specials',
    'russian', 'RUSSIAN', 'chinese'])
def test_add_pet_information_negative(name, animal_type, age):
    pytest.status, result = pf.post_pet_information(pytest.key, name, animal_type, age)
    assert pytest.status == 400
