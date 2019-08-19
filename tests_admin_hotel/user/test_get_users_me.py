from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestGetUsersMeAdminHotel:
    """ Тесты категории User, метод GET /users/me, роль - администратор гостиницы """
    def test_get_user_me_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки получить информацию о собственном пользователе администратором гостиницы """
        with allure.step('Запрос на получение данных о собственном пользователе'):
            r = Users().get_users_me()

        with allure.step('Проверки, что администратор гостиницы может получить информацию о себе'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.ADMIN_HOTEL_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(1))
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert_that(r.json()["checkin_enabled"], is_(True))
