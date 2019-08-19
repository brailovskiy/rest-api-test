from hamcrest import *
from api.rooms import Rooms
import allure


class TestGetRoomsNoRole:
    """ Тесты категории Rooms, метод GET /rooms, авторизационный токен отсутствует """
    def test_get_rooms_no_role(self, free_room_number, delete_session):
        """
            Тест попытки получения списка номеров без авторизационного токена
            Проверка недоступности данного метода без авторизационного токена.
            Тестирование с различными параметрами проводится в другом модуле от пользователя с ролью сотрудник
        """
        with allure.step('Запрос на получение списка номеров комнат'):
            r = Rooms().get_rooms()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
