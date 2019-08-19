from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestGetRoomsAdminHotel:
    """ Тесты категории Rooms, метод GET /rooms, роль - администратор гостиницы """
    def test_get_rooms_by_admin_hotel(self, use_session_admin_hotel, free_room_number):
        """
            Тест получения списка номеров администратором гостиницы
            Проверка доступности данного метода администратору гостиницы.
            Тестирование с различными параметрами проводится в другом модуле от пользователя с ролью сотрудник
        """
        with allure.step('Запрос на получение списка номеров'):
            r = Rooms().get_rooms()

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что в гостинице 3 номера'):
            assert_that(r.json()["rooms"], has_length(3))

        with allure.step('Проверки, что отображается информация о комнатах (на примере выселенной главной комнаты)'):
            assert_that(r.json()["rooms"][0]["id"], equal_to(DV.SAN_MAIN_ROOM))
            assert_that(r.json()["rooms"][0]["status"], equal_to("CheckOut"))
