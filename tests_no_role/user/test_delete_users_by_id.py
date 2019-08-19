from hamcrest import *
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestDeleteUsersByIdNoRole:
    """ Тесты категории User, метод DELETE /users, авторизационный токен отсутствует """
    def test_delete_employee_no_role(self, delete_session):
        """ Тест попытки удалить сотрудника без авторизационного токена """
        with allure.step('Запрос на удаление сотрудника'):
            r = Users().delete_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_delete_admin_hotel_no_role(self, delete_session):
        """ Тест попытки удалить администратора гостиницы без авторизационного токена """
        with allure.step('Запрос на удаление администратора гостиницы'):
            r = Users().delete_users_by_id(UAD.ADMIN_HOTEL_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_delete_admin_rt_no_role(self, delete_session):
        """ Тест попытки удалить администратора Ростелеком без авторизационного токена """
        with allure.step('Запрос на удаление администратора Ростелеком'):
            r = Users().delete_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
