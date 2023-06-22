import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Библиотека доступных методов запросов API PetFriends."""

    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email: str, password: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус и результат в формате JSON
        с уникальным ключом пользователя для указанной пары email-password."""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_pets(self, auth_key: json, filter: str = '') -> json:
        """Метод делает запрос к API сервера и возвращает статус и результат в JSON
        со списком найденных питомцев, совпадающих с указанным фильтром: либо всех, либо только своих."""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet(self, auth_key: json,
                     name: str,
                     animal_type: str,
                     age: str,
                     pet_photo: str) -> json:
        """Создание нового питомца с фотографией. Возвращает JSON с данными созданного питомца."""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Удаляет питомца по ID. Возвращает JSON с уведомлением об успешном удалении."""
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_photo(self, auth_key: json,
                       pet_id: str,
                       pet_photo: str) -> json:
        """Меняет фотографию питомца. Возвращает JSON с данными измененного питомца."""
        data = MultipartEncoder(fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')})
        headers = {'auth_key': auth_key['key'], 'Content-type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_information(self, auth_key: json,
                               pet_id: str,
                               name: str,
                               animal_type: str,
                               age: str) -> json:
        """Обновляет информацию питомца по ID. Возвращает JSON с новой информацией."""
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_pet_information(self, auth_key: json,
                             name: str,
                             animal_type: str,
                             age: str) -> json:
        """Создание нового питомца без фотографии. Возвращает JSON с данными созданного питомца."""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result
