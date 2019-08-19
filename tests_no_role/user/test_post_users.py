from hamcrest import *
from api.users import Users
import allure


class TestPostUsersNoRole:
    """ Тесты категории User, метод POST /users, авторизационный токен отсутствует """
    def test_create_employee_no_role(self, delete_session):
        """ Тест попытки создания сотрудника без авторизационного токена """
        with allure.step('Запрос на создание сотрудника'):
            r = Users(role_id=0).post_user()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_create_admin_hotel_no_role(self, delete_session):
        """ Тест попытки создания администратора гостиницы без авторизационного токена """
        with allure.step('Запрос на создание администратора гостиницы'):
            r = Users(role_id=1).post_user()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_create_admin_rt_no_role(self, delete_session):
        """ Тест попытки создания администратора Ростелеком без авторизационного токена """
        with allure.step('Запрос на создание администратора Ростелеком'):
            r = Users(role_id=2).post_user()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
