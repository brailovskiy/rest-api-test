from shared.constants import DefaultValues as DV
from shared.generate_data import *


class User:
    """ Модель, описывающая пользователя """
    def __init__(self, **kwargs):
        # Некоторые дефолтные данные временно захардкожены
        self.client_id = kwargs.get("client_id", DV.MAIN_HOTEL_ID)
        self.email = kwargs.get("email", Email().generate_valid_email())
        self.name = kwargs.get("name", Names().generate_name())
        self.password = kwargs.get("password", "Q1w2e3r4t5y6!")
        self.role_id = kwargs.get("role_id", 0)

    def get_auth_data(self):
        """ Словарь с параметрами для авторизации """
        auth_data = dict()
        auth_data['email'] = self.email
        auth_data['password'] = self.password
        return auth_data

    def do_dict(self):
        """ Словарь с параметрами запроса для создания/редактирования пользователя """
        return self.__dict__
