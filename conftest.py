# -*- coding: utf-8 -*-
import pytest
from shared.sdp_actions_room import RoomControl as RC
from api.sessions import Sessions
from shared.constants import *
from api.users import Users
from settings import create_env_properties
import time
import logging
import allure


@pytest.fixture(scope="session", autouse=True)
def write_allure_env():
    """ Write environment to alluredir """
    yield

    create_env_properties()


@pytest.fixture(scope="session", autouse=True)
def get_sdp_session():
    """ Авторизация в SDP """
    RC().get_cookies()

    yield

    RC().clear_cookies()


@pytest.fixture(scope="session", autouse=True)
def get_session_employee():
    """ Получение сессии пользователя с ролью сотрудник """
    time.sleep(2)
    r = Sessions(email=UserAuthData().EMPLOYEE['email'],
                 password=UserAuthData().EMPLOYEE['password']).get_new_session()

    session_id = r.json()['session_id']

    yield session_id

    Sessions().delete_session_by_id(session_id)


@pytest.fixture(scope="session", autouse=True)
def get_session_admin_hotel():
    """ Получение сессии пользователя с ролью администратор гостиницы """
    time.sleep(2)
    r = Sessions(email=UserAuthData().ADMIN_HOTEL['email'],
                 password=UserAuthData().ADMIN_HOTEL['password']).get_new_session()

    session_id = r.json()['session_id']

    yield session_id

    Sessions().delete_session_by_id(session_id)


@pytest.fixture(scope="session", autouse=True)
def get_session_admin_rt():
    """ Получение сессии пользователя с ролью администратор МРФ """
    time.sleep(2)
    r = Sessions(email=UserAuthData().ADMIN_MRF['email'],
                 password=UserAuthData().ADMIN_MRF['password']).get_new_session()

    session_id = r.json()['session_id']

    yield session_id

    Sessions().delete_session_by_id(session_id)


@pytest.fixture(scope="function")
def free_room_number():
    """ Свободная главная комната """
    status = RC().get_room_param('state_name')

    if status == 'Active':
        RC().check_out_room()
    elif status == 'CheckOut':
        pass
    else:
        raise ValueError('Unknown room status: ' + status)

    yield


@pytest.fixture(scope="function")
def check_in_room_number():
    """ Заселенная главная комната """
    status = RC().get_room_param('state_name')

    if status == 'Active':
        RC().check_out_room()
        RC().check_in_room()
    elif status == 'CheckOut':
        RC().check_in_room()
    else:
        raise ValueError('Unknown room status: ' + status)

    yield


@pytest.fixture(scope="function")
def create_user_admin_hotel(get_session_admin_rt):
    """ Фикстура создания нового администратора гостиницы """
    r = Users(role_id=1).create_user(get_session_admin_rt)
    user_id = r.json()["id"]
    time.sleep(1)

    yield user_id

    # Удаляем пользователя на случай, если он не удалился в тесте (если удалился - ничего страшного, метод вернет 500)
    Users().delete_user_by_id(user_id, get_session_admin_rt)


@pytest.fixture(scope="function")
def create_user_employee(get_session_admin_rt):
    """ Фикстура создания нового сотрудника """
    r = Users(role_id=0).create_user(get_session_admin_rt)
    user_id = r.json()["id"]
    time.sleep(1)

    yield user_id

    # Удаляем пользователя на случай, если он не удалился в тесте (если удалился - ничего страшного, метод вернет 500)
    Users().delete_user_by_id(user_id, get_session_admin_rt)


@pytest.fixture(scope="function")
def check_user(get_session_admin_rt):
    """ Фикстура проверки существования пользователя по его ID """
    def check_user_by_id(user_id):
        r = Users().get_user_by_id(user_id, get_session_admin_rt)
        user_status = r.status_code

        if user_status == 200:
            return True
        elif user_status == 404:
            return False
        else:
            raise ValueError("Unknown response from server, see logs")

    return check_user_by_id


# Данный функционал позволяет выводить логи в каждый шаг allure, где есть requests
class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('Log {}'.format(message)):
            pass

    def emit(self, record):
        self.log("[{}] {}".format(record.levelname, record.getMessage()))


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield
