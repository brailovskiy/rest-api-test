from hamcrest import *
from api.sessions import Sessions
from shared.constants import UserAuthData
import time
import allure


class TestPostSessions:
    """ Тесты категории Sessions, метод GET /sessions """
    def test_get_new_session_admin_rt(self, delete_session):
        """ Получение новой сессии администратора Ростелеком """
        with allure.step('Пауза, чтобы избежать превышения лимита запросов'):
            time.sleep(2)

        with allure.step('Запрос на получение новой сессии администратора Ростелеком'):
            r = Sessions(email=UserAuthData.ADMIN_MRF['email'],
                         password=UserAuthData.ADMIN_MRF['password']).get_new_session()

        with allure.step('Проверка на успешный ответ от сервера и наличие токена в ответе'):
            assert_that(r.status_code, equal_to(200))
            assert 'session_id' in r.json()

        with allure.step('Удаляем сессию после прохождения теста, чтобы не засорять БД'):
            session_id = r.json()['session_id']
            Sessions().delete_session_by_id(session_id)

    def test_get_new_session_admin_hotel(self, delete_session):
        """ Получение новой сессии администратора гостиницы """
        with allure.step('Пауза, чтобы избежать превышения лимита запросов'):
            time.sleep(2)

        with allure.step('Запрос на получение новой сессии администратора гостиницы'):
            r = Sessions(email=UserAuthData.ADMIN_HOTEL['email'],
                         password=UserAuthData.ADMIN_HOTEL['password']).get_new_session()

        with allure.step('Проверка на успешный ответ от сервера и наличие токена в ответе'):
            assert_that(r.status_code, equal_to(200))
            assert 'session_id' in r.json()

        with allure.step('Удаляем сессию после прохождения теста, чтобы не засорять БД'):
            session_id = r.json()['session_id']
            Sessions().delete_session_by_id(session_id)

    def test_get_new_session_employee(self, delete_session):
        """ Получение новой сессии пользователя """
        with allure.step('Пауза, чтобы избежать превышения лимита запросов'):
            time.sleep(2)

        with allure.step('Запрос на получение новой сессии сотрудника'):
            r = Sessions(email=UserAuthData.EMPLOYEE['email'],
                         password=UserAuthData.EMPLOYEE['password']).get_new_session()

        with allure.step('Проверка на успешный ответ от сервера и наличие токена в ответе'):
            assert_that(r.status_code, equal_to(200))
            assert 'session_id' in r.json()

        with allure.step('Удаляем сессию после прохождения теста, чтобы не засорять БД'):
            session_id = r.json()['session_id']
            Sessions().delete_session_by_id(session_id)

    def test_get_new_session_fail(self, delete_session):
        """ Попытка получения новой сессии с некорректными авторизационными данными """
        with allure.step('Пауза, чтобы избежать превышения лимита запросов'):
            time.sleep(2)
            incorrect_auth_data = {
                "email": "",
                "password": ""
            }

        with allure.step('Запрос на получение новой сессии с невалидными логином и паролем'):
            r = Sessions(email=incorrect_auth_data['email'],
                         password=incorrect_auth_data['password']).get_new_session()

        with allure.step('Проверка на корректный ответ от сервера, что неверные логин или пароль'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(7))
            assert_that(r.json()["description"], string_contains_in_order('Invalid email or password'))
