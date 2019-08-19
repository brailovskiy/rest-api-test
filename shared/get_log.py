import logging
LOGGER = logging.getLogger(__name__)


def get_log(r):
    LOGGER.info("[{}]".format('----------Request params----------'))
    LOGGER.info("{} {}".format('{      REQUEST_METHOD}', str(r.request.method)))
    LOGGER.info("{} {}".format('{         REQUEST_URL}', str(r.request.url)))
    LOGGER.info("{} {}".format('{     REQUEST_HEADERS}', str(r.request.headers)))
    if r.request.body is not None:
        LOGGER.info("{} {}".format('{        REQUEST_BODY}', str(r.request.body)))

    LOGGER.info("[{}]".format('-------------Response-------------'))
    LOGGER.info("{} {}".format('{RESPONSE_STATUS_CODE}', str(r.status_code)))
    if r.text is not None:
        LOGGER.info("{} {}".format('{       RESPONSE_BODY}', str(r.text)))
