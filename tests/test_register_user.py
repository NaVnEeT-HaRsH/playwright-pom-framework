import pytest
from pages.register_user_page import RegisterUser
from utils.config import (
    NAME,
    EMAIL,
    BASE_URL,
    PASSWORD,
    DAY,
    MONTH,
    YEAR,
    RANDOME_DATA
)

@pytest.mark.order(1)
def test_user_can_register(page):
    # page = logged_in_page

    # Step 1: Open signup page
    page.goto(f"{BASE_URL}/signup")

    register = RegisterUser(page)

    # Step 2: Signup basic info
    register.sign_up(NAME, EMAIL)
    assert register.is_step_2_visible(), "Step 2 page is not visible"

    # Step 3: Account info
    register.fill_step_2(PASSWORD, DAY, MONTH, YEAR)
    assert register.is_step_3_visible(), "Step 3 page is not visible"

    # Step 4: Address info
    register.fill_step_3(RANDOME_DATA)
        
    # Step 5: Success validation
    assert register.is_account_created_visible(), "Account Created page is not visible"

    register.continue_after_account_created()