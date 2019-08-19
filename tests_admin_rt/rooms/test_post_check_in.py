from hamcrest import *
from shared.constants import DefaultValues as DV
from shared.sdp_actions_room import RoomControl as RC
from api.rooms import Rooms
import allure


class TestPostCheckInAdminRt:
    """ Тесты категории Rooms, метод POST /id/checkin, роль - администратор Ростелеком """
    def test_check_in_by_admin_rt(self, use_session_admin_rt, free_room_number):
        """ Тест попытки заселения номера """
        with allure.step('Запрос на заселение номера'):
            r = Rooms(name="Guest").post_check_in(DV.SAN_MAIN_ROOM)

        with allure.step('Проверки, что администратор Ростелеком не может заселять номера'):
            assert_that(r.status_code, equal_to(403))
            assert_that(r.json()["error_code"], equal_to(11))

        # Дописать проверку описания, когда будет починен баг https://git.itv.restr.im/ITV.RT/b2b/hotel-tv/issues/103
        # with allure.step('Проверка'):
        #     assert_that(r.json()["description"], equal_to(""))

        with allure.step('Проверка через метод SDP, что комната свободна'):
            status = RC().get_room_param('state_name')
            assert_that(status, equal_to("CheckOut"))
