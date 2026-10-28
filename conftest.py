
import json
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright


def load_config():
    config_path = Path(__file__).resolve().parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def login(page):
    config = load_config()
    url = config["base_url"]
    username = config["credentials"]["standard_user"]["username"]
    password = config["credentials"]["standard_user"]["password"]

    page.goto(url)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo= 500)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def logged_in_page(page):
    login(page)
    return page
