from hamcrest import *
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestGetUsersByIdNoRole:
    """ Тесты категории User, метод GET /users/{id}, авторизационный токен отсутствует """
    def test_get_employee_no_role(self, delete_session):
        """ Тест попытки получить данные сотрудника без авторизационного токена """
        with allure.step('Запрос на получение данных сотрудника'):
            r = Users().get_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_get_admin_hotel_no_role(self, delete_session):
        """ Тест попытки получить данные администратора гостиницы без авторизационного токена """
        with allure.step('Запрос на получение данных администратора гостиницы'):
            r = Users().get_users_by_id(UAD.ADMIN_HOTEL_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_get_admin_rt_no_role(self, delete_session):
        """ Тест попытки получить данные администратора Ростелеком без авторизационного токена """
        with allure.step('Запрос на получение данных администратора Ростелеком'):
            r = Users().get_users_by_id(UAD.ADMIN_MRF_ID)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
