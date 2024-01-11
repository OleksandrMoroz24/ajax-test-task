import time

from appium.webdriver.common.mobileby import MobileBy

# locators for test
SIDEBAR_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/menuDrawer"
)
SETTINGS_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/settings"
)
HELP_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/help"
)
LOGS_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/logs"
)
ADD_HUB_XPATH = (
    MobileBy.XPATH,
    "//android.widget.Button"
)
TERMS_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/documentation_text"
)
BACK_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/back"
)
HUB_BACK_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/backButton"
)
SWIPE_DOWN_BUTTON_ID = (
    MobileBy.ID,
    "com.ajaxsystems:id/toolbar"
)


def test_sidebar(login_and_get_sidebar):
    sidebar = login_and_get_sidebar
    time.sleep(5)
    sidebar.click_all_sidebar_elements(
        SIDEBAR_BUTTON_ID,
        SETTINGS_BUTTON_ID,
        HELP_BUTTON_ID,
        LOGS_BUTTON_ID,
        ADD_HUB_XPATH,
        TERMS_BUTTON_ID,
        BACK_BUTTON_ID,
        HUB_BACK_BUTTON_ID,
    )
