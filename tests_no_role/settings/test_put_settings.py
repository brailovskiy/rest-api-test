from hamcrest import *
from api.settings import Settings
import allure


class TestPutSettingsNoRole:
    """ Тесты категории Settings, метод PUT /settings авторизационный токен отсутствует """

    def test_change_settings_no_role(self, delete_session):
        """ Тест попытки изменения настроек гостиницы без авторизационного токена """
        # Задаем данные, на которые нужно изменить настройки
        day_change_time = "13:00:00"
        hello_message_EN = "english text hello_message"
        hello_message_RU = "russian text hello_message"
        memo_EN = "english text memo"
        memo_RU = "russian text memo"
        promo_on_startup_enabled = False

        with allure.step('Запрос на изменение настроек'):
            r = Settings(day_change_time=day_change_time, hello_message_EN=hello_message_EN,
                         hello_message_RU=hello_message_RU, memo_EN=memo_EN, memo_RU=memo_RU,
                         promo_on_startup_enabled=promo_on_startup_enabled).put_settings()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
