from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestPutUsersByIdAdminRt:
    """ Тесты категории Rooms, метод POST /rooms/notify, роль - администратор Ростелеком """
    def test_post_notify_by_admin_rt(self, use_session_admin_rt):
        """ Тест попытки отправки нотификации в номер """
        with allure.step('Запрос на отправку нотификаций'):
            r = Rooms().post_notify_to_select_rooms(DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что администратор Ростелеком не может отправлять нотификации'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
