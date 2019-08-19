import requests
from shared.constants import DefaultValues as DV
from models.room import Room
from models.room import Notify
from shared.get_log import get_log


class Rooms:
    """ Методы категории Rooms """
    def __init__(self, **kwargs):
        self.headers = DV.HEADERS
        self.url = DV.URL
        self.room_data = Room(**kwargs)
        self.notify_body = Notify(**kwargs)

    def get_purchases(self, start_date=1544572800, end_date=None, san=None):
        """ Получить список покупок всех гостей номера """
        url = self.url + 'purchases?start_date=' + str(start_date)

        if end_date is not None and san is not None:
            url = url + '&end_date=' + str(end_date) + '&room_id=' + san
        elif end_date is not None and san is None:
            url = url + '&end_date=' + str(end_date)
        elif end_date is None and san is not None:
            url = url + '&room_id=' + san

        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def get_rooms(self, **kwargs):
        """ Получить список всех комнат """
        url = self.url + 'rooms'
        if kwargs:
            url = url + "?"
            i = 0
            for arg in kwargs:
                i += 1
                url = url + str(arg) + "=" + str(kwargs[arg])
                if i > 0:
                    if i < len(kwargs):
                        url = url + "&"

        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def post_notify_to_select_rooms(self, *args):
        """ Отправить сообщение в выбранные номера """
        url = self.url + 'rooms/notify'
        receivers = [*args]
        self.notify_body.receivers = receivers
        body = self.notify_body.do_dict()
        r = requests.post(url, headers=self.headers, json=body)

        get_log(r)

        return r

    def post_notify_to_all_rooms(self):
        """ Отправить сообщение в выбранные номера """
        url = self.url + 'rooms/notify_all'
        body = self.notify_body.do_dict_without_receivers()
        r = requests.post(url, headers=self.headers, json=body)

        get_log(r)

        return r

    def get_room_by_san(self, san):
        """ Получить комнату по SAN """
        url = DV.URL + 'rooms/' + san
        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def put_room_by_san(self, san):
        """ Изменить комнату с заданным SAN """
        url = DV.URL + 'rooms/' + san
        body = self.room_data.do_body_to_change_room()
        r = requests.put(url, headers=self.headers, json=body)

        get_log(r)

        return r

    def post_check_in(self, san):
        """ Запрос на заселение комнаты с заданным SAN """
        url = DV.URL + 'rooms/' + san + '/check_in'
        body = self.room_data.do_body_to_check_in()
        r = requests.post(url, headers=self.headers, json=body)

        get_log(r)

        return r

    def post_check_out(self, san):
        """ Запрос на выселение из комнаты с заданным SAN """
        url = DV.URL + 'rooms/' + san + '/check_out'
        r = requests.post(url, headers=self.headers)

        get_log(r)

        return r

    def post_change_number(self, san):
        """
            Запрос на изменение номера у комнаты с заданным SAN
            (меняется только номер комнаты, а SAN остается прежним)
        """
        url = DV.URL + 'rooms/' + san + '/number'
        body = self.room_data.do_body_to_update_number()
        r = requests.post(url, headers=self.headers, json=body)

        get_log(r)

        return r

    def get_purchases_by_san(self, san):
        """ Получить список покупок в комнате с заданным SAN """
        url = DV.URL + 'rooms/' + san + '/purchases'
        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r

    def post_update_pin_by_san(self, san):
        """
            Запрос на изменение пин-кода у комнаты с заданным SAN
            (новый пин-код генерируется автоматически)
        """
        url = DV.URL + 'rooms/' + san + '/update_pin'
        r = requests.post(url, headers=self.headers)

        get_log(r)

        return r

    def get_rooms_for_activation(self):
        """ Получить список номеров для активации """
        url = DV.URL + 'rooms_for_activation'
        r = requests.get(url, headers=self.headers)

        get_log(r)

        return r
