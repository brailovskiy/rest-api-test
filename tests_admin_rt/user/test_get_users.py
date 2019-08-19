from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestGetUsersAdminRt:
    """ Тесты категории User, метод GET /users, роль - администратор Ростелеком """
    def test_create_user_by_admin_rt(self, use_session_admin_rt):
        """ Тест получения списка пользователей """
        with allure.step('Запрос на получение списка пользователей'):
            r = Users().get_users()

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что администратор МРФ видит более 2 пользователей'):
            assert len(r.json()) > 2

        with allure.step('Проверка, что администратор МРФ видит собственного пользователя'):
            admin_is = False
            for user in r.json():
                if user['role_id'] == 2:
                    admin_is = True

                    # Проверка, что данные администратора МРФ соответствуют действительным
                    assert_that(user['id'], equal_to(UAD.ADMIN_MRF_ID))
                    assert_that(user['mrf'], equal_to(DV.ACTUAL_MRF))
                    assert_that(user['client_id'], equal_to(""))
                    assert_that(user['name'], is_not(""))
                    assert_that(user['email'], is_not(""))
                    assert "checkin_enabled" not in r.json()[0]

            assert_that(admin_is, is_(True))
