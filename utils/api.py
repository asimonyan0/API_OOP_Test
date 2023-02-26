from utils.http_methods import Http_methods

"""Можно собрать все тесты(не только Google maps) по api"""
"""Метод для тестирования Google maps api"""
base_url = "https://rahulshettyacademy.com"   # Базовый url
kay = "?key=qaclick123"                       # Параметр для всех запросов

class Google_maps_api:

    """ Метод для создания локации"""
    @staticmethod     # Сделаем методы статическими (без Self) и сможем вызывать в любом классе и в любом тесте, и не будем привязываться к этому классу
    def create_new_place():
        json_for_create_new_place = {
            "location": {

                "lat": -38.383494,

                "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

                "shoe park",

                "shop"

            ],

            "website": "http://google.com",

            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"    # Ресурс для метода post
        post_url = base_url + post_resource + kay     # Полный ресурс для запроса post
        print(post_url)

        result_post = Http_methods.post(post_url, json_for_create_new_place)  # Отправляем запрос по методу post из класса  Http_methods
        print(result_post.text)                       # Печатаем результат в формате text
        return result_post                            # Возвращаем результат запроса

    """ Метод для получения локации"""
    @staticmethod     # Сделаем методы статическими (без Self) и сможем вызывать в любом классе и в любом тесте, и не будем привязываться к этому классу
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"                            # Ресурс для метода get
        get_url = base_url + get_resource + kay + "&place_id=" + place_id    # Полный ресурс для запроса get
        print(get_url)
        result_get = Http_methods.get(get_url)   # Отправляем запрос по методу get из класса  Http_methods
        print(result_get.text)                   # Печатаем результат в формате text
        return result_get                        # Возвращаем результат запроса

    """ Метод для изменения локации"""
    @staticmethod   # Сделаем методы статическими (без Self) и сможем вызывать в любом классе и в любом тесте, и не будем привязываться к этому классу
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"                        # Ресурс для метода put
        put_url = base_url + put_resource + kay                             # Полный ресурс для запроса put
        print(put_url)
        json_for_update_new_place = {
            "place_id": place_id,

            "address": "TEST__ Lenina street, RU",

            "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_place)   # Отправляем запрос по методу get из класса  Http_methods
        print(result_put.text)                   # Печатаем результат в формате text
        return result_put                        # Возвращаем результат запроса

    """ Метод для удаления локации"""
    @staticmethod   # Сделаем методы статическими (без Self) и сможем вызывать в любом классе и в любом тесте, и не будем привязываться к этому классу
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"                        # Ресурс для метода delete
        delete_url = base_url + delete_resource + kay                          # Полный ресурс для запроса delete
        print(delete_url)
        json_for_delete_new_place = {
            "place_id": place_id
        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_place) # Отправляем запрос по методу delete из класса  Http_methods
        print(result_delete.text)               # Печатаем результат в формате text
        return result_delete                    # Возвращаем результат запроса






