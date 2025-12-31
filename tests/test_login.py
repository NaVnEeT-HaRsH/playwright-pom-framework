import pytest
from pages.login_page import Login
from utils.config import EMAIL,PASSWORD,BASE_URL

@pytest.mark.order(2)
def test_login(page):
    # page = logged_in_page

    # Step 1: Open login page
    page.goto(f"{BASE_URL}/login")

    login = Login(page)

    # Step 2: putting login info
    login.login(EMAIL,PASSWORD)
    assert login.is_user_logged_in(), "user is not logged in"