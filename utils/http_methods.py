# """ \Api_OOP_Stepik> python -m pytest --alluredir=allure_results/ tests/test_google_map_api.py  создаем директорию для allure
#  и пишем название теста, который хотим запускать. Для запуска всех тестов пишем python -m pytest --alluredir=allure_results/ tests/"""

# """ Api_OOP_Stepik> allure serve allure_results  В Командной Строке  WINDOWS!! можно генерить отчет в браузере
# или allure serve C:\Users\Armen\PycharmProjects\Api_OOP_Stepik\allure_results  в консоли IDE"""

import allure
import requests

from utils.logger import Logger

"""Список HTTP методов"""
class Http_methods:
    headers = {'Content-Type': 'application/json'}  # заголовки будем передать в формате json
    cookie = ""

    # Сделаем методы статическими (без Self) и сможем вызывать в любом классе и в любом тесте, и не будем привязываться к этому классу
    @staticmethod
    @allure.step("Allure step name: Method Get")
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        # Logger.add_response(result)
        return result

    @staticmethod
    @allure.step("Allure step name: Method Post")
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        # Logger.add_response(result)
        return result

    @staticmethod
    @allure.step("Allure step name: Method Put")
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        # Logger.add_response(result)
        return result

    @staticmethod
    @allure.step("Allure step name: Method Delete")
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        # Logger.add_response(result)
        return result







