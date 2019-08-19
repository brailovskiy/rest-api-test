from hamcrest import *
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestPutUsersByIdNoRole:
    """ Тесты категории User, метод PUT /users/{id}, авторизационный токен отсутствует """
    def test_put_employee_no_role(self, delete_session):
        """ Тест попытки изменить данные сотрудника без авторизационного токена """
        with allure.step('Запрос на изменение сотрудника'):
            r = Users().put_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_put_admin_hotel_no_role(self, delete_session):
        """ Тест попытки изменить данные администратора гостиницы без авторизационного токена """
        with allure.step('Запрос на изменение администратора гостиницы'):
            r = Users().put_users_by_id(UAD.ADMIN_HOTEL_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_put_admin_rt_no_role(self, delete_session):
        """ Тест попытки изменить данные администратора Ростелеком без авторизационного токена """
        with allure.step('Запрос на изменение администратора Ростелеком'):
            r = Users().put_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
