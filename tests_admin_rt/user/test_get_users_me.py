from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestGetUsersMeAdminMrf:
    """ Тесты категории User, метод GET /users/me, роль - администратор Ростелеком """
    def test_get_user_me_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки получить информацию о собственном пользователе """
        with allure.step('Запрос на получение данных о собственном пользователе'):
            r = Users().get_users_me()

        with allure.step('Проверки, что администратор Ростелекома может получить информацию о себе'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.ADMIN_MRF_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(2))
            assert_that(r.json()["client_id"], equal_to(""))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert_that(r.json()["checkin_enabled"], is_(False))
