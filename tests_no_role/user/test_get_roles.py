from hamcrest import *
from api.users import Users
import allure


class TestGetRolesNoRole:
    """ Тесты категории User, метод GET /roles, авторизационный токен отсутствует """
    def test_get_roles_no_role(self, delete_session):
        """ Тест метода просмотра всех ролей, без авторизационного токена """
        with allure.step('Запрос на просмотр всех ролей'):
            r = Users().get_roles()

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что ролей - три'):
            assert_that(r.json(), has_length(3))

        with allure.step('Проверка, что без авторизационного токена можно увидеть все три роли'):
            assert_that(
                r.json()[0],
                has_entries("id", equal_to(0),
                            "name", equal_to("Сотрудник")))
            assert_that(
                r.json()[1],
                has_entries("id", equal_to(1),
                            "name", equal_to("Администратор гостиницы")))
            assert_that(
                r.json()[2],
                has_entries("id", equal_to(2),
                            "name", equal_to("Администратор Ростелеком")))
