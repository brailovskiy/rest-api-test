from hamcrest import *
from shared.constants import UserAuthData as UAD
from api.users import Users
import allure


# Тест план:
# Вначале каждого теста необходим созданный пользователь с дефолтными параметрами
# Для этого нужно добавить фикстуру, возвращающую ID созданного пользователя с дефолтными параметрами
# После выполнения теста необходимо удалять пользователя (делается также в фикстуре)
# В тесте выполняем метод изменения и проверяем GET-запросом новые данные пользователя, сравнивая с переданными
# Необходимо проверить доступность выполнять данный метод всеми ролями для всех ролей

class TestPutUsersByIdEmployee:
    """ Тесты категории User, метод PUT /users/id, роль - сотрудник """
    def _test_change_employee_by_employee(self, use_session_employee):
        """ Тест попытки изменить данные сотрудника сотрудником """
        with allure.step('Запрос на изменение пользователя с ролью сотрудника'):
            r = Users(role_id=0).put_users_by_id(UAD.EMPLOYEE_ID)

        with allure.step('Проверки, что сотрудник не может изменять сотрудников'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(403))
            assert_that(r.json()["description"], equal_to("Forbidden"))
