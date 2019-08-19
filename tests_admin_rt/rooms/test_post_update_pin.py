from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
import allure


class TestPostUpdatePinAdminRt:
    """ Тесты категории Rooms, метод POST /id/update_pin, роль - администратор Ростелеком """
    def test_update_pin_by_admin_rt(self, use_session_admin_rt, check_in_room_number):
        """ Тест попытки изменения ПИН-кода """
        with allure.step('Запрос на изменение ПИН-кода'):
            r = Rooms().post_update_pin_by_san(DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что администратор Ростелеком не может изменить ПИН-код в номере'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(11))

        # Дописать проверку описания, когда будет починен баг https://git.itv.restr.im/ITV.RT/b2b/hotel-tv/issues/103
        # with allure.step('Проверка'):
        #     assert_that(r.json()["description"], equal_to(""))
