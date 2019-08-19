from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestPutRoomsByIdNoRole:
    """ Тесты категории Rooms, метод GET /rooms/id, авторизационный токен отсутствует """
    def test_put_rooms_by_id_no_role(self, check_in_room_number, delete_session):
        """ Тест попытки изменения данных номера без авторизационного токена """
        with allure.step('Запрос на изменение данных номера'):
            r = Rooms(name="Guest Changed", checkout_date=4132252800, forbid_extra=True, language="ru",
                      pay_limit=15000, pin_required=False).put_room_by_san(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
