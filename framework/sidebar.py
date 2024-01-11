import time

from framework.page import Page


class Sidebar(Page):

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
    ) -> None:
        """This function clicks on each element of the sidebar in turn"""
        self.click_element(sidebar_button)
        time.sleep(1)
        self.click_element(settings_button)
        time.sleep(1)
        self.click_element(back_button)
        time.sleep(1)
        self.click_element(sidebar_button)
        time.sleep(1)
        self.click_element(help_button)
        time.sleep(1)
        self.click_element(back_button)
        time.sleep(2)
        self.click_element(sidebar_button)
        time.sleep(1)
        self.click_element(add_hub_button)
        time.sleep(1)
        self.click_element(hub_back_button)
        time.sleep(2)
        self.click_element(sidebar_button)
        time.sleep(1)
        self.click_element(terms_button)
        time.sleep(1)
        self.click_element(back_button)
        time.sleep(1)
        self.click_element(sidebar_button)
        time.sleep(1)
        self.click_element(logs_button)
