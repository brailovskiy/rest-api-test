from hamcrest import *
from api.hotels import Hotels
import allure


class TestGetHotelsNoRole:
    """ Тесты категории Hotels, метод GET /hotels, авторизационный токен отсутствует """
    def test_get_hotels_no_role(self, delete_session):
        """ Тест попытки получения списка отелей без авторизационного токена """
        with allure.step('Запрос на получение списка отелей'):
            r = Hotels().get_hotels()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
