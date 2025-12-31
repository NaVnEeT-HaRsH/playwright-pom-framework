from playwright.sync_api import Page

class Logout:
    def __init__(self,page: Page):
        self.page = page

        self.logout_btn = page.locator(".navbar-nav").get_by_text("Logout")

    def logout_user(self):
        self.logout_btn.click()