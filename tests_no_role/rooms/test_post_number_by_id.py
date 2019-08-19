from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestPostCheckInNoRole:
    """ Тесты категории Rooms, метод POST /id/number, авторизационный токен отсутствует """
    def test_change_room_number_no_role(self, free_room_number, delete_session):
        """ Тест изменения номера комнаты без авторизационного токена """
        with allure.step('Запрос на изменение номера комнаты'):
            r = Rooms(number="123").post_change_number(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
