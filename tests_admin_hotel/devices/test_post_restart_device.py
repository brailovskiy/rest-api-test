from hamcrest import *
from api.devices import Devices
from shared.constants import DefaultValues as DV
import allure


class TestPostRestartDeviceAdminHotel:
    """ Тесты категории devices, метод POST /device_slots/{id}/restart, роль - администратор гостиницы """
    def test_post_restart_device_stb_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест перезагрузки устройства STB """
        with allure.step('Запрос на перезагрузку STB'):
            r = Devices().post_restart_device_by_id(DV.FIRST_SLOT_ID)

        with allure.step('Проверки на успешный ответ внутри системы'):
            assert_that(r.status_code, equal_to(200))
            assert_that(r.json()["success"], is_(True))

    def test_post_restart_device_smart_tv_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки перезагрузки устройства Smart TV """
        with allure.step('Запрос на перезагрузку Smart TV'):
            r = Devices().post_restart_device_by_id(DV.SECOND_SLOT_ID)

        with allure.step('Проверки на коррекность кодов ошибок и сообщений об ошибке'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(14))
            assert_that(r.json()["description"], equal_to("Not supported for given device type"))

    def test_post_restart_unknown_device_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки перезагрузки неизвестного устройства """
        with allure.step(
                'Запрос на перезагрузку неизвестного устройства (MAC не соответствует ни одному известному устройству'):
            r = Devices().post_restart_device_by_id(DV.THIRD_SLOT_ID)

        with allure.step('Проверки на коррекность кодов ошибок и сообщений об ошибке'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(14))
            assert_that(r.json()["description"], equal_to("Not supported for given device type"))

    def test_post_restart_empty_slot_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки перезагрузки при пустом слоте """
        with allure.step('Запрос на перезагрузку, если в слоте отсутствует устройство'):
            r = Devices().post_restart_device_by_id(DV.FOURTH_SLOT_ID)

        with allure.step('Проверки на коррекность кодов ошибок и сообщений об ошибке'):
            assert_that(r.status_code, equal_to(400))
            assert_that(r.json()["error_code"], equal_to(14))
            assert_that(r.json()["description"], equal_to("Not supported for given device type"))

    def test_post_restart_null_device_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки перезагрузки устройства с несуществующим id """
        with allure.step('Запрос на перезагрузку устройства с несуществующим id (использовался id "qwerty")'):
            r = Devices().post_restart_device_by_id("qwerty")

        with allure.step('Проверки на коррекность кодов ошибок и сообщений об ошибке'):
            assert_that(r.status_code, equal_to(404))
            assert_that(r.json()["error_code"], equal_to(13))
            assert_that(r.json()["description"], equal_to("Service id is not found"))

    def test_post_restart_device_in_another_hotel_by_admin_hotel(self, use_session_admin_hotel):
        """ Тест попытки перезагрузки устройства STB не в своей гостинице """
        with allure.step('Запрос на перезагрузку существующего устройства в чужой гостинице'):
            r = Devices().post_restart_device_by_id(DV.SECOND_HOTEL_FIRST_SLOT_ID)

        with allure.step('Проверки на коррекность кодов ошибок и сообщений об ошибке'):
            assert_that(r.status_code, equal_to(404))
            assert_that(r.json()["error_code"], equal_to(13))
            assert_that(r.json()["description"], equal_to("Service id is not found"))
