import requests
from shared.constants import DefaultValues as DV
from shared.get_log import get_log


class Hotels:
    """ Методы категории Hotels """
    def __init__(self):
        self.headers = DV.HEADERS
        self.url = DV.URL + 'hotels'

    def get_hotels(self):
        """ Получить список гостиниц """
        r = requests.get(self.url, headers=self.headers)

        get_log(r)

        return r
