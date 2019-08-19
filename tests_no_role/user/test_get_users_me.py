from hamcrest import *
from api.users import Users
import allure


class TestGetUsersMeNoRole:
    """ Тесты категории User, метод GET /users/me, авторизационный токен отсутствует """
    def test_get_user_me_no_role(self, delete_session):
        """ Тест попытки получить информацию о собственном пользователе без авторизационного токена """
        with allure.step('Запрос на получение информации о собственном пользователе'):
            r = Users().get_users_me()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
