from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.sdp_actions_room import RoomControl as RC
from shared.generate_data import DepartureDate
from api.rooms import Rooms
import allure


class TestPostCheckInEmployee:
    """ Тесты категории Rooms, метод POST /id/checkin, роль - сотрудник """

    def test_check_in_by_employee(self, use_session_employee, free_room_number):
        """ Тест заселения номера сотрудником """
        with allure.step('Запрос на вселение гостя в пустую комнату'):
            r = Rooms(name="New Guest", checkout_date=4132252800, forbid_extra=True, language="ru",
                      pay_limit=15000, pin_required=False).post_check_in(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что при успешном заселении возвращается не пустые ПИН-код и памятка'):
            assert_that(r.json()["pin_code"], is_not(""))
            assert_that(r.json()["memo"], is_not(""))

        with allure.step('Получение через метод SDP статуса комнаты и проверка, что комната заселена'):
            status = RC().get_room_param('state_name')
            assert_that(status, equal_to("Active"), "Incorrect status after check in: " + status)

        with allure.step('Получение через метод SDP данных гостя вселенного номера и сравнение их с параметрами, '
                         'указанными в запросе'):
            new_name = RC().get_room_param('ServiceAccount_name')
            new_checkout_date = RC().get_room_param('ServiceAccount_lateCheckOut')
            new_forbid_extra = RC().get_room_param('ServiceAccount_forbidExtra')
            new_pay_limit = RC().get_room_param('ServiceAccount_payLimit')
            new_pin_required = RC().get_room_param('ServiceAccount_pinRequired')
            new_language = RC().get_room_param('language_externalId')

            assert_that(new_name, equal_to("New Guest"))
            assert_that(new_checkout_date, equal_to(DepartureDate.parse_timestamp_to_sdp_format(4132263600)))
            assert_that(new_forbid_extra, equal_to("1"))
            assert_that(new_pay_limit, equal_to("15000"))
            assert_that(new_pin_required, equal_to("0"))
            assert_that(new_language, equal_to("EN"))

    def test_check_in_to_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки заселения номера из другой гостиницы сотрудником """
        with allure.step('Запрос на вселение гостя в комнату чужой гостиницы'):
            r = Rooms(name="Guest").post_check_in(DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки, что сотрудник не может заселить комнату из чужой гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_check_in_to_incorrect_room_by_employee(self, use_session_employee):
        """ Тест попытки заселения в несуществующий номер сотрудником """
        with allure.step('Запрос на вселение гостя в комнату с несуществующим SAN'):
            r = Rooms(name="Guest").post_check_in("incorrect")

        with allure.step('Проверки на корректность ответа при попытке заселить несуществующую комнату'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
