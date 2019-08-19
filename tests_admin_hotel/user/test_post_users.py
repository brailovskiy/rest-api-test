from hamcrest import *
from shared.constants import DefaultValues as DV
from api.users import Users
import time
import allure


class TestPostUsersAdminHotel:
    """ Тесты категории User, метод POST /users, роль - администратор гостиницы """
    def test_create_employee_by_admin_hotel(self, use_session_admin_hotel, check_user):
        """ Тест создания сотрудника администратором гостиницы """
        with allure.step('Запрос на создание сотрудника'):
            r = Users(role_id=0).post_user()

        with allure.step('Проверки, что администратор гостиницы может создавать сотрудника'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], greater_than(0))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(0))
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()

        with allure.step('Проверка, что пользователь создан (запрос пользователя по id)'):
            user_id = r.json()["id"]
            user_exists = check_user(user_id)
            assert_that(user_exists, is_(True))
            time.sleep(1)

        with allure.step('Удаление созданного пользователя, чтобы не засорять БД'):
            Users().delete_users_by_id(user_id)

    def test_create_admin_hotel_by_admin_hotel(self, use_session_admin_hotel, check_user):
        """ Тест создания администратора гостиницы администратором гостиницы """
        with allure.step('Запрос на создание администратора гостиницы'):
            r = Users(role_id=1).post_user()

        with allure.step('Проверки, что администратор гостиницы может создавать администратора гостиницы'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], greater_than(0))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(1), r.text)
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert "checkin_enabled" not in r.json()

        with allure.step('Проверка, что пользователь создан (запрос пользователя по id)'):
            user_id = r.json()["id"]
            user_exists = check_user(user_id)
            assert_that(user_exists, is_(True))
            time.sleep(1)

        with allure.step('Удаление созданного пользователя, чтобы не засорять БД'):
            Users().delete_users_by_id(user_id)

    def test_create_admin_mrf_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки создания администратора МРФ администратором гостиницы """
        with allure.step('Запрос на создание администратора Ростелеком'):
            r = Users(role_id=2).post_user()

        with allure.step('Проверки, что администратор гостиницы не может создавать другого администратора Ростелеком'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))

    def test_create_user_to_another_hotel_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки создания пользователя в другой гостинице администратором гостиницы """
        with allure.step('Запрос на создание пользователя в чужой гостинице'):
            r = Users(client_id=DV.SECOND_HOTEL_ID).post_user()

        with allure.step('Проверки, что администратор гостиницы не может создавать пользователей в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
