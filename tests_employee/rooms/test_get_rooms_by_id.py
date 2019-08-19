from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestGetRoomsByIdEmployee:
    """ Тесты категории Rooms, метод GET /rooms/id, роль - сотрудник """
    def test_get_rooms_by_id_by_employee(self, use_session_employee):
        """ Тест получения информации о номере сотрудником """
        with allure.step('Запрос на получение информации о номере'):
            r = Rooms().get_room_by_san(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверка на успешный статус код и на верные SAN и номер комнаты в ответе'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(DV.SAN_MAIN_ROOM))
            assert_that(r.json()["number"], equal_to(DV.NUMBER_MAIN_ROOM))

    def test_get_rooms_by_incorrect_id_by_employee(self, use_session_employee):
        """ Тест попытки получить информацию о несуществующем номере сотрудником """
        with allure.step('Запрос на получение информации о номере'):
            r = Rooms().get_room_by_san(san="incorrect")

        with allure.step('Проверка на корректный ответ при попытке получить информацию о несуществующем номере'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_get_rooms_by_id_in_not_your_hotel_by_employee(self, use_session_employee):
        """ Тест попытки получить информацию о номере не в своей гостинице сотрудником """
        with allure.step('Запрос на получение информации о номере'):
            r = Rooms().get_room_by_san(san=DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверка, что сотрудник не может просмотреть информацию о номере в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
