from hamcrest import *
from api.hotels import Hotels
import allure


class TestGetHotelsEmployee:
    """ Тесты категории Hotels, метод GET /hotels, роль - сотрудник """
    def test_get_hotels_by_employee(self, use_session_employee):
        """ Тест попытки получения списка отелей сотрудником """
        with allure.step('Запрос на получение списка отелей'):
            r = Hotels().get_hotels()

        with allure.step('Проверки, что сотруднику запрещен доступ к просмотру списка всех гостиниц'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to('Forbidden'))
