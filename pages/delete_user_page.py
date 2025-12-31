from playwright.sync_api import Page,expect

class Delete:
    def __init__(self,page: Page):
        self.page = page
        self.delete_btn = page.locator(".navbar-nav").get_by_text("Delete Account")
        self.continue_button = page.locator("[data-qa='continue-button']")

    def delete_user(self):
        self.delete_btn.click()
        expect(self.page.get_by_text("Account Deleted!"))

    def continue_after_account_created(self):
        self.continue_button.click()