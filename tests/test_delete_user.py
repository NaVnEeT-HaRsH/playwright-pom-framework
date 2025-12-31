import pytest
from pages.delete_user_page import Delete

@pytest.mark.order(5)
def test_delete_user(logged_in_page):
    page = logged_in_page

    test_delete_user = Delete(page)
    test_delete_user.delete_user()