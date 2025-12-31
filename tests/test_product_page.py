import pytest
from pages.product_page import Products
from utils.config import BASE_URL

@pytest.mark.order(3)
def test_product(logged_in_page):
    page = logged_in_page
    
    # open product page
    page.goto(f"{BASE_URL}/products")

    product = Products(page)

    product.add_to_cart()