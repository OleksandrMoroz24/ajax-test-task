import logging
import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)


def setup_logging():
    logger = logging.getLogger('pytest_logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('pytest.log', mode='a') # 'a' for append mode
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


@pytest.fixture(scope='session', autouse=True)
def configure_logging(request):
    logger = setup_logging()
    request.addfinalizer(lambda: logging.shutdown())
    return logger
