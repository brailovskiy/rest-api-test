from settings import get_env_constants
from settings import get_url
from settings import get_mrf


constants = get_env_constants('config.yaml')
secret_constants = get_env_constants('secret_config.yaml')


class DefaultValues:
    # Дефолтный URL HTM, взятый из config.yaml на основе выбранного окружения
    URL = get_url('config.yaml')

    # Дефолтный URL SDP, взятый из config.yaml на основе выбранного окружения
    SDP_URL = constants['sdp_api_url'] + 'spine/admin_services/json4/'

    # Хедера по-умолчанию
    HEADERS = {'Content-Type': 'application/json'}

    # Текущий МРФ, на котором проводятся тесты (задается в .env)
    ACTUAL_MRF = get_mrf()

    # Данные основной гостиницы
    main_hotel_data = constants['main_hotel']
    MAIN_HOTEL_ID = main_hotel_data['hotel_id']

    # Первая комната
    SAN_MAIN_ROOM = main_hotel_data['main_room']['san']
    NUMBER_MAIN_ROOM = main_hotel_data['main_room']['number']
    SDP_MAIN_ROOM_ID = main_hotel_data['main_room']['sdp_room_id']

    # Первый слот для устройства (STB)
    FIRST_SLOT_ID = main_hotel_data['main_room']['connection_slots']['first_slot']['id']
    FIRST_SLOT_MAC = main_hotel_data['main_room']['connection_slots']['first_slot']['mac']
    FIRST_SLOT_DEVICE_ID = main_hotel_data['main_room']['connection_slots']['first_slot']['device_type']

    # Второй слот для устройства (Smart TV)
    SECOND_SLOT_ID = main_hotel_data['main_room']['connection_slots']['second_slot']['id']
    SECOND_SLOT_MAC = main_hotel_data['main_room']['connection_slots']['second_slot']['mac']
    SECOND_SLOT_DEVICE_ID = main_hotel_data['main_room']['connection_slots']['second_slot']['device_type']

    # Третий слот для устройства (Unknown device)
    THIRD_SLOT_ID = main_hotel_data['main_room']['connection_slots']['third_slot']['id']
    THIRD_SLOT_MAC = main_hotel_data['main_room']['connection_slots']['third_slot']['mac']
    THIRD_SLOT_DEVICE_ID = main_hotel_data['main_room']['connection_slots']['third_slot']['device_type']

    # Четвертый слот для устройства (Empty slot)
    FOURTH_SLOT_ID = main_hotel_data['main_room']['connection_slots']['fourth_slot']['id']
    FOURTH_SLOT_MAC = main_hotel_data['main_room']['connection_slots']['fourth_slot']['mac']
    FOURTH_SLOT_DEVICE_ID = main_hotel_data['main_room']['connection_slots']['fourth_slot']['device_type']

    # Вторая комната
    SAN_SECOND_ROOM = main_hotel_data['second_room']['san']
    NUMBER_SECOND_ROOM = main_hotel_data['second_room']['number']
    SDP_SECOND_ROOM_ID = main_hotel_data['second_room']['sdp_room_id']

    SAN_ROOM_WITH_PURCHASES = main_hotel_data['third_room']['san']
    NUMBER_ROOM_WITH_PURCHASES = main_hotel_data['third_room']['number']
    SDP_ROOM_WITH_PURCHASES_ID = main_hotel_data['third_room']['sdp_room_id']

    # Данные второй гостиницы
    second_hotel_data = constants['second_hotel']
    SECOND_HOTEL_ID = second_hotel_data['hotel_id']

    SECOND_SAN_MAIN_ROOM = second_hotel_data['main_room']['san']
    SECOND_NUMBER_MAIN_ROOM = second_hotel_data['main_room']['number']
    SECOND_SDP_MAIN_ROOM_ID = second_hotel_data['main_room']['sdp_room_id']

    # Первый слот для устройства (STB)
    SECOND_HOTEL_FIRST_SLOT_ID = second_hotel_data['main_room']['connection_slots']['first_slot']['id']
    SECOND_HOTEL_FIRST_SLOT_MAC = second_hotel_data['main_room']['connection_slots']['first_slot']['mac']
    SECOND_HOTEL_FIRST_SLOT_DEVICE_ID = second_hotel_data['main_room']['connection_slots']['first_slot']['device_type']


class UserAuthData:
    user_data = secret_constants['role_auth_data']
    user_data_main_hotel = user_data['main_hotel_users']
    user_data_second_hotel = user_data['second_hotel_users']

    # Данные администратора МРФ
    ADMIN_MRF = {'email': user_data['admin_mrf']['email'], 'password': user_data['admin_mrf']['password']}
    ADMIN_MRF_ID = user_data['admin_mrf']['id']

    # Данные администратора основной гостиницы
    ADMIN_HOTEL = {'email': user_data_main_hotel['admin_hotel']['email'], 'password': user_data_main_hotel['admin_hotel']['password']}
    ADMIN_HOTEL_ID = user_data_main_hotel['admin_hotel']['id']

    # Данные сотрудника основной гостиницы
    EMPLOYEE = {'email': user_data_main_hotel['employee']['email'], 'password': user_data_main_hotel['employee']['password']}
    EMPLOYEE_ID = user_data_main_hotel['employee']['id']

    # Данные администратора второй гостиницы
    SECOND_ADMIN_HOTEL = {'email': user_data_second_hotel['admin_hotel']['email'], 'password': user_data_second_hotel['admin_hotel']['password']}
    SECOND_ADMIN_HOTEL_ID = user_data_second_hotel['admin_hotel']['id']

    # Данные сотрудника второй гостиницы
    SECOND_EMPLOYEE = {'email': user_data_second_hotel['employee']['email'], 'password': user_data_second_hotel['employee']['password']}
    SECOND_EMPLOYEE_ID = user_data_second_hotel['employee']['id']


class SdpAuthData:
    SDP_AUTH_DATA = secret_constants['sdp_auth_data']
