import json

import allure

from utils.api import Google_maps_api
from utils.checking import Checking

"""Создаем класс, в котором будем хранить шаги для теста"""

"""Создание, изменение, удаление новой локации"""
@allure.epic("Test Suite Name: Test create place")  # Если написать перед каждым классом (суит тестом), в отчете будет разделение от других классов
class Test_create_place:

    @allure.description("Test Create/Update/Delete New Place")  # Перед каждым тестом будет описание этого теста
    def test_create_new_place(self):
        print("\n --Начало работы метода POST--")

        """В переменную result_post храним экземпляр класса Google_maps_api, из которой вызываем необходимый метод (метод create_new_place)"""
        result_post = Google_maps_api.create_new_place()  # Обращаемся к методу create_new_place, чтоб выполнить метод POST
        check_post = result_post.json()                   # В переменную сохраняем ответ в формате json, для дальнейшей работы с ним
        place_id = check_post.get("place_id")             # Получаем значение поля "place_id"

        # all_tokens = json.loads(result_post.text)       # Получаем список Всех полей и печатаем, чтоб в ручную не вводить
        # print(list(all_tokens))
        Checking.check_status_code(result_post, 200)      # Вызовем метод для проверки статус кода
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id']) # Вызовем метод для проверки наличия обязательных полей
        Checking.check_json_value(result_post, 'scope', 'APP') # Вызовем метод для проверки статус кода

        print("\n --Начало работы метода GET(post)--")
        """В переменную result_get храним экземпляр класса Google_maps_api, из которой вызываем необходимый метод (метод GET)"""
        result_get = Google_maps_api.get_new_place(place_id) # Обращаемся к методу get_new_place, чтоб выполнить метод GET

        Checking.check_status_code(result_get, 200)          # Вызовем метод для проверки статус кода
        # all_tokens = json.loads(result_get.text)           # Получаем список Всех полей и печатаем, чтоб в ручную не вводить
        # print(list(all_tokens))
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'accuracy', '50') # Вызовем метод для проверки содержания полей

        print("\n --Начало работы метода PUT--")
        """В переменную result_put храним экземпляр класса Google_maps_api, из которой вызываем необходимый метод (метод PUT)"""
        result_put = Google_maps_api.put_new_place(place_id) # Обращаемся к методу put_new_place, чтоб выполнить метод PUT

        Checking.check_status_code(result_put, 200)          # Вызовем метод для проверки статус кода
        Checking.check_json_token(result_put, ['msg'])       # Вызовем метод для проверки наличия обязательных полей
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated') # Вызовем метод для проверки содержания полей

        print("\n --Начало работы метода GET(put)--")
        """В переменную result_get храним экземпляр класса Google_maps_api, из которой вызываем необходимый метод (метод GET)"""
        result_get = Google_maps_api.get_new_place(place_id) # Обращаемся к методу get_new_place, чтоб выполнить метод GET

        Checking.check_status_code(result_get, 200)          # Вызовем метод для проверки статус кода
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])              # Вызовем метод для проверки наличия обязательных полей
        Checking.check_json_value(result_get, 'name', 'Frontline house') # Вызовем метод для проверки содержания полей

        print("\n --Начало работы метода DELETE--")
        """В переменную result_delete храним экземпляр класса Google_maps_api, из которой вызываем необходимый метод (метод DELETE)"""
        result_delete = Google_maps_api.delete_new_place(place_id) # Обращаемся к методу delete_new_place, чтоб выполнить метод DELETE

        Checking.check_status_code(result_delete, 200)             # Вызовем метод для проверки статус кода
        # all_tokens = json.loads(result_delete.text)              # Получаем список Всех полей и печатаем, чтоб в ручную не вводить
        # print(list(all_tokens))
        Checking.check_json_token(result_delete, ['status'])       # Вызовем метод для проверки наличия обязательных полей
        Checking.check_json_value(result_delete, 'status', 'OK')   # Вызовем метод для проверки содержания полей

        print("\n --Начало работы метода GET(delete)--")
        """В переменную result_get храним экземпляр класса Google_maps_api, из которой вызываем необходимый метод (метод GET)"""
        result_get = Google_maps_api.get_new_place(place_id) # Обращаемся к методу get_new_place, чтоб выполнить метод GET

        Checking.check_status_code(result_get, 404)          # Вызовем метод для проверки статус кода
        Checking.check_json_token(result_get, ['msg'])       # Вызовем метод для проверки наличия обязательных полей
        Checking.check_json_search_word_in_value(result_get, 'msg', "Get operation failed") # Вызовем метод для проверки полей по заданному слову





