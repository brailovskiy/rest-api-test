import requests
from models.user import User
from shared.constants import DefaultValues as DV
from shared.get_log import get_log


class Sessions:
    """ Методы категории Sessions """
    def __init__(self, **kwargs):
        self.url = DV.URL + 'sessions'
        self.headers = DV.HEADERS
        self.body = User(**kwargs).get_auth_data()

    def create_session(self):
        """ Получить новую сессию для тестового модуля """
        r = requests.post(self.url, json=self.body, headers=self.headers)
        session = r.json()['session_id']

        get_log(r)

        self.headers['session_id'] = session

    def delete_session(self):
        """ Удалить сессию, добавленную в тестовом модуле """
        r = requests.delete(self.url, headers=self.headers)
        try:
            del self.headers['session_id']
        except KeyError:
            pass

        get_log(r)

        return r

    def get_new_session(self):
        """ Запрос на получение новой сессии """
        r = requests.post(self.url, json=self.body, headers=self.headers)

        get_log(r)

        return r

    def delete_session_by_id(self, session_id):
        """ Удалить сессию по id """
        headers = DV.HEADERS
        headers['session_id'] = session_id
        r = requests.delete(self.url, headers=headers)
        try:
            del self.headers['session_id']
        except KeyError:
            pass

        get_log(r)

        return r

    def put_session_id_into_headers(self, session_id):
        """ Поместить session_id в headers """
        self.headers['session_id'] = session_id

    def delete_session_id_from_headers(self):
        """ Удаление session_id из headers, если они там есть """
        try:
            del self.headers['session_id']
        except KeyError:
            pass
