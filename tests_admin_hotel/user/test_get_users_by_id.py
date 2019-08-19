from hamcrest import *
from shared.constants import UserAuthData as UAD
from shared.constants import DefaultValues as DV
from api.users import Users
import allure


class TestGetUsersByIdAdminHotel:
    """ Тесты категории User, метод GET /users/{id}, роль - администратор гостиницы """
    def test_get_employee_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест получения данных сотрудника администратором гостиницы """
        with allure.step('Запрос на получение данных сотрудника'):
            r = Users().get_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что администратор гостиницы может просмотреть информацию о сотруднике'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.EMPLOYEE_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(0))
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()

    def test_get_admin_hotel_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест получения данных администратора гостиницы администратором гостиницы """
        with allure.step('Запрос на получение данных администратора гостиницы'):
            r = Users().get_users_by_id(UAD.ADMIN_HOTEL_ID)

        with allure.step('Проверки, что администратор гостиницы может просмотреть информацию об администраторе '
                         'гостиницы'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.ADMIN_HOTEL_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(1))
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()

    def test_get_admin_rt_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки получить данные администратора Ростелеком администратором гостиницы """
        with allure.step('Запрос на получение данных администратора Ростелеком'):
            r = Users().get_users_by_id(UAD.ADMIN_MRF_ID)

        with allure.step('Проверки, что администратор гостиницы не может получить данные администратора Ростелеком'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_get_null_user_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки получить данные несуществующего пользователя администратором гостиницы """
        with allure.step('Запрос на получение данных несуществующего пользователя'):
            r = Users().get_users_by_id(None)

        with allure.step('Проверка на корректный ответ от сервера'):
            assert_that(r.status_code, equal_to(400))

    def test_get_employee_in_another_hotel_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки получить данные сотрудника не своей гостиницы администратором гостиницы """
        with allure.step('Запрос на получение данных сотрудника чужой гостиницы'):
            r = Users().get_users_by_id(UAD.SECOND_EMPLOYEE_ID)

        with allure.step('Проверки, что администратор гостиницы не может получить данные пользователей чужой гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
