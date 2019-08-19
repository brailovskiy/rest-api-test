from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.sdp_actions_room import RoomControl as RC
from api.rooms import Rooms
import allure


class TestPostCheckOutNoRole:
    """ Тесты категории Rooms, метод POST /id/checkout, авторизационный токен отсутствует """
    def test_check_out_by_employee(self, check_in_room_number, delete_session):
        """ Тест попытки выселения из номера без авторизационного токена """
        with allure.step('Запрос на выселение номера'):
            r = Rooms().post_check_out(DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

        with allure.step('Проверка через метод SDP, что комната осталась заселенной'):
            status = RC().get_room_param('state_name')
            assert_that(status, equal_to("Active"))
