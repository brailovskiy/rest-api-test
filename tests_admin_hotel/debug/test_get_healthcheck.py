from hamcrest import *
from api.debug import Healthcheck
import allure


class TestGetHealthcheckAdminHotel:
    """ Тесты проверки статуса сервера администратором гостиницы """
    def test_get_healthcheck_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест получения информации о сервере администратором гостиницы """
        with allure.step('Запрос на получение информации о сервере'):
            r = Healthcheck().get_healthcheck()

        with allure.step('Проверка на корректность статус кода'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка статуса приложения'):
            assert_that(
                r.json()["app"],
                has_entries("status", is_(True),
                            "error", equal_to("")))

        with allure.step('Проверка статуса nsq'):
            assert_that(
                r.json()["nsq"],
                has_entries("status", is_(True),
                            "error", equal_to("")))

        with allure.step('Проверка статуса базы данных'):
            assert_that(
                r.json()["db"],
                has_entries("status", is_(True),
                            "error", equal_to("")))

        with allure.step('Проверка статуса redis'):
            assert_that(
                r.json()["redis"],
                has_entries("status", is_(True),
                            "error", equal_to("")))
