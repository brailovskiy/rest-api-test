class Setting:
    """ Сущность: данные настроек """
    def __init__(self, **kwargs):
        self.day_change_time = kwargs.get('day_change_time')
        self.hello_message = dict()
        self.memo = dict()
        self.hello_message['EN'] = kwargs.get('hello_message_EN')
        self.hello_message['RU'] = kwargs.get('hello_message_RU')
        self.memo['EN'] = kwargs.get('memo_EN')
        self.memo['RU'] = kwargs.get('memo_RU')
        self.promo_on_startup_enabled = kwargs.get('promo_on_startup_enabled')

    def do_dict(self):
        """ Возвращает словарь со всеми параметрами комнаты """
        return self.__dict__
