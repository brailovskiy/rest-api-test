from hamcrest import *
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestGetUsersByIdEmployee:
    """
        Тесты категории User, метод GET /users/{id}, роль - сотрудник
        Проверки, что сотрудник не имеет права просматривать никакого пользователя, даже себя
    """
    def test_get_employee_by_employee(self, use_session_employee):
        """ Тест попытки получить данные сотрудника сотрудником """
        with allure.step('Запрос на получение данных сотрудника'):
            r = Users().get_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что сотрудник не может просмотреть данные сотрудника'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_get_admin_hotel_by_employee(self, use_session_employee):
        """ Тест попытки получить данные администратора гостиницы сотрудником """
        with allure.step('Запрос на получение данных администратора гостиницы'):
            r = Users().get_users_by_id(UAD.ADMIN_HOTEL_ID)

        with allure.step('Проверки, что сотрудник не может просмотреть данные администратора гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_get_admin_rt_by_employee(self, use_session_employee):
        """ Тест попытки получить данные администратора Ростелеком сотрудником """
        with allure.step('Запрос на получение данных администратора Ростелеком'):
            r = Users().get_users_by_id(UAD.ADMIN_MRF_ID)

        with allure.step('Проверки, что сотрудник не может просмотреть данные администратора Ростелеком'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_get_null_user_by_employee(self, use_session_employee):
        """ Тест попытки получить данные несуществующего пользователя сотрудником """
        with allure.step('Запрос на получение данных пользователя с несуществующим ID'):
            r = Users().get_users_by_id(None)

        with allure.step('Проверки на корректный ответ от сервера'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_get_employee_in_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки получить данные сотрудника не своей гостиницы сотрудиком """
        with allure.step('Запрос на получение данных пользователя сотрудника чужой гостиницы'):
            r = Users().get_users_by_id(UAD.SECOND_EMPLOYEE_ID)

        with allure.step('Проверки, что сотрудник не может просмотреть данные пользователя чужой гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
