import requests
from shared.constants import DefaultValues as DV
from models.setting import Setting
from shared.get_log import get_log


class Settings:
    """ Методы категории Settings """
    def __init__(self, **kwargs):
        self.headers = DV.HEADERS
        self.url = DV.URL + 'settings'
        self.body = Setting(**kwargs).do_dict()

    def get_settings(self):
        """ Получить настройки гостиницы """
        r = requests.get(self.url, headers=self.headers)

        get_log(r)

        return r

    def put_settings(self):
        """ Изменить настройки гостиницы """
        r = requests.put(self.url, headers=self.headers, json=self.body)

        get_log(r)

        return r
