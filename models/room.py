class Room:
    """ Сущность: комната """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.number = kwargs.get('number')
        self.status = kwargs.get('status')
        self.name = kwargs.get('name')
        self.pay_limit = kwargs.get('pay_limit')
        self.balance = kwargs.get('balance')
        self.pin_code = kwargs.get('pin_code')
        self.pin_required = kwargs.get('pin_required')
        self.forbid_extra = kwargs.get('forbid_extra')
        self.checkout_date = kwargs.get('checkout_date')
        self.memo = kwargs.get('memo')
        self.language = kwargs.get('language')

    def do_dict(self):
        """ Возвращает словарь со всеми параметрами комнаты """
        return self.__dict__

    def do_body_to_check_in(self):
        """ Возвращает словарь с данными для тела запроса POST /rooms/check_in """
        body = dict()
        body['checkout_date'] = self.checkout_date
        body['forbid_extra'] = self.forbid_extra
        body['language'] = self.language
        body['name'] = self.name
        body['pay_limit'] = self.pay_limit
        body['pin_required'] = self.pin_required
        return body

    def do_body_to_change_room(self):
        """ Возвращает словарь с данными для тела запроса PUT /rooms/id """
        body = dict()
        body['checkout_date'] = self.checkout_date
        body['forbid_extra'] = self.forbid_extra
        body['name'] = self.name
        body['pay_limit'] = self.pay_limit
        body['pin_required'] = self.pin_required
        return body

    def do_body_to_update_number(self):
        """ Возвращает словарь с данными для тела запроса POST /rooms/id/number """
        body = dict()
        body['number'] = self.number
        return body


class Notify:
    """ Сущность: тело сообщения """
    def __init__(self, **kwargs):

        # Основные параметры на текущий момент (другие игнорируются Smart TV приложением):
        # display:
        #   display_type: "popup"
        #   duration
        #   is_cancellable
        #   message
        # receivers

        self.display = dict()
        target = dict()
        link = dict()
        self.receivers = list()

        link['channel_id'] = kwargs.get('channel_id', 0)
        link['id'] = kwargs.get('id', 'string')
        link['media_item_type'] = kwargs.get('media_item_type', 'string')
        link['program_id'] = kwargs.get('program_id', 0)
        link['screen_name'] = kwargs.get('screen_name', 'string')

        target['link'] = link
        target['title'] = kwargs.get('title', 'string')
        target['type'] = kwargs.get('type', 'string')

        self.display['display_type'] = kwargs.get('display_type', 'popup')
        self.display['duration'] = kwargs.get('duration', 120)
        self.display['is_cancellable'] = kwargs.get('is_cancellable', True)
        self.display['message'] = kwargs.get('message', 'text message')
        self.display['target'] = target

        self.receivers = kwargs.get('receivers')

    def do_dict(self):
        """ Возвращает словарь со всеми параметрами тела сообщения """
        return self.__dict__

    def do_dict_without_receivers(self):
        """ Возвращает словарь с телом запроса для POST /rooms/notify_all без receivers """
        body = self.__dict__
        del body['receivers']
        return body
