from hamcrest import *
from shared.constants import UserAuthData as UAD
from shared.constants import DefaultValues as DV
from api.users import Users
import allure


class TestGetUsersByIdAdminRt:
    """ Тесты категории User, метод GET /users/{id}, роль - администратор МРФ """
    def test_get_employee_by_admin_rt(self, use_session_admin_rt):
        """ Тест получения данных сотрудника """
        with allure.step('Запрос на получение данных сотрудника'):
            r = Users().get_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что администратор Ростелеком может просмотреть информацию о сотруднике'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.EMPLOYEE_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(0))
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()

    def test_get_admin_hotel_by_admin_rt(self, use_session_admin_rt):
        """ Тест получения данных администратора гостиницы """
        with allure.step('Запрос на получение данных администратора гостиницы'):
            r = Users().get_users_by_id(UAD.ADMIN_HOTEL_ID)

        with allure.step('Проверки, что администратор Ростелеком может просмотреть информацию об администраторе '
                         'гостиницы'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.ADMIN_HOTEL_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(1))
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()

    def test_get_admin_mrf_by_admin_rt(self, use_session_admin_rt):
        """ Тест получения данных администратора Ростелеком администратором Ростелеком """
        with allure.step('Запрос на получение данных администратора Ростелеком'):
            r = Users().get_users_by_id(UAD.ADMIN_MRF_ID)

        with allure.step('Проверки, что администратор Ростелеком может просмотреть информацию об администраторе '
                         'Ростелеком'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.ADMIN_MRF_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(2))
            assert_that(r.json()["client_id"], equal_to(""))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()

    def test_get_null_user_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки получить данные несуществующего пользователя """
        with allure.step('Запрос на получение данных несуществующего пользователя'):
            r = Users().get_users_by_id(None)

        with allure.step('Проверка на корректный ответ от сервера'):
            assert_that(r.status_code, equal_to(400))

    def test_get_employee_in_another_hotel_by_admin_rt(self, use_session_admin_rt):
        """ Тест получения данных сотрудника другой гостиницы администратором Ростелеком """
        with allure.step('Запрос на получение данных сотрудника другой гостиницы'):
            r = Users().get_users_by_id(UAD.SECOND_EMPLOYEE_ID)

        with allure.step('Проверки, что администратор Ростелеком может посмотреть информацию пользователях любой '
                         'гостиницы своего МРФ'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.SECOND_EMPLOYEE_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(0))
            assert_that(r.json()["client_id"], equal_to(DV.SECOND_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()
