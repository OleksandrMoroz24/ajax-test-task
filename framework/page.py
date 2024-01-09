from appium.webdriver import WebElement


class Page:
    def __init__(self, driver):
        self.driver = driver

    """
    A locator is a tuple that specifies how to find a certain element.

    The locator tuple consists of two parts:
    1. 'by': The method to use for locating the element (e.g., MobileBy.XPATH).
    2. 'element': The specific identifier for the element (e.g., XPath, CSS selector).

    Example:
        The following locator finds an element by its XPath:

        (
            MobileBy.XPATH,
            "//android.widget.EditText"
            "[@resource-id='com.ajaxsystems:id/authLoginEmail']"
        )
    """
    def find_element(self, locator: tuple) -> WebElement:
        """ Find an element by a given locator """
        return self.driver.find_element(*locator)

    def click_element(self, locator: tuple) -> None:
        """ Click on the element at the specified locator """
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text) -> None:
        """ Enter text in the input field at the specified locator """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
