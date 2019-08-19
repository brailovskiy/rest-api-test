from datetime import datetime
from faker import Faker
import logging
LOGGER = logging.getLogger(__name__)


class DepartureDate:
    """ Методы генерации даты и времени """
    def __init__(self):
        self.this_year = datetime.now().year
        self.old_year = str(self.this_year - 1)
        self.future_year = str(self.this_year + 1)
        self.old_date_time = datetime.now().strftime(self.old_year + "-%m-%d %H:%M")
        self.future_date_time = datetime.now().strftime(self.future_year + "-%m-%d %H:%M")
        self.now_date_time_uts = datetime.now().timestamp()

    def generate_old_date(self):
        """ Возвращает дату на год раньше текущей """
        return self.old_date_time

    def generate_future_date(self):
        """ Возвращает дату на год позже текущей """
        return self.future_date_time

    def generate_future_date_timestamp(self):
        """ Возвращает дату на год позже текущей в формате "TimeStamp" """
        pass

    def generate_now_date_timestamp(self):
        """ Возвращает текущую дату в формате "TimeStamp" """
        now_time = str(self.now_date_time_uts).partition('.')[0]
        return now_time

    @staticmethod
    def parse_sdp_date_get_date(sdp_date):
        """ Парсинг даты, если дата из SDP - возвращает только дату в формате year-month-day """
        full_date = str(sdp_date).rsplit(' ', 1)
        date = full_date[0]
        if "/" in date:
            date = date.split("/")
            date = list(reversed(date))
            day = date[1]
            month = date[2]
            date[2] = day
            date[1] = month
            date = "-".join(date)
        return date

    @staticmethod
    def parse_sdp_date_get_time(sdp_date):
        """ Парсинг даты, приходящей из SDP, возвращает только время без секунд """
        full_date = str(sdp_date).rsplit(' ', 1)
        time = full_date[1]
        time = time.split(':')
        if len(time) == 3:
            time = time[:-1]
            time = ':'.join(time)
        elif len(time) == 2:
            time = ':'.join(time)
        else:
            LOGGER.error("Incorrect time: " + str(time))
        return time

    @staticmethod
    def parse_timestamp_to_sdp_format(date_in_timestamp):
        """ Парсинг даты из Time Stamp в формат даты SDP """
        date = datetime.utcfromtimestamp(date_in_timestamp).strftime('%d/%m/%Y %H:%M:%S')
        return date


class Names:
    """ Методы генерации имени и фамилии """
    def __init__(self):
        self.full_name = Faker().name()

    def generate_name(self):
        """ Генерация полного имени """
        return self.full_name


class Password:
    """ Методы генерации пароля """
    def __init__(self):
        self.password = ""

    def generate_valid_password(self):
        """ Генерация пароля, соответствующего 4 условиям, а также минимальной длине """

        # Требования к паролю:
        # Длина - 10 или более символов
        # Выполнение 3 из 4 следующих условий:
        # 1. Наличие букв нижнего регистра
        # 2. Наличие букв верхнего регистра
        # 3. Наличие цифр
        # 4. Наличие спец.символов

        regex = "[a-z]{2}|[0-9]{3}|[A-Z]{2}|[!,#,$,%,&]{3}"
        pass

    def generate_short_password(self):
        """ Генерация короткого пароля (менее 10 символов) """
        pass

    def generate_password_with_two_main_conditions(self):
        """ Генерация пароля, соответствующего минимальной длине и двум из четырех обязательных условий """
        pass

    def generate_password_with_three_main_conditions(self):
        """ Генерация пароля, соответствующего минимальной длине и трем из четырех обязательных условий """


class Email:
    """ Методы генерации email """
    def __init__(self):
        self.email = Faker().email()

    def generate_valid_email(self):
        """ Генерация валидного email """
        return self.email


class SearchData:
    """
        Методы генерации номера комнаты
        Необходимо для проверки поиска по частичному/полному вхождению
    """

    @staticmethod
    def do_short_room_number(number):
        """ Из номера убирается последний символ """
        short_number = number[:-1]
        return short_number
