from hamcrest import *
from api.users import Users
from shared.constants import UserAuthData as UAD
import allure


class TestDeleteUsersAdminHotel:
    """ Тесты категории User, метод DELETE /users/id, роль - администратор гостиницы """
    def test_delete_admin_hotel_by_admin_hotel(self, use_session_admin_hotel, create_user_admin_hotel, check_user):
        """ Тест удаления администратора гостиницы администратором гостиницы """
        with allure.step('Запрос на удаление администратора гостиницы'):
            r = Users().delete_users_by_id(create_user_admin_hotel)

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

        with allure.step('Проверка, что удаленный пользователь не существует (запрос пользователя по id)'):
            user_exists = check_user(create_user_admin_hotel)
            assert_that(user_exists, is_(False))

    def test_delete_employee_by_admin_hotel(self, use_session_admin_hotel, create_user_employee, check_user):
        """ Тест удаления сотрудника администратором гостиницы """
        with allure.step('Запрос на удаление администратора гостиницы'):
            r = Users().delete_users_by_id(create_user_employee)

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

        with allure.step('Проверка, что удаленный пользователь не существует (запрос пользователя по id)'):
            user_exists = check_user(create_user_employee)
            assert_that(user_exists, is_(False))

    def test_delete_admin_rt_by_admin_hotel(self, use_session_admin_hotel, check_user):
        """ Тест попытки удаления администратора Ростелеком администратором гостиницы """
        with allure.step('Запрос на удаление администратора Ростелеком'):
            r = Users().delete_users_by_id(UAD.ADMIN_MRF_ID)

        with allure.step('Проверка, что администратор гостиницы не может удалять администратора Ростелеком'):
            assert_that(r.status_code, equal_to(403))

        with allure.step('Проверка, что пользователь не удалился (запрос пользователя по id)'):
            user_exists = check_user(UAD.ADMIN_MRF_ID)
            assert_that(user_exists, is_(True))
