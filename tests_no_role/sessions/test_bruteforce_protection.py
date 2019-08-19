from hamcrest import *
from api.sessions import Sessions
import time
import allure


class TestBruteforceProtection:
    """ Тесты защиты от подбора паролей """
    def test_bruteforce_protection(self, delete_session):
        """ Тест защиты от брутфорса """
        with allure.step('Пауза, чтобы избежать превышения лимита запросов'):
            time.sleep(2)
            incorrect_auth_data = {
                "email": "",
                "password": ""
            }

        with allure.step('Делаем последовательно {count} запросов на авторизацию'):
            count = 4
            i = 0
            while i < count:
                r = Sessions(email=incorrect_auth_data['email'],
                             password=incorrect_auth_data['password']).get_new_session()
                i += 1

                if i == count:
                    # На последней итерации проверяем защиту от брутфорса
                    assert_that(r.status_code, equal_to(429), ("Protection. Incorrect status code on " + str(i) + " attempt"))
                    assert_that(r.json()["error_code"], equal_to(429))
                    assert_that(r.json()["description"], equal_to('Too many requests'))
                else:
                    # Проверяем, что запросы до {count} проходят корректно
                    assert_that(r.status_code, equal_to(400), ("Normal auth before protection. Incorrect status code on " + str(i) + " attempt"))
                    assert_that(r.json()["error_code"], equal_to(7))
                    assert_that(r.json()["description"], string_contains_in_order('Invalid email or password'))

        with allure.step('Ждем 2 секунды и проверяем, что дальнейшая авторизация работает в штатном режиме'):
            time.sleep(2)
            r = Sessions(email=incorrect_auth_data['email'],
                         password=incorrect_auth_data['password']).get_new_session()
            assert_that(r.status_code, equal_to(400), ("Normal auth after protection. Incorrect status code on " + str(i) + " attempt"))
            assert_that(r.json()["error_code"], equal_to(7))
            assert_that(r.json()["description"], string_contains_in_order('Invalid email or password'))
