import pytest
from hamcrest import *
from api.settings import Settings
import allure
# Методы данной категории работают некорректно!
# Необходимо дополнить тесты после починки


class TestGetSettingsAdminHotel:
    """ Тесты категории Settings, метод GET /settings, роль - администратор гостиницы """
    def _test_get_rooms_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест получения настроек гостиницы администратором гостиницы """
        with allure.step('Запрос на получение настроек гостиницы'):
            r = Settings().get_settings()

        with allure.step('Проверки: успешный ответ от сервера, текст памятки и приветственного сообщения на разных'
                         'языках в ответе'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["day_change_time"], equal_to("13:00:00"))
            assert_that(
                r.json()["memo"],
                has_entries("EN", equal_to("english text memo"),
                            "RU", string_contains_in_order("Как включить приставку")))
            assert_that(
                r.json()["hello_message"],
                has_entries("EN", equal_to("english text hello_message"),
                            "RU", equal_to("Guest")))
            assert_that(r.json()["promo_on_startup_enabled"], is_(False))


@pytest.fixture(scope="function")
def default_hotel_settings():
    """ Фикстура для задания дефолтных значений настроек гостиницы """
    # Методом SDP присвоить дефолтные значения гостинице до теста

    yield

    # После теста также установить дефолтные значения
