import json
from playwright.sync_api import sync_playwright, expect

def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

# Get standard user information
def test_login_from_json():
    config = load_config()
    url = config["base_url"]
    username = config["credentials"]["standard_user"]["username"]
    password = config["credentials"]["standard_user"]["password"]

    # Access the web page and fill standard user information
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto(url)
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_role('button',name='Login').click()

        # Verify the result after loading
        expect(page).to_have_url(f"{url}/inventory.html")
        expect(page).to_have_title("Swag Labs")

        browser.close()