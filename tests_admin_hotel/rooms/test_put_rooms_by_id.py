from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.sdp_actions_room import RoomControl as RC
from shared.generate_data import DepartureDate
from api.rooms import Rooms
import allure


class TestPutRoomsByIdAdminHotel:
    """ Тесты категории Rooms, метод GET /rooms/id, роль - администратор гостиницы """
    def test_put_rooms_by_id_by_admin_hotel(self, use_session_admin_hotel, check_in_room_number):
        """ Тест изменения данных номера администратором гостиницы """
        with allure.step('Запрос на изменение данных комнаты'):
            r = Rooms(name="Guest Changed", checkout_date=4132252800, forbid_extra=True, language="ru",
                      pay_limit=15000, pin_required=False).put_room_by_san(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверки на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

        with allure.step('Проверки через метод SDP, что данные в комнате изменились'):
            new_name = RC().get_room_param('ServiceAccount_name')
            new_checkout_date = RC().get_room_param('ServiceAccount_lateCheckOut')
            new_forbid_extra = RC().get_room_param('ServiceAccount_forbidExtra')
            new_pay_limit = RC().get_room_param('ServiceAccount_payLimit')
            new_pin_required = RC().get_room_param('ServiceAccount_pinRequired')

            assert_that(new_name, equal_to("Guest Changed"))
            assert_that(new_checkout_date, equal_to(DepartureDate.parse_timestamp_to_sdp_format(4132263600)))
            assert_that(new_forbid_extra, equal_to("1"))
            assert_that(new_pay_limit, equal_to("15000"))
            assert_that(new_pin_required, equal_to("0"))

    def test_put_rooms_by_incorrect_id_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки изменить данные в несуществующем номере администратором гостиницы """
        with allure.step('Запрос на изменение данных комнаты с несуществующим SAN'):
            r = Rooms(name="Guest Changed").put_room_by_san(san="incorrect")

        with allure.step('Проверки на корректность ответа от сервера'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_put_rooms_by_id_in_not_your_hotel_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки изменить данные в номере не в своей гостинице администратором гостиницы """
        with allure.step('Запрос на изменение данных комнаты в чужой гостинице'):
            r = Rooms(name="Guest Changed").put_room_by_san(san=DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки, что сотрудник не может изменять данные комнат в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
