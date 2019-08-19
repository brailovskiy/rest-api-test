from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


class TestGetUsersMeEmployee:
    """ Тесты категории User, метод GET /users/me, роль - сотрудник """
    def test_get_user_me_by_employee(self, use_session_employee):
        """ Тест получения информацию о собственном пользователе сотрудником """
        with allure.step('Запрос на получение информации о собственном пользователе'):
            r = Users().get_users_me()

        with allure.step('Проверка на успешный ответ от сервера и верные данные своего пользователя в теле ответа'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["id"], equal_to(UAD.EMPLOYEE_ID))
            assert_that(r.json()["mrf"], equal_to(DV.ACTUAL_MRF))
            assert_that(r.json()["role_id"], equal_to(0))
            assert_that(r.json()["client_id"], equal_to(DV.MAIN_HOTEL_ID))
            assert_that(r.json()["name"], is_not(""))
            assert_that(r.json()["email"], is_not(""))
            assert_that(r.json()["checkin_enabled"], is_(True))
