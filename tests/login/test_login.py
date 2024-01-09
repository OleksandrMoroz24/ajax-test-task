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


def test_user_login_valid_credentials(user_login_fixture):
    # Grant permissions if asked
    user_login_fixture.click_element((
        MobileBy.ID,
        "com.android.permissioncontroller:id/permission_allow_button"
    ))
    # Login with valid credentials
    user_login_fixture.login(
        LOGIN_BUTTON_XPATH,
        SECOND_LOGIN_BUTTON_XPATH,
        EMAIL_FIELD_XPATH,
        PASSWORD_FIELD_XPATH,
        "oleksandrmoroz2003@gmail.com",
        "Ajax2405!"
    )
    time.sleep(5)
    try:
        user_login_fixture.find_element((MobileBy.ID, "com.ajaxsystems:id/hubAdd"))
        # Element is found. You can add further actions or assertions here.
    except NoSuchElementException:
        # Element is not found. Handle the situation or assert failure.
        assert False, "Element with ID 'com.ajaxsystems:id/hubAdd' not found"
    # user_login_fixture.driver.reset()


def test_user_login_invalid_credentials(user_login_fixture):
    user_login_fixture.driver.reset()
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
        "ivalid@gmail.com",
        "invalidpassword"
    )
    time.sleep(3)
    try:
        user_login_fixture.find_element((MobileBy.ID, "com.ajaxsystems:id/hubAdd"))
        # If the element is found, assert failure, because it should not be present
        assert False, "Element unexpectedly found"
    except NoSuchElementException:
        # If NoSuchElementException is raised, the test should pass
        pass
