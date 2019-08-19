from hamcrest import *
from api.devices import Devices
from shared.constants import DefaultValues as DV
import allure


class TestGetDevicesNoRole:
    """ Тесты категории devices, метод GET /device_slots, авторизационный токен отсутствует """
    def test_get_device_slots_no_role(self, delete_session):
        """ Тест попытки получения списка доступных слотов для привязки устройства без авторизационного токена """
        with allure.step('Запрос на получение списка доступных слотов'):
            r = Devices().get_device_slots_by_san(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
