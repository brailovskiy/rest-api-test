from hamcrest import *
from api.rooms import Rooms
import allure


class TestPutUsersByIdNoRole:
    """ Тесты категории Rooms, метод POST /rooms/notify, авторизационный токен отсутствует """
    def test_post_notify_no_role(self, delete_session):
        """ Тест отправки нотификации в несколько номеров без авторизационного токена """
        with allure.step('Запрос на отправку нотификации во все номера гостиницы'):
            r = Rooms().post_notify_to_all_rooms()

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))
