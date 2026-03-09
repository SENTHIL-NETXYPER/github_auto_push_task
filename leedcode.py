from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Opening LeetCode...")
    page.goto("https://leetcode.com/problemset/all/")

    page.wait_for_timeout(6000)

    print("Clicking the streak fire icon...")

    # locate the fire icon
    page.locator("text=Streak").first.click()

    page.wait_for_timeout(3000)

    print("Opening daily problem...")

    # click the daily challenge problem
    page.locator("a[href*='/problems/']").first.click()

    time.sleep(10)