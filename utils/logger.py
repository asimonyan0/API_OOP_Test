import datetime
import os

class Logger:
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod    # Метод write_log_to_file сможет обращаться к переменным класса (вместо self пишем cls)
    def write_log_to_file(cls, data: str):  # Данные будем хранить в виде строки(str)
        with open(cls.file_name, "a", encoding='utf-8') as logger_file:     # Откроем наш файл
            logger_file.write(data)                                         # Запишем туда данные, которые передадим при вызове

    @classmethod
    def add_request(cls, url: str, method: str):            # Получаем данные по нашему запросу
        test_name = os.environ.get("PYTEST_CURRENT_TEST")   # Помещаем в логи название теста, который выполняется

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"               # Будет добавляться(+=) к каждой новой строчке
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request: {method}\n"
        data_to_add += f"Request method: {url}\n"
        data_to_add = "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result):                  # Получаем ответ на наш запрос
        cookies_as_dict = dict(result.cookies)      # Обращаемся к нашим cookies, чтоб поместить их в лог файл
        headers_as_dict = dict(result.headers)      # Обращаемся к нашим headers, чтоб поместить их в лог файл

        data_to_add = f"Response code: {result.status_code}\n"  # Помещаем в лог файл status_code
        data_to_add += f"Response_text: {result.text}\n"        # Помещаем в лог файл ответ в формате text
        data_to_add += f"Response headers: {headers_as_dict}\n" # Помещаем в лог файл заголовки
        data_to_add += f"Response cookies: {cookies_as_dict}\n" # Помещаем в лог файл куки
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)