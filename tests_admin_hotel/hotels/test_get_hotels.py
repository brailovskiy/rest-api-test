from hamcrest import *
from api.hotels import Hotels
import allure


class TestGetHotelsAdminHotel:
    """ Тесты списка отелей, роль - администратор гостиницы """
    def test_get_hotels_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки получения списка отелей администратором гостиницы """
        with allure.step('Запрос на получение списка отелей'):
            r = Hotels().get_hotels()

        with allure.step('Проверки, что администратор гостиницы не может просматривать список отелей'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to('Forbidden'))
