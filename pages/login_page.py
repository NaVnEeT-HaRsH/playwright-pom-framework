from playwright.sync_api import Page

class Login:
    def __init__(self, page:Page):
        self.page = page

        # LOGIN FORM
        self.email = page.locator("[data-qa='login-email']")
        self.password = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")

        self.login_verify_text = page.get_by_text("Logged in as")

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
    
    def is_user_logged_in(self):
        return self.login_verify_text.is_visible()