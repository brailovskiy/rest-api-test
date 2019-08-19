from hamcrest import *
from api.debug import Healthcheck
import allure


class TestGetHealthcheckAdminRt:
    """ Тесты категории debug, метод GET /healthcheck, роль - администратор Ростелеком """
    def test_get_healthcheck_by_admin_rt(self, use_session_admin_rt):
        """ Тест получения информации о сервере """
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
