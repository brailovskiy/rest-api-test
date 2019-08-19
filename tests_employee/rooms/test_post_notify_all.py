from hamcrest import *
from api.rooms import Rooms
import allure


class TestPutUsersByIdEmployee:
    """ Тесты категории Rooms, метод POST /rooms/notify_all, роль - сотрудник """
    def test_post_notify_by_employee(self, use_session_employee):
        """ Тест отправки нотификации во все номера гостиницы сотрудником """
        with allure.step('Запрос на отправку нотификации во все номера гостиницы'):
            r = Rooms().post_notify_to_all_rooms()

        with allure.step('Проверки на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

    def test_post_notify_with_incorrect_display_type_by_employee(self, use_session_employee):
        """ Тест отправки нотификации с некорректным параметром display_type сотрудником """
        with allure.step('Запрос на отправку нотификации во все номера гостиницы с некорректным значением параметра '
                         'display_type'):
            r = Rooms(display_type="incorrect_display_type").post_notify_to_all_rooms()

        with allure.step('Проверки на корректный ответ от сервера (неверные параметры запроса)'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(1003))
            assert_that(r.json()["description"], equal_to("Invalid form's parameters"))
