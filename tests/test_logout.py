import pytest
from pages.logout_page import Logout

@pytest.mark.order(4)
def test_logout(logged_in_page):
    page = logged_in_page

    logout = Logout(page)
    logout.logout_user()