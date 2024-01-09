from .page import Page


class LoginPage(Page):

    def enter_email(self, locator: tuple, email: str) -> None:
        """ Enter email in email field """
        self.enter_text(locator, email)

    def enter_password(self, locator: tuple, password: str) -> None:
        """ Enter password in password field """
        self.enter_text(locator, password)

    def click_login_button(self, locator: tuple) -> None:
        """ Clic on first login button """
        self.click_element(locator)

    def click_second_login_button(self, locator: tuple) -> None:
        """ Clic on second login button """
        self.click_element(locator)

    def login(
            self,
            first_login_locator: tuple,
            second_login_locator: tuple,
            email_locator: tuple,
            password_locator: tuple,
            email: str,
            password: str
    ) -> None:
        """ General method for login """
        self.click_login_button(first_login_locator)
        self.enter_email(email_locator, email)
        self.enter_password(password_locator, password)
        self.click_second_login_button(second_login_locator)
