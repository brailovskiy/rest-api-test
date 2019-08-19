from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.sdp_actions_room import RoomControl as RC
from api.rooms import Rooms
import allure


class TestPostUpdatePinEmployee:
    """ Тесты категории Rooms, метод POST /id/update_pin, роль - сотрудник """
    def test_update_pin_by_employee(self, use_session_employee, check_in_room_number):
        """ Тест изменения ПИН-кода сотрудником """
        with allure.step('Сохранение установленного в номере пин-кода (метод SDP)'):
            old_pin = RC().get_room_param('ServiceAccount_pinCode')

        with allure.step('Запрос на изменение ПИН-кода'):
            r = Rooms().post_update_pin_by_san(DV.SAN_MAIN_ROOM)

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Сохранение нового пин-кода (метод SDP)'):
            new_pin = RC().get_room_param('ServiceAccount_pinCode')

        with allure.step('Проверка, что новый пин-код не совпадает со старым'):
            assert_that(old_pin, is_not(new_pin))

        with allure.step('Проверка соответсвия нового ПИН-кода (в SDP) и в ответе на запрос смены ПИН-кода в HTM'):
            assert_that(r.json()["pin_code"], equal_to(new_pin))

    def test_update_pin_in_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки изменения ПИН-кода в номере из другой гостиницы сотрудником """
        with allure.step('Запрос на изменение ПИН-кода в номере чужой гостиницы'):
            r = Rooms().post_update_pin_by_san(DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки, что сотрудник не может изменить ПИН-код в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_update_pin_in_incorrect_room_by_employee(self, use_session_employee):
        """ Тест попытки изменения ПИН-кода в несущестующем номере сотрудником """
        with allure.step('Запрос на изменение ПИН-кода в номере с несуществующим SAN'):
            r = Rooms().post_update_pin_by_san("incorrect")

        with allure.step('Проверки на корректный ответ от сервера'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
