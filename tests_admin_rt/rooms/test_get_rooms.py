from hamcrest import *
from api.rooms import Rooms
import allure


class TestGetRoomsAdminRt:
    """ Тесты категории Rooms, метод GET /rooms, роль - администратор Ростелеком  """
    def test_get_rooms_by_admin_rt(self, use_session_admin_rt, free_room_number):
        """ Тест попытки получения списка номеров """
        with allure.step('Запрос на получение списка номеров'):
            r = Rooms().get_rooms()

        with allure.step('Проверки, что администратор Ростелеком не может получить список номеров в любой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
