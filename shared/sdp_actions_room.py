import requests
from shared.constants import DefaultValues as DV
from shared.constants import SdpAuthData
import os
import pickle
from shared.get_log import get_log


class RoomControl:
    """ Методы данных комнаты (используются сервисы старой SDP) """
    def __init__(self, san=DV.SAN_MAIN_ROOM, room_id=DV.SDP_MAIN_ROOM_ID):
        self.url = DV.SDP_URL
        self.san = san
        self.room_id = room_id

        self.file = os.path.join(os.path.dirname(os.path.abspath(__file__.rsplit('/', 1)[0])), 'cookies')
        with open(self.file, 'a') as f:
            f.close()

        self.cookies = self.load_cookies(self.file)

    def get_cookies(self):
        """ Авторизация для получения куков """
        r = requests.post(self.url + "User/simple_login", data=SdpAuthData.SDP_AUTH_DATA)
        response = r.json()
        if response['code'] == 1:
            get_log(r)
            raise ValueError('Failed to log in to SDP')

        get_log(r)

        self.save_cookies(r.cookies, self.file)

    def clear_cookies(self):
        """ Очищение файла с куками """
        self.save_cookies(None, self.file)

    @staticmethod
    def save_cookies(requests_cookiejar, filename):
        """ Сохранение куков в файл """
        with open(filename, 'wb') as f:
            pickle.dump(requests_cookiejar, f)

    @staticmethod
    def load_cookies(filename):
        """ Загрузка куков из файла """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except EOFError:
            pass

    def check_out_room(self):
        """ Выселение комнаты посредством метода SDP """
        body = {'serviceAccountNumber': self.san}
        r = requests.post(self.url + "ServiceAccount/check_out", data=body, cookies=self.cookies)

        get_log(r)

        return r

    def check_in_room(self):
        """ Вселение комнаты посредством метода SDP """
        body = {'serviceAccountNumber': self.san,
                'name': 'Guest'}
        r = requests.post(self.url + "ServiceAccount/check_in", data=body, cookies=self.cookies)

        get_log(r)

        return r

    def get_profile_list(self):
        """ Вызов метода SDP, который возвращает параметры учетной записи """
        room_id = self.room_id
        body = {'ID': room_id}
        r = requests.post(self.url + "ServiceAccount/list", data=body, cookies=self.cookies)

        get_log(r)

        return r

    def parse_response(self):
        """ Парсинг ответа из get_profile_list и возвращение json'а с основными параметрами """
        response = self.get_profile_list()
        data = response.json()
        rows = data['rows'][0]
        return rows

    def get_room_param(self, param):
        """ Возвращает значение выбранного параметра для комнаты """

        # Параметры комнаты:
        # 'ServiceAccount_pinCode' - пин код, установленный в комнате
        # 'language_externalId' - локализация, установленная в номере
        # 'state_name' - статус комнаты (вселен/выселен)
        # 'ServiceAccount_payLimit' - платежный лимит (в копейках)
        # 'ServiceAccount_name' - имя гостя
        # 'ServiceAccount_lateCheckOut' - дата выселения
        # 'ServiceAccount_forbidExtra' - запрет покупок (0 - запрещены, 1 - разрешены)
        # 'ServiceAccount_pinRequired' - покупки с ПИН-кодом или без (0 - с, 1 - без)
        # 'ServiceAccount_additionalInfo' - номер комнаты

        all_params = self.parse_response()
        room_param = all_params[param]
        return room_param
