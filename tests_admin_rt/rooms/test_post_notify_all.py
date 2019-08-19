from hamcrest import *
from api.rooms import Rooms
import allure


class TestPutUsersByIdAdminRt:
    """ Тесты категории Rooms, метод POST /rooms/notify_all, роль - администратор Ростелеком """
    def test_post_notify_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки отправки нотификации во все номера гостиницы """
        with allure.step('Запрос на отправку нотификаций'):
            r = Rooms().post_notify_to_all_rooms()

        with allure.step('Проверки, что администратор Ростелеком не может отправить нотификации'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
