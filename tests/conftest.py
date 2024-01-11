import logging
import subprocess
import time
import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723', android_get_desired_capabilities())
    yield driver


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
