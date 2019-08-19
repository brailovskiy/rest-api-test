from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestGetRoomsByIdNoRole:
    """ Тесты категории Rooms, метод GET /rooms/id, авторизационный токен отсутствует """
    def test_get_rooms_by_id_no_role(self, delete_session):
        """ Тест попытки получить информацию о номере без авторизационного токена """
        with allure.step('Запрос на получение информации о номере'):
            r = Rooms().get_room_by_san(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
