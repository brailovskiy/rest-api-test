import pytest
from api.sessions import Sessions


@pytest.fixture(scope="module")
def use_session_admin_hotel(get_session_admin_hotel):
    """ Фикстура получения сессии сотрудника """
    Sessions().put_session_id_into_headers(get_session_admin_hotel)

    yield
