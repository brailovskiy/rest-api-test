from hamcrest import *
from api.users import Users
import allure


class TestGetUsersNoRole:
    """ Тесты категории User, метод GET /users, авторизационный токен отсутствует """
    def test_create_user_no_role(self, delete_session):
        """ Тест попытки получить список пользователей без авторизационного токена """
        with allure.step('Запрос на получение списка пользователей'):
            r = Users().get_users()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
