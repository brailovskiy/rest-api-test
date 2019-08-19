from hamcrest import *
from api.devices import Devices
from shared.constants import DefaultValues as DV
import allure


class TestPostRestartDeviceNoRole:
    """ Тесты категории devices, метод POST /device_slots/{id}/restart, авторизационный токен отсутствует """
    def test_post_restart_device_stb_no_role(self, delete_session):
        """ Тест попытки перезагрузки устройства STB """
        with allure.step('Запрос на перезагрузку STB'):
            r = Devices().post_restart_device_by_id(DV.FIRST_SLOT_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
