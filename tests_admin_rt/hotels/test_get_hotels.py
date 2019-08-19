from hamcrest import *
from api.hotels import Hotels
import allure


class TestGetHotelsAdminRt:
    """ Тесты категории Hotels, метод GET /hotels, роль - администратор Ростелеком """
    def test_get_hotels_by_admin_rt(self, use_session_admin_rt):
        """ Тест получения списка отелей """
        with allure.step('Запрос на получение списка отелей'):
            r = Hotels().get_hotels()

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что основной тестируемый отель присутствует в списке отелей данного МРФ'):
            assert {'id': 150612589, 'name': 'Клиент тест HTM API'} in r.json()

        with allure.step('Проверка, что отелей в списке несколько'):
            assert len(r.json()) > 1
