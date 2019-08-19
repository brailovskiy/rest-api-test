import requests
from shared.constants import DefaultValues as DV
from shared.get_log import get_log


class Devices:
    """ Методы категории Devices """
    def __init__(self):
        self.headers = DV.HEADERS
        self.url = DV.URL

    def get_device_slots_by_san(self, san):
        """ Получить данные обо всех слотах для привязки в номере по SAN """
        url = self.url + 'device_slots?room_id=' + san
        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def post_restart_device_by_id(self, connection_id):
        """ Перезагрузить устройство по ID подключения """
        url = self.url + 'device_slots/' + connection_id + '/restart'
        r = requests.post(url, headers=self.headers)

        get_log(r)

        return r

    def post_unbind_device_by_id(self, connection_id):
        """ Отвязать устройство по ID подключения """
        url = self.url + 'device_slots/' + connection_id + '/unbind'
        r = requests.post(url, headers=self.headers)

        get_log(r)

        return r
