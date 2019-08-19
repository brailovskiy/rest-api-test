from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestPostUpdatePinNoRole:
    """ Тесты категории Rooms, метод POST /id/update_pin, авторизационный токен отсутствует """
    def test_update_pin_by_employee(self, check_in_room_number, delete_session):
        """ Тест попытки изменения ПИН-кода без авторизационного токена """
        with allure.step('Запрос на изменение ПИН-кода'):
            r = Rooms().post_update_pin_by_san(DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
