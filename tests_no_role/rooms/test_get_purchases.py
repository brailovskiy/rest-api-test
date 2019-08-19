from hamcrest import *
from api.rooms import Rooms
import allure


class TestGetPurchasesNoRole:
    """ Тесты категории Rooms, метод GET /purchases, авторизационный токен отсутствует """
    def test_get_purchases_no_role(self, delete_session):
        """ Тест попытки получить список покупок всех гостей номера без авторизационного токена """
        with allure.step('Запрос на получение списка покупок всех гостей номера'):
            r = Rooms().get_purchases()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
