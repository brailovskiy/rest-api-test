from hamcrest import *
from api.debug import Healthcheck
import allure


class TestGetHealthcheckEmployee:
    """ Тесты проверки статуса сервера сотрудником """
    def test_get_healthcheck_by_employee(self, use_session_employee):
        """ Тест получения информации о сервере сотрудником """
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
