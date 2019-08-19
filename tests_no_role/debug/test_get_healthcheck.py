from hamcrest import *
from api.debug import Healthcheck
import allure


class TestGetHealthcheckNoRole:
    """ Тесты проверки статуса сервера, авторизационный токен отсутствует """
    def test_get_healthcheck_no_role(self, delete_session):
        """ Тест получения информации о сервере без авторизационного токена """
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
