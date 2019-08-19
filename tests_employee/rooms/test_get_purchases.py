from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestGetPurchasesEmployee:
    """ Тесты категории Rooms, метод GET /purchases, роль - сотрудник """
    def test_get_purchases_by_employee(self, use_session_employee):
        """ Тест получения списка покупок всех гостей номера сотрудником """
        with allure.step('Запрос на получение списка покупок всех гостей номера'):
            r = Rooms().get_purchases()

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что список покупок не пустой'):
            assert_that(r.json(), is_not([]))

    def test_get_purchases_by_room_id_by_employee(self, use_session_employee):
        """ Тест получения списка покупок в номере с покупками сотрудником """
        with allure.step('Запрос на получение списка покупок в определенном номере'):
            r = Rooms().get_purchases(san=DV.SAN_ROOM_WITH_PURCHASES)

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверки информации о комнате'):
            assert_that(r.json()[0]["service_account_number"], equal_to(DV.SAN_ROOM_WITH_PURCHASES))
            assert_that(
                r.json()[0],
                has_entries(
                    "service_account_number", equal_to(DV.SAN_ROOM_WITH_PURCHASES),
                    "purchases", is_not([])
                )
            )

        with allure.step('Проверки списка покупок'):
            assert_that(
                r.json()[0]["purchases"][0],
                has_entries(
                    "name", equal_to("Сахара")))
            assert_that(
                r.json()[0]["purchases"][1],
                has_entries(
                    "name", equal_to("Карлик Нос")))
            assert_that(
                r.json()[0]["purchases"][2],
                has_entries(
                    "name", equal_to("Взрослый Деловой")))

    def test_get_purchases_by_room_id_in_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки получения списка покупок в номере чужого отеля сотрудником """
        with allure.step('Запрос на получение списка покупок в номере чужой гостиницы'):
            r = Rooms().get_purchases(san=DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки, что сотруднику запрещен доступ к просмотру списка покупок в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_get_purchases_by_incorrect_room_id_by_employee(self, use_session_employee):
        """ Тест попытки получения списка покупок в несуществующем номере сотрудником """
        with allure.step('Запрос на получение списка покупок в несуществующем номере'):
            r = Rooms().get_purchases(san="incorrect")

        with allure.step('Проверки на корректный ответ от сервера'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
