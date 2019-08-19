from dotenv import load_dotenv
from pathlib import Path
import yaml
import os


load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def read_yaml(file_yaml):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_yaml)
    with open(file) as f:
        data = yaml.load(f)
    return data


def _select_env():
    environment = os.getenv("TARGET_ENV")

    if environment == 'prod':
        selected_env = 'prod'
    elif environment == 'test' or environment is None:
        selected_env = 'test'
    else:
        raise ValueError('Incorrect environment data: ' + str(environment) + '. Correct: prod or test. Default: prod')

    return selected_env


def _select_mrf():
    """ Выбор МРФ на основе выбранного окружения """
    mrf = os.getenv("MRF")
    available_mrf = ['mos', 'ural', 'ct', 'volga', 'sibir', 'fe', 'south', 'nw']

    # mos - Москва
    # ural - Урал
    # ct - Центр
    # volga - Волга
    # sibir - Сибирь
    # fe - Дальний Восток
    # south - Юг
    # nw - Северо-Запад

    if mrf in available_mrf:
        return mrf
    elif mrf is None:
        return 'ct'
    else:
        raise ValueError('Incorrect mrf: ' + str(mrf) + '. Correct: ' + str(available_mrf) + '. Default mrf: mos')


def create_env_properties():
    """ Правка allure_results/environments.properties """
    mrf_full = {"mos": "Moscow",
                "ural": "Ural",
                "ct": "Center",
                "volga": "Volga",
                "sibir": "Siberia",
                "fe": "Far East",
                "south": "South",
                "nw": "Northwest"}

    env_full = {"test": "Test",
                "prod": "Production"}

    selected_mrf = _select_mrf()
    selected_env = _select_env()

    for mrf in mrf_full:
        if mrf == selected_mrf:
            selected_mrf = mrf_full[mrf]

    for env in env_full:
        if env == selected_env:
            selected_env = env_full[env]

    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/allure-results/environment.properties')
    with open(file, 'w') as f:
        f.write("SDP_ENVIRONMENT=" + selected_env + "\n" + "MRF=" + selected_mrf)


def get_env_constants(file_yaml):
    """ Получение констант из config.yaml в виде dict'а на основе выбранного окружения и МРФ """
    data = read_yaml(file_yaml)
    selected_env = _select_env()
    selected_mrf = _select_mrf()
    constants = None
    env_data = data[selected_env]

    for i in env_data['mrf']:
        if i == selected_mrf:
            constants = env_data['mrf'][i]
            break

    if constants is not None:
        return constants
    else:
        raise ValueError('Empty data. Check file ' + str(file_yaml))


def get_url(file_yaml):
    """ Получение URL из config.yaml на основе выбранного окружения """
    data = read_yaml(file_yaml)
    selected_env = _select_env()
    url = data[selected_env]['url']
    return url


def get_mrf():
    """ Получение текущего МРФ """
    selected_mrf = _select_mrf()
    return selected_mrf
