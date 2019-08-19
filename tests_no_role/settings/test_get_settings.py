from hamcrest import *
from api.settings import Settings
import allure


class TestGetSettingsNoRole:
    """ Тесты категории Settings, метод GET /settings авторизационный токен отсутствует """
    def test_get_settings_no_role(self, delete_session):
        """ Тест попытки получения настроек гостиницы без авторизационного токена """
        with allure.step('Запрос на получение настроек гостиницы'):
            r = Settings().get_settings()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
