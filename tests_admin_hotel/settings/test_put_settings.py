import pytest
from hamcrest import *
from api.settings import Settings
import allure


# Методы данной категории работают некорректно!
# Необходимо дополнить тесты после починки


class TestPutSettingsAdminHotel:
    """ Тесты категории Settings, метод PUT /settings, роль - администратор гостиницы """

    def _test_change_settings_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест изменения настроек администратором гостиницы """
        # Задаем данные, на которые нужно изменить настройки
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

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

        with allure.step('Получаем список настроек в HTM'):
            r = Settings().get_settings()

        with allure.step('Проверяем, что изменения применились'):
            assert_that(r.json()["day_change_time"], equal_to(day_change_time))
            assert_that(
                r.json()["memo"],
                has_entries("EN", equal_to(memo_EN)))
            assert_that(
                r.json()["hello_message"],
                has_entries("EN", equal_to(hello_message_EN)))
            assert_that(r.json()["promo_on_startup_enabled"], is_(False))

        # Внимание!!! В SDP заведен баг (не меняется русские memo и hello_message
        # После исправления бага необходимо дополнить assert'ы


@pytest.fixture(scope="function")
def default_hotel_settings():
    """ Фикстура для задания дефолтных значений настроек гостиницы """
    # Методом SDP присвоить дефолтные значения гостинице до теста

    yield

    # После теста также установить дефолтные значения
