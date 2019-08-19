import requests
from shared.constants import DefaultValues as DV
from models.user import User
from shared.get_log import get_log


class Users:
    """ Методы категории Users """
    def __init__(self, **kwargs):
        self.headers = DV.HEADERS
        self.url = DV.URL + 'users'
        self.body = User(**kwargs).do_dict()

    def get_roles(self):
        """ Получить список ролей. Авторизация для этого метода не требуется! """
        url = DV.URL + 'roles'
        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def get_users(self):
        """ Получить всех пользователей """
        r = requests.get(self.url, headers=self.headers)

        get_log(r)

        return r

    def post_user(self):
        """ Создание нового пользователя """
        r = requests.post(self.url, headers=self.headers, json=self.body)

        get_log(r)

        return r

    def get_users_me(self):
        """ Получить всех пользователей """
        url = self.url + '/me'
        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def delete_users_by_id(self, user_id):
        """ Удалить пользователя с выбранным id """
        url = self.url + '/' + str(user_id)
        r = requests.delete(url, headers=self.headers)

        get_log(r)

        return r

    def get_users_by_id(self, user_id):
        """ Получить данные пользователя с выбранным id """
        url = self.url + '/' + str(user_id)
        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def put_users_by_id(self, user_id):
        """ Изменить данные пользователя с выбранным id """
        url = self.url + '/' + str(user_id)
        r = requests.put(url, headers=self.headers, json=self.body)

        get_log(r)

        return r

    # Следующие 3 метода необходимы для фикстур. Они не затрагивают headers, который используется в тестах.
    # Работают с КОПИЕЙ headers!
    def create_user(self, session_id):
        """ Создание нового пользователя (для фикстуры) """
        headers = DV.HEADERS.copy()
        headers.update({'session_id': session_id})
        r = requests.post(self.url, headers=headers, json=self.body)

        get_log(r)

        return r

    def get_user_by_id(self, user_id, session_id):
        """ Получить данные пользователя с выбранным id (для фикстуры) """
        url = self.url + '/' + str(user_id)
        headers = DV.HEADERS.copy()
        headers.update({'session_id': session_id})
        r = requests.get(url, headers=headers)

        get_log(r)

        return r

    def delete_user_by_id(self, user_id, session_id):
        """ Удалить пользователя с выбранным id (для фикстуры) """
        url = self.url + '/' + str(user_id)
        headers = DV.HEADERS.copy()
        headers.update({'session_id': session_id})
        r = requests.delete(url, headers=headers)

        get_log(r)

        return r
