from hamcrest import *
from api.devices import Devices
from shared.constants import DefaultValues as DV
import allure


class TestPostRestartDeviceAdminRt:
    """ Тесты категории devices, метод POST /device_slots/{id}/restart, роль - администратор Ростелеком """
    def test_post_restart_device_stb_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки перезагрузки устройства STB """
        with allure.step('Запрос на получение списка доступных слотов для привязки устройств'):
            r = Devices().post_restart_device_by_id(DV.FIRST_SLOT_ID)

        with allure.step(
                'Проверки, что администратор Ростелеком не может перезагружать устройства в номере'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
