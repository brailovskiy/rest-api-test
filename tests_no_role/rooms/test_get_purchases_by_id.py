from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestGetPurchasesByIdNoRole:
    """ Тесты категории Rooms, метод GET /id/purchases, авторизационный токен отсутствует """
    def test_get_purchases_by_id_no_role(self, delete_session):
        """ Тест попытки получения списка покупок без авторизационного токена """
        with allure.step('Запрос на получение списка покупок'):
            r = Rooms().get_purchases_by_san(san=DV.SAN_ROOM_WITH_PURCHASES)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
