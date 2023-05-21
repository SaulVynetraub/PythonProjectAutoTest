from app.api import PetFriends
from settings import valid_password, valid_email, unvalid_password, \
    unvalid_email  # settings.py добавлен в gitignore

pf = PetFriends()  # создание образца класса

"""Ниже - тесты для коллекции API PetFriends. Проверки с корректными/некорректными данными."""


def test_get_api_key(email=valid_email, password=valid_password):
    """Получение API-ключа с корректными данными."""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_wrong_user(email=unvalid_email, password=unvalid_password):
    """Получение API-ключа с некорректными данными."""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_list_pets(filter=''):
    """Получение списка всех питомцев."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) >= 0


def test_get_list_my_pets(filter='my_pets'):
    """Получение списка моих питомцев."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) >= 0


def test_post_new_pet(
        name='Doggo',
        animal_type='Dogster',
        age='6',
        pet_photo='images/pet_photo.jpg'):
    """Создание нового питомца с фотографией."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age


def test_post_new_pet_clear_name(
        name='',
        animal_type='Catster',
        age='5',
        pet_photo='images/catto_1.jpg'):
    """Создание нового питомца с пустым полем 'name'."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_post_new_pet_strange_name(
        name='1@$!%!^!^!&!(&)!^_!+!$!%)!LLadsD@2!%%!%>>>>////,,,<<@%<15125@%!%!D!D"":@',
        animal_type='StrangeThing',
        age='2',
        pet_photo='images/catto_1.jpg'):
    """Создание нового питомца с произвольным набором символов в поле 'name'."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_post_new_pet_negative_age(
        name='Flask',
        animal_type='Django',
        age='-2',
        pet_photo='images/catto_1.jpg'):
    """Создание нового питомца с отрицательным возрастом."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age


def test_post_new_pet_clear_info(
        name='',
        animal_type='',
        age='',
        pet_photo='images/catto_1.jpg'):
    """Создание нового питомца с пустыми полями информации."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_delete_pet():
    """Удаление последнего созданного питомца из своего списка."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) == 0:  # проверка на пустой список
        pf.post_new_pet(auth_key, 'Git', 'Github', '4', 'images/doggo_2.jpg')  # создание питомца в своем списке
        _, my_pets = pf.get_list_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_pets(auth_key, 'my_pets')
    assert status == 200
    assert pet_id not in my_pets.values()


def test_delete_alien_pet():
    """Удаление последнего созданного питомца из общего списка."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_pets(auth_key, '')
    pet_id = pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, pets = pf.get_list_pets(auth_key, '')
    assert status == 200
    assert pet_id not in pets.values()


def test_post_new_photo(pet_photo='images/doggo_2.jpg'):
    """Замена фотографии последнего созданного питомца из своего списка."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) > 0:  # проверка, что в своем списке есть хотя бы один питомец
        status, result = pf.post_new_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
        _, my_pets = pf.get_list_pets(auth_key, 'my_pets')
        assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
    else:
        raise Exception('Clear list of pets.')


def test_post_new_photo_alien(pet_photo='images/doggo_2.jpg'):
    """Замена фотографии последнего созданного питомца из общего списка."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_pets(auth_key, '')
    status, result = pf.post_new_photo(auth_key, pets['pets'][0]['id'], pet_photo)
    _, pets = pf.get_list_pets(auth_key, '')
    assert status == 200
    assert result['pet_photo'] == pets['pets'][0]['pet_photo']


def test_update_pet_information(
        name='Justin',
        animal_type='Parrot',
        age='3'):
    """Обновление информации последнего созданного питомца из своего списка."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_information(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('Clear list of pets.')


def test_post_pet_information(
        name='Daniel',
        animal_type='Dragon',
        age='3'):
    """Создание нового питомца без фотографии."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_pet_information(auth_key, name, animal_type, age)
    assert status == 200
    assert result['animal_type'] == animal_type
