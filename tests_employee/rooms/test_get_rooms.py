from hamcrest import *
from shared.constants import DefaultValues as DV
from api.rooms import Rooms
from shared.generate_data import SearchData
import allure


class TestGetRoomsEmployee:
    """ Тесты категории Rooms, метод GET /rooms, роль - сотрудник """
    def test_get_rooms_by_employee(self, use_session_employee, free_room_number):
        """ Тест получения списка номеров сотрудником """
        with allure.step('Запрос на получение списка номеров'):
            r = Rooms().get_rooms()

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что в гостинице 3 номера'):
            assert_that(r.json()["rooms"], has_length(3))

        with allure.step('Проверки, что отображается информация о комнатах (на примере выселенной главной комнаты)'):
            assert_that(r.json()["rooms"][0]["id"], equal_to(DV.SAN_MAIN_ROOM))
            assert_that(r.json()["rooms"][0]["status"], equal_to("CheckOut"))

    def test_get_rooms_with_search_by_number_exact_match_by_employee(self, use_session_employee, free_room_number):
        """ Тест получения списка номеров с поиском search по номеру (точное совпадение) сотрудником """
        with allure.step('Запрос на получение списка номеров с поиском search по номеру (точное совпадение)'):
            r = Rooms().get_rooms(search=DV.NUMBER_MAIN_ROOM)

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверки, что нашлась одна комната и отображается ее информация (главная, выселенная)'):
            assert_that(r.json()["rooms"], has_length(1))
            assert_that(r.json()["rooms"][0]["id"], equal_to(DV.SAN_MAIN_ROOM))
            assert_that(r.json()["rooms"][0]["status"], equal_to("CheckOut"))

    def test_get_rooms_with_search_by_number_overlap_by_employee(self, use_session_employee, free_room_number):
        """ Тест получения списка номеров с поиском search по номеру (частичное совпадение) сотрудником """
        with allure.step('Запрос на получение списка номеров с поиском search по номеру (частичное совпадениее)'):
            r = Rooms().get_rooms(search=SearchData.do_short_room_number(DV.NUMBER_MAIN_ROOM))

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверки, что нашлись все 3 комнаты и отображается их информация (на примере выселенной главной комнаты)'):
            assert_that(r.json()["rooms"], has_length(3))
            assert_that(r.json()["rooms"][0]["id"], equal_to(DV.SAN_MAIN_ROOM))
            assert_that(r.json()["rooms"][0]["status"], equal_to("CheckOut"))

    def test_get_rooms_with_pagination_by_employee(self, use_session_employee):
        """ Тест получения списка номеров с пагинацией сотрудником """
        # page - номер текущей страницы (начиная с 0)
        # page_size - количество элементов на странице

        with allure.step('Запрос на получение списка номеров с пагинацией (1 элемент на странице, вторая страница)'):
            r = Rooms().get_rooms(page=1, page_size=1)

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что на второй странице только один элемент, и это вторая комната'):
            assert_that(r.json()["rooms"], has_length(1))
            assert_that(r.json()["rooms"][0]["id"], equal_to(DV.SAN_SECOND_ROOM))

    def test_get_rooms_with_search_by_incorrect_by_employee(self, use_session_employee):
        """ Тест получения списка номеров по несуществующему номеру сотрудником """
        with allure.step('Запрос на получение списка номеров по несуществующему номеру'):
            r = Rooms().get_rooms(number="qwerty")

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверка, что номеров не нашлось'):
            assert_that(r.json()["rooms"], equal_to(None))

    def test_get_rooms_with_search_by_number_by_employee(self, use_session_employee, free_room_number):
        """ Тест получения списка номеров с поиском number по номеру (точное совпадение) сотрудником """
        with allure.step('Запрос на получение списка номеров с поиском number по номеру (точное совпадение)'):
            r = Rooms().get_rooms(number=DV.NUMBER_MAIN_ROOM)

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверки, что нашелся только 1 элемент, и это выселенная главная комната'):
            assert_that(r.json()["rooms"], has_length(1))
            assert_that(r.json()["rooms"][0]["id"], equal_to(DV.SAN_MAIN_ROOM))
            assert_that(r.json()["rooms"][0]["status"], equal_to("CheckOut"))

    def test_get_rooms_with_search_by_status_by_employee(self, use_session_employee, free_room_number):
        """ Тест получения списка номеров с поиском status по статусу сотрудником """
        with allure.step('Запрос на получение списка номеров с поиском status по статусу'):
            r = Rooms().get_rooms(status="CheckOut")

        with allure.step('Проверка на успешный статус код'):
            assert_that(r.status_code, equal_to(200))

        with allure.step('Проверки, что в списке результатов присутствует выселенная главная комната'):
            assert_that(r.json()["rooms"][0]["id"], equal_to(DV.SAN_MAIN_ROOM))
            assert_that(r.json()["rooms"][0]["status"], equal_to("CheckOut"))
