from hamcrest import *
from shared.constants import DefaultValues as DV
from api.users import Users
import allure


class TestPostUsersEmployee:
    """ Тесты категории User, метод POST /users, роль - сотрудник """
    def test_create_employee_by_employee(self, use_session_employee):
        """ Тест попытки создания сотрудника сотрудником """
        with allure.step('Запрос на создание пользователя с ролью сотрудника'):
            r = Users(role_id=0).post_user()

        with allure.step('Проверки, что сотрудник не может создавать сотрудников'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_create_admin_hotel_by_employee(self, use_session_employee):
        """ Тест попытки создания администратора гостиницы сотрудником """
        with allure.step('Запрос на создание пользователя с ролью администратора гостиницы'):
            r = Users(role_id=1).post_user()

        with allure.step('Проверки, что сотрудник не может создавать администраторов гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_create_admin_rt_by_employee(self, use_session_employee):
        """ Тест попытки создания администратора Ростелеком сотрудником """
        with allure.step('Запрос на создание пользователя с ролью администратора Ростелеком'):
            r = Users(role_id=2).post_user()

        with allure.step('Проверки, что сотрудник не может создавать администраторов Ростелеком'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_create_user_to_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки создания пользователя в другой гостинице сотрудником """
        with allure.step('Запрос на создание пользователя с ролью администратора Ростелеком'):
            r = Users(client_id=DV.SECOND_HOTEL_ID).post_user()

        with allure.step('Проверки, что сотрудник не может создавать пользователей в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
