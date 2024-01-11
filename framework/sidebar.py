from appium.webdriver.common.touch_action import TouchAction

from framework.page import Page


class Sidebar(Page):
    # id com.ajaxsystems:id/menuDrawer id com.ajaxsystems:id/back
    # id com.ajaxsystems:id/settings
    # id com.ajaxsystems:id/help
    # id com.ajaxsystems:id/logs
    # xpath //android.widget.Button com.ajaxsystems:id/backButton HUB
    # id com.ajaxsystems:id/documentation_text

    def swipe_down(self) -> None:
        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']

        # Define start and end points for the swipe
        start_x = screen_width / 2
        start_y = screen_height / 4  # Starting from one-quarter down the screen
        end_x = start_x
        end_y = start_y + screen_height / 2  # Ending halfway down the screen

        # Create a TouchAction sequence
        action = TouchAction(self.driver)

        # Perform the swipe down action
        action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()

    def click_all_sidebar_elements(
            self,
            sidebar_button: tuple,
            settings_button: tuple,
            help_button: tuple,
            logs_button: tuple,
            add_hub_button: tuple,
            terms_button: tuple,
            back_button: tuple,
            hub_back_button: tuple
    ):
        self.click_element(sidebar_button)
        self.click_element(settings_button)
        self.click_element(back_button)
        self.click_element(sidebar_button)
        self.click_element(help_button)
        self.click_element(back_button)
        self.click_element(sidebar_button)
        self.click_element(logs_button)
        self.swipe_down()
        self.click_element(sidebar_button)
        self.click_element(add_hub_button)
        self.click_element(hub_back_button)
        self.click_element(terms_button)
        self.click_element(back_button)


