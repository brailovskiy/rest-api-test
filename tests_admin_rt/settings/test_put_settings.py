from hamcrest import *
from api.settings import Settings
import allure


class TestPutSettingsAdminRt:
    """ Тесты категории Settings, метод PUT /settings, роль - администратор Ростелеком """

    def test_change_settings_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки изменения настроек гостиницы """
        with allure.step('Задаем данные, на которые нужно изменить настройки'):
            day_change_time = "13:00:00"
            hello_message_EN = "english text hello_message"
            hello_message_RU = "russian text hello_message"
            memo_EN = "english text memo"
            memo_RU = "russian text memo"
            promo_on_startup_enabled = False

        with allure.step('Запрос на изменение настроек гостиницы'):
            r = Settings(day_change_time=day_change_time, hello_message_EN=hello_message_EN,
                         hello_message_RU=hello_message_RU, memo_EN=memo_EN, memo_RU=memo_RU,
                         promo_on_startup_enabled=promo_on_startup_enabled).put_settings()

        with allure.step('Запрос на изменение настроек гостиницы'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
