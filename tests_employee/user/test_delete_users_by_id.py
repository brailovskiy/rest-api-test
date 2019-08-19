from hamcrest import *
from api.users import Users
from shared.constants import UserAuthData as UAD
import allure


class TestDeleteUsersEmployee:
    """ Тесты категории User, метод DELETE /users/id, роль - сотрудник """
    def test_delete_admin_hotel_by_employee(self, create_user_admin_hotel, use_session_employee, check_user):
        """ Тест попытки удаления администратора гостиницы сотрудником """
        with allure.step('Запрос на удаление администратора гостиницы'):
            r = Users().delete_users_by_id(create_user_admin_hotel)

        with allure.step('Проверка, что сотрудник не может удалять администратора гостиницы'):
            assert_that(r.status_code, equal_to(403))

        with allure.step('Проверка, что пользователь не удалился (запрос пользователя по id)'):
            user_exists = check_user(create_user_admin_hotel)
            assert_that(user_exists, is_(True))

    def test_delete_employee_by_employee(self, create_user_employee, use_session_employee, check_user):
        """ Тест попытки удаления сотрудника сотрудником """
        with allure.step('Запрос на удаление сотрудника'):
            r = Users().delete_users_by_id(create_user_employee)

        with allure.step('Проверка, что сотрудник не может удалять сотрудника'):
            assert_that(r.status_code, equal_to(403))

        with allure.step('Проверка, что пользователь не удалился (запрос пользователя по id)'):
            user_exists = check_user(create_user_employee)
            assert_that(user_exists, is_(True))

    def test_delete_admin_rt_by_employee(self, use_session_employee, check_user):
        """ Тест попытки удаления администратора Ростелеком сотрудником """
        with allure.step('Запрос на удаление администратора Ростелеком'):
            r = Users().delete_users_by_id(UAD.ADMIN_MRF_ID)

        with allure.step('Проверка, что сотрудник не может удалять администратора Ростелеком'):
            assert_that(r.status_code, equal_to(403))

        with allure.step('Проверка, что пользователь не удалился (запрос пользователя по id)'):
            user_exists = check_user(UAD.ADMIN_MRF_ID)
            assert_that(user_exists, is_(True))
