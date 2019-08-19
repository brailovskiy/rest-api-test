from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.sdp_actions_room import RoomControl as RC
from api.rooms import Rooms
import allure


class TestPostCheckOutEmployee:
    """ Тесты категории Rooms, метод POST /id/checkout, роль - сотрудник """
    def test_check_out_by_employee(self, use_session_employee, check_in_room_number):
        """ Тест выселения из номера сотрудником """
        with allure.step('Запрос на выселение из заселенной комнаты'):
            r = Rooms().post_check_out(DV.SAN_MAIN_ROOM)

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()['success'], is_(True))

        with allure.step('Получение через метод SDP статуса комнаты и проверка, что комната выселена'):
            status = RC().get_room_param('state_name')
            assert_that(status, equal_to("CheckOut"))

    def test_check_out_for_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки выселения из номера другой гостиницы сотрудником """
        with allure.step('Запрос на выселение из комнаты чужой гостиницы'):
            r = Rooms(name="Guest").post_check_out(DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки, что сотрудник не может выселять номера чужой гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_check_out_for_incorrect_room_by_employee(self, use_session_employee):
        """ Тест попытки выселения из несуществующего номера сотрудником """
        with allure.step('Запрос на выселение из комнаты с несуществующим SAN'):
            r = Rooms(name="Guest").post_check_out("incorrect")

        with allure.step('Проверки на корректность ответа от сервера при попытке выселить несуществующую комнату'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_check_out_for_empty_room_by_employee(self, use_session_employee, free_room_number):
        """ Тест выселения из выселенного номера сотрудником """
        with allure.step('Запрос на выселение из выселенной комнаты'):
            r = Rooms(name="Guest").post_check_out(DV.SAN_MAIN_ROOM)

        with allure.step('Проверки на корректность ответа от сервера (успешный ответ, комната остается выселенной)'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()['success'], is_(True))

        with allure.step('Получение через метод SDP статуса комнаты и проверка, что комната выселена'):
            status = RC().get_room_param('state_name')
            assert_that(status, equal_to("CheckOut"))
