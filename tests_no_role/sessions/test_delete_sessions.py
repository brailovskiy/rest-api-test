from hamcrest import *
from api.sessions import Sessions
from shared.constants import UserAuthData
import time
import allure


class TestDeleteSessions:
    """ Тесты категории Sessions, метод DELETE /sessions """
    def test_delete_session(self, delete_session):
        """ Успешное удаление сессии """
        with allure.step('Пауза, чтобы избежать превышения лимита запросов'):
            time.sleep(2)

        with allure.step('Получаем новую сессию'):
            r = Sessions(email=UserAuthData.ADMIN_HOTEL['email'],
                         password=UserAuthData.ADMIN_HOTEL['password']).get_new_session()
            session_id = r.json()['session_id']

        with allure.step('Запрос на удаление сессии'):
            r = Sessions().delete_session_by_id(session_id)

        with allure.step('Проверка на успешный ответ от сервера'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

    def test_delete_session_fail(self):
        """ Попытка удаления сессии без токена """
        with allure.step('Запрос на удаление сессии без токена'):
            r = Sessions().delete_session_by_id(None)

        with allure.step('Проверки, что без авторизационного токена нельзя выполнить данный метод'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(1))
            assert_that(r.json()["description"], equal_to("No 'session_id' header was provided"))

    def test_delete_session_without_token(self):
        """ Попытка удаления сессии с неверным токеном """
        with allure.step('Запрос на удаление сессии с несуществующим токеном'):
            r = Sessions().delete_session_by_id("incorrect_token")

        with allure.step('Проверки на корректный ответ от сервера, что токен не найден'):
            assert_that(r.status_code, equal_to(401))
            assert_that(r.json()["error_code"], equal_to(3))
            assert_that(r.json()["description"], equal_to("Session token was not found"))
