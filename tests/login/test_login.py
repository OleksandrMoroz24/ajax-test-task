import logging
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

# XPath locators
LOGIN_BUTTON_XPATH = (
    MobileBy.XPATH,
    "(//androidx.compose.ui.platform."
    "ComposeView[@resource-id='com.ajaxsystems:id/compose_view'])"
    "[1]/android.view.View/android.view.View/android.widget.Button"
)
EMAIL_FIELD_XPATH = (
    MobileBy.XPATH,
    "//android.widget.EditText"
    "[@resource-id='com.ajaxsystems:id/authLoginEmail']"
)
PASSWORD_FIELD_XPATH = (
    MobileBy.XPATH,
    "//android.widget.EditText"
    "[@resource-id='com.ajaxsystems:id/authLoginPassword']"
)
SECOND_LOGIN_BUTTON_XPATH = (
    MobileBy.XPATH,
    "(//androidx.compose.ui.platform."
    "ComposeView[@resource-id='com.ajaxsystems:id/compose_view'])"
    "[4]/android.view.View/android.view.View/android.widget.Button"
)


def test_user_login_invalid_credentials(user_login_fixture):
    # logging
    logger = logging.getLogger('pytest_logger')
    logger.info("Starting test_user_login_invalid_credentials")

    time.sleep(3)  # extra time for weaker systems
    # Grant permissions if asked
    user_login_fixture.click_element((
        MobileBy.ID,
        "com.android.permissioncontroller:id/permission_allow_button"
    ))
    # Login with invalid credentials
    user_login_fixture.login(
        LOGIN_BUTTON_XPATH,
        SECOND_LOGIN_BUTTON_XPATH,
        EMAIL_FIELD_XPATH,
        PASSWORD_FIELD_XPATH,
        "invalid@gmail.com",
        "invalidpassword!"
    )
    time.sleep(3)
    try:
        user_login_fixture.find_element((MobileBy.ID, "com.ajaxsystems:id/hubAdd"))
        # If the element is found, assert failure, because it should not be present
        logger.error("Error in test_user_login_invalid_credentials")
        assert False, "Element unexpectedly found"
    except NoSuchElementException:
        # If NoSuchElementException is raised, the test should pass
        pass
    user_login_fixture.driver.reset()

    logger.info("test_user_login_invalid_credentials completed successfully")


def test_user_login_valid_credentials(user_login_fixture):
    # logging
    logger = logging.getLogger('pytest_logger')
    logger.info("Starting test_user_login_valid_credentials")

    time.sleep(1)
    # Grant permissions if asked
    user_login_fixture.click_element((
        MobileBy.ID,
        "com.android.permissioncontroller:id/permission_allow_button"
    ))
    time.sleep(1)
    # Login with valid credentials
    user_login_fixture.login(
        LOGIN_BUTTON_XPATH,
        SECOND_LOGIN_BUTTON_XPATH,
        EMAIL_FIELD_XPATH,
        PASSWORD_FIELD_XPATH,
        "qa.ajax.app.automation@gmail.com",
        "qa_automation_password"
    )
    time.sleep(5)

    try:
        user_login_fixture.find_element((MobileBy.ID, "com.ajaxsystems:id/hubAdd"))
        # Element on main page is found.
    except NoSuchElementException:
        # Element is not found.
        logger.error("Error in test_user_login_valid_credentials ")
        assert False, "Element with ID 'com.ajaxsystems:id/hubAdd' not found"

    logger.info("test_user_login_valid_credentials completed successfully")
