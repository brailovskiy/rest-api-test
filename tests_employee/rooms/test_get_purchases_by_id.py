from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestGetPurchasesByIdEmployee:
    """ Тесты категории Rooms, метод GET /id/purchases, роль - сотрудник """
    def test_get_purchases_by_id_by_employee(self, use_session_employee):
        """ Тест получения списка покупок в номере с покупками сотрудником """
        with allure.step('Запрос на получение списка покупок в номере по его SAN'):
            r = Rooms().get_purchases_by_san(san=DV.SAN_ROOM_WITH_PURCHASES)

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверки информации о комнате'):
            assert_that(r.json()["service_account_number"], equal_to(DV.SAN_ROOM_WITH_PURCHASES))
            assert_that(
                r.json(),
                has_entries(
                    "service_account_number", equal_to(DV.SAN_ROOM_WITH_PURCHASES),
                    "purchases", is_not([])
                )
            )

        with allure.step('Проверки списка покупок'):
            assert_that(
                r.json()["purchases"][0],
                has_entries(
                    "name", equal_to("Сахара")))
            assert_that(
                r.json()["purchases"][1],
                has_entries(
                    "name", equal_to("Карлик Нос")))
            assert_that(
                r.json()["purchases"][2],
                has_entries(
                    "name", equal_to("Взрослый Деловой")))

    def test_get_purchases_by_id_in_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки получения списка покупок в номере чужого отеля сотрудником """
        with allure.step('Запрос на получение списка покупок в номере чужого отеля по его SAN'):
            r = Rooms().get_purchases_by_san(san=DV.SECOND_SAN_MAIN_ROOM)

        with allure.step('Проверки, что сотруднику запрещен доступ к просмотру списка покупок в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))

    def test_get_purchases_by_incorrect_id_by_employee(self, use_session_employee):
        """ Тест попытки получения списка покупок в несуществующем номере сотрудником """
        with allure.step('Запрос на получение списка покупок в номере чужого отеля по его SAN'):
            r = Rooms().get_purchases_by_san(san="incorrect")

        with allure.step('Проверки, что сотруднику запрещен доступ к просмотру списка покупок в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
