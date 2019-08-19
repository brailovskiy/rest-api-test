from hamcrest import *
from api.devices import Devices
from shared.constants import DefaultValues as DV
import allure


class TestGetDevicesAdminRt:
    """ Тесты категории devices, метод GET /device_slots, роль - администратор Ростелеком """
    def test_get_device_slots_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки получения списка доступных слотов для привязки устройства """
        with allure.step('Запрос на получение списка доступных слотов для привязки устройств'):
            r = Devices().get_device_slots_by_san(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что администратор Ростелеком не может просмотреть список доступных слотов в номере'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to('Forbidden'))
