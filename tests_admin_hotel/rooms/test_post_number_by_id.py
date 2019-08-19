from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.sdp_actions_room import RoomControl as RC
from api.rooms import Rooms
import allure


class TestPostCheckInAdminHotel:
    """ Тесты категории Rooms, метод POST /id/number, роль - администратор гостиницы """
    def test_change_room_number_by_admin_hotel(self, use_session_admin_hotel, free_room_number):
        """ Тест изменения номера комнаты администратором гостиницы """
        with allure.step('Проверка, что перед тестом стоит дефолтный номер комнаты'):
            old_room_number = RC().get_room_param('ServiceAccount_additionalInfo')
            assert_that(old_room_number, equal_to(DV.NUMBER_MAIN_ROOM))

        with allure.step('Запрос на изменение номера комнаты'):
            r = Rooms(number="123").post_change_number(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверки на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

        with allure.step('Проверка через метод SDP, что номер комнаты поменялся'):
            room_number = RC().get_room_param('ServiceAccount_additionalInfo')
            assert_that(room_number, equal_to("123"))

        with allure.step('Выставление дефолтного значения номера комнаты'):
            Rooms(number=DV.NUMBER_MAIN_ROOM).post_change_number(san=DV.SAN_MAIN_ROOM)

    def test_change_room_number_in_another_hotel_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки изменить номер комнаты в другой гостинице администратором гостиницы """
        with allure.step('Запрос на изменение номера комнаты в номере чужой гостиницы по его SAN'):
            r = Rooms(number="123").post_change_number(DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки, что сотруднику запрещено изменять номера комнат в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_change_room_number_to_incorrect_room_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки изменить номер комнаты в несуществущем номере администратором гостиницы """
        with allure.step('Запрос на изменение номера комнаты с несуществующим SAN'):
            r = Rooms(number="123").post_change_number("incorrect")

        with allure.step('Проверки на корректный ответ от сервера'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
