import time

import pytest
from appium.webdriver.common.mobileby import MobileBy

from framework.login_page import LoginPage
from framework.sidebar import Sidebar


@pytest.fixture(scope='session')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='session')
def sidebar(driver):
    return Sidebar(driver)


@pytest.fixture(scope='session')
def login_and_get_sidebar(login_page, sidebar):
    # reuse paths for login
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
    time.sleep(3)
    # Use login_page to perform login
    login_page.click_element((
        MobileBy.ID,
        "com.android.permissioncontroller:id/permission_allow_button"
    ))
    # Login with valid credentials
    login_page.login(
        LOGIN_BUTTON_XPATH,
        SECOND_LOGIN_BUTTON_XPATH,
        EMAIL_FIELD_XPATH,
        PASSWORD_FIELD_XPATH,
        "qa.ajax.app.automation@gmail.com",
        "qa_automation_password"
    )

    # Now the sidebar should be accessible as the user is logged in
    return sidebar
