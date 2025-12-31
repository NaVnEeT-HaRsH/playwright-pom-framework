from playwright.sync_api import Page

class RegisterUser:

    def __init__(self, page: Page):
        self.page = page

        # Step 1
        self.name_input = page.locator("[data-qa='signup-name']")
        self.email_input = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")

        # Step 2
        self.step2_heading = page.locator("text=Enter Account Information")
        self.title_mrs = page.get_by_label("Mrs")
        self.password_input = page.locator("[data-qa='password']")
        self.day = page.locator("[data-qa='days']")
        self.month = page.locator("[data-qa='months']")
        self.year = page.locator("[data-qa='years']")

        # Step 3
        self.step3_heading = page.locator("text=Address Information")
        self.first_name = page.locator("[data-qa='first_name']")
        self.last_name = page.locator("[data-qa='last_name']")
        self.company = page.locator("[data-qa='company']")
        self.address1 = page.locator("[data-qa='address']")
        self.address2 = page.locator("[data-qa='address2']")
        self.state = page.locator("[data-qa='state']")
        self.city = page.locator("[data-qa='city']")
        self.zipcode = page.locator("[data-qa='zipcode']")
        self.mobile = page.locator("[data-qa='mobile_number']")
        self.create_account_btn = page.locator("[data-qa='create-account']")

        # Success page
        self.account_created_heading = page.locator("[data-qa='account-created']")
        self.continue_button = page.locator("[data-qa='continue-button']")



    def sign_up(self, name, email):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def is_step_2_visible(self):
        return self.step2_heading.is_visible()

    def fill_step_2(self, password, day, month, year):
        self.title_mrs.check()
        self.password_input.fill(password)
        self.day.select_option(str(day))
        self.month.select_option(str(month))
        self.year.select_option(str(year))

    def is_step_3_visible(self):
        return self.step3_heading.is_visible()

    def fill_step_3(self, user):
        self.first_name.fill(user)
        self.last_name.fill(user)
        self.company.fill(user)
        self.address1.fill(user)
        self.address2.fill(user)
        self.state.fill(user)
        self.city.fill(user)
        self.zipcode.fill(user)
        self.mobile.fill(user)
        self.create_account_btn.click()

    def is_account_created_visible(self):
        return self.account_created_heading.is_visible()
    
    def continue_after_account_created(self):
        self.continue_button.click()
