from hamcrest import *
from api.settings import Settings
import allure


class TestGetSettingsAdminRt:
    """ Тесты категории Settings, метод GET /settings, роль - администратор Ростелеком """
    def test_get_rooms_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки получения настроек гостиницы """
        with allure.step('Запрос на получение настроек гостиницы'):
            r = Settings().get_settings()

        with allure.step('Проверки, что администратор Ростелеком не может получить настройки гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
