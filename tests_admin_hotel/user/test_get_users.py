from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestGetUsersAdminHotel:
    """ Тесты категории User, метод GET /users, роль - администратор гостиницы """
    def test_get_users_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест получения списка пользователей администратором гостиницы """
        with allure.step('Запрос на получение списка пользователей'):
            r = Users().get_users()

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что администратор гостиницы видит более 1 пользователя'):
            assert len(r.json()) > 1

        with allure.step('Проверка, что администратор гостиницы видит собственного пользователя'):
            admin_is = False
            for user in r.json():
                if user['id'] == UAD.ADMIN_HOTEL_ID:
                    admin_is = True

                    # Проверка, что данные администратора гостиницы соответствуют действительным
                    assert_that(user['id'], equal_to(UAD.ADMIN_HOTEL_ID))
                    assert_that(user['mrf'], equal_to(DV.ACTUAL_MRF))
                    assert_that(user['client_id'], equal_to(DV.MAIN_HOTEL_ID))
                    assert_that(user['name'], is_not(""))
                    assert_that(user['email'], is_not(""))
                    assert "checkin_enabled" not in r.json()[0]

            assert_that(admin_is, is_(True))
