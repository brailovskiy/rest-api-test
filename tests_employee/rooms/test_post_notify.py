from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestPutUsersByIdEmployee:
    """ Тесты категории Rooms, метод POST /rooms/notify, роль - сотрудник """
    def test_post_notify_by_employee(self, use_session_employee):
        """ Тест отправки нотификации в несколько номеров сотрудником """
        with allure.step('Запрос на отправку нотификации в два номера'):
            r = Rooms().post_notify_to_select_rooms(DV.SAN_MAIN_ROOM, DV.SAN_SECOND_ROOM)

        with allure.step('Проверки на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

    def test_post_notify_to_empty_room_by_employee(self, use_session_employee):
        """ Тест отправки нотификации без указания номера комнаты сотрудником """
        with allure.step('Запрос на отправку нотификации без указания номера'):
            r = Rooms().post_notify_to_select_rooms()

        with allure.step('Проверки на корректный ответ от сервера (неверные параметры запроса)'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(1003))
            assert_that(r.json()["description"], equal_to("Invalid form's parameters"))
            assert_that(r.json()["details"]["receivers"], equal_to("min 1"))

    def test_post_notify_to_incorrect_room_by_employee(self, use_session_employee):
        """ Тест отправки нотификации в несуществующую комнату сотрудником """
        with allure.step('Запрос на отправку нотификации в комнату с несуществующим SAN'):
            r = Rooms().post_notify_to_select_rooms("incorrect_room")

        with allure.step('Проверки на корректный ответ от сервера (комната не найдена)'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(9))
            assert_that(r.json()["description"], equal_to("Room is not found"))

    def test_post_notify_to_room_in_another_hotel_by_employee(self, use_session_employee):
        """ Тест отправки нотификации в комнату чужого отеля сотрудником """
        with allure.step('Запрос на отправку нотификации в комнату чужого отеля'):
            r = Rooms().post_notify_to_select_rooms(DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки на корректный ответ от сервера (комната не найдена)'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(9))
            assert_that(r.json()["description"], equal_to("Room is not found"))

    def test_post_notify_with_incorrect_display_type_by_employee(self, use_session_employee):
        """ Тест отправки нотификации с некорректным параметром display_type сотрудником """
        with allure.step('Запрос на отправку нотификации в комнату с некорректным значением параметра display_type'):
            r = Rooms(display_type="incorrect_display_type").post_notify_to_select_rooms(DV.SAN_MAIN_ROOM)

        with allure.step('Проверки на корректный ответ от сервера (неверные параметры запроса)'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(1003))
            assert_that(r.json()["description"], equal_to("Invalid form's parameters"))
