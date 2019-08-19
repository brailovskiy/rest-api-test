from hamcrest import *
from api.devices import Devices
from shared.constants import DefaultValues as DV
import allure


class TestGetDevicesEmployee:
    """ Тесты категории devices, метод GET /device_slots, роль - сотрудник """
    def test_get_device_slots_by_employee(self, use_session_employee):
        """ Тест получения списка доступных слотов для привязки устройства сотрудником """
        with allure.step('Запрос на получение списка доступных слотов для привязки устройств'):
            r = Devices().get_device_slots_by_san(san=DV.SAN_MAIN_ROOM)

        with allure.step('Проверка на корректность статус кода'):
            assert_that(r.status_code, equal_to(200))

        # Проверка первого слота - STB (device_type 1)
        with allure.step('Проверка устройства первого слота - STB (device_type: 1)'):
            assert_that(
                r.json()["device_slots"][0],
                has_entries(
                    "id", equal_to(DV.FIRST_SLOT_ID),
                    "is_device_bound", is_(True),
                    "device_type", equal_to(DV.FIRST_SLOT_DEVICE_ID),
                    "device_id", equal_to(DV.FIRST_SLOT_MAC)
                )
            )

        # Проверка второго слота - Smart TV (device_type 2)
        with allure.step('Проверка устройства второго слота - Smart TV (device_type: 2)'):
            assert_that(
                r.json()["device_slots"][1],
                has_entries(
                    "id", equal_to(DV.SECOND_SLOT_ID),
                    "is_device_bound", is_(True),
                    "device_type", equal_to(DV.SECOND_SLOT_DEVICE_ID),
                    "device_id", equal_to(DV.SECOND_SLOT_MAC)
                )
            )

        # Проверка третьего слота - неизвестное устройство (device_type 0)
        with allure.step('Проверка устройства третьего слота - неизвестное устройство (device_type: 0)'):
            assert_that(
                r.json()["device_slots"][2],
                has_entries(
                    "id", equal_to(DV.THIRD_SLOT_ID),
                    "is_device_bound", is_(True),
                    "device_type", equal_to(DV.THIRD_SLOT_DEVICE_ID),
                    "device_id", equal_to(DV.THIRD_SLOT_MAC)
                )
            )

        # Проверка четвертого слота - свободный слот (device_type 0)
        with allure.step('Проверка четвертого слота - слот свободен (device_type: 0)'):
            assert_that(
                r.json()["device_slots"][3],
                has_entries(
                    "id", equal_to(DV.FOURTH_SLOT_ID),
                    "is_device_bound", is_(False),
                    "device_type", equal_to(DV.FOURTH_SLOT_DEVICE_ID),
                    "device_id", equal_to(DV.FOURTH_SLOT_MAC)
                )
            )

    def test_get_device_slots_in_another_hotel_by_employee(self, use_session_employee):
        """ Тест попытки получения списка доступных слотов для привязки устройства не в своей гостинице сотрудником """
        with allure.step('Запрос на получение списка доступных слотов для привязки устройств в комнате чужой гостиницы'):
            r = Devices().get_device_slots_by_san(san=DV.SECOND_SAN_MAIN_ROOM)

        # Проверки, что сотрудник не может получить просмотреть устройства в чужой гостинице
        with allure.step('Проверки, что сотруднику запрещен доступ к просмотру устройств в чужой гостинице'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(12))
            assert_that(r.json()["description"], equal_to("Action is forbidden for given room's san"))
