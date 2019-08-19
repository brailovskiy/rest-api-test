import requests
from shared.constants import DefaultValues as DV
from shared.get_log import get_log


class Healthcheck:
    """ Метод проверки статуса состояния сервера """
    def __init__(self):
        self.headers = DV.HEADERS
        self.url = DV.URL + 'healthcheck'

    def get_healthcheck(self):
        """ Получить состояние сервера """
        r = requests.get(self.url, headers=self.headers)

        get_log(r)

        return r
