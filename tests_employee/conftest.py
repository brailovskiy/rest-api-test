# -*- coding: utf-8 -*-
import pytest
from api.sessions import Sessions


@pytest.fixture(scope="module")
def use_session_employee(get_session_employee):
    """ Фикстура получения сессии сотрудника """
    Sessions().put_session_id_into_headers(get_session_employee)

    yield
