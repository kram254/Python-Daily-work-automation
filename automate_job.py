from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin")
    page.get_by_label("Email:").click()
    page.get_by_label("Password:").click()
    page.get_by_role("button", name="Log in").click()
    page.wait_for_load_state ('networkidle')
    page.get_by_role("link", name=" Promotions ").click()
    page.get_by_role("link", name=" Discounts").click()
    page.get_by_role("link", name=" Add new").click()
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("Karios_discount1")
    page.get_by_label("Use percentage").check()
    page.get_by_role("spinbutton", name="0.0000").click()
    page.get_by_label("Discount percentage").fill("30")
    page.get_by_label("Requires coupon code").check()
    page.get_by_label("Coupon code", exact=True).click()
    page.get_by_label("Coupon code", exact=True).fill("Karios-30")
    page.get_by_role("button", name=" Save", exact=True).click()

    # ---------------------
    context.close()
    browser.close()
    
    print('Discount created successfully')


with sync_playwright() as playwright:
    run(playwright)
