from playwright.sync_api import Page,expect

class Products():
    def __init__(self, page: Page):
        self.page = page

        # First product card
        self.product_card = page.locator(".product-image-wrapper").first

        # IMPORTANT: overlay Add to Cart button
        self.add_to_cart_btn = self.product_card.locator(
            ".product-overlay .add-to-cart"
        )

    def add_to_cart(self):
        
        # Hover on product to reveal overlay
        self.product_card.hover()

        # Click ONLY overlay button (single element)
        self.add_to_cart_btn.click()

        expect(self.page.get_by_text("Added!")).to_be_visible()