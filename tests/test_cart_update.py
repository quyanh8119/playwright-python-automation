from playwright.sync_api import expect

# Add one item to cart and verify cart count
def test_cart_update(logged_in_page):
    page = logged_in_page

    # Count initial cart number
    cart_container = page.locator('a.shopping_cart_link')
    text = cart_container.inner_text() if cart_container.count() > 0 else ""
    cart_initial_count = int(text) if text.strip() else 0

    # Add one item to cart
    page.get_by_text('Sauce Labs Backpack').click()
    page.get_by_role('button', name='Add to cart').click()

    # Verify the cart count increases by 1
    expect(cart_container).to_have_text(str(cart_initial_count +1))


