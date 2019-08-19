from hamcrest import *
from api.users import Users
import allure


class TestGetUsersEmployee:
    """ Тесты категории User, метод GET /users, роль - сотрудник """
    def test_create_user_by_employee(self, use_session_employee):
        """ Тест попытки получить список пользователей сотрудником """
        with allure.step('Запрос на получение списка пользователей'):
            r = Users().get_users()

        with allure.step('Проверки, что сотрудник не может получить список пользователей'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
