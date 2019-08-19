import pytest
from api.sessions import Sessions


@pytest.fixture(scope="module")
def use_session_admin_rt(get_session_admin_rt):
    """ Фикстура получения сессии сотрудника """
    Sessions().put_session_id_into_headers(get_session_admin_rt)

    yield


@pytest.fixture(scope="function")
def default_hotel_settings():
    """ Фикстура для задания дефолтных значений настроек гостиницы """
    # Методом SDP присвоить дефолтные значения гостинице до теста

    yield

    # После теста также установить дефолтные значения
