import pytest
from api.sessions import Sessions
import logging
LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def delete_session():
    """ Удалить сессию из headers, если она есть """
    Sessions().delete_session_id_from_headers()

    yield
