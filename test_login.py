# # from playwright.sync_api import Playwright, sync_playwright, expect
# import re
# from playwright.sync_api import Page, expect

# def run(playwrigth : Page) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()
#     expect(page.get_by_text("Swag Labs")).to_be_visible()

#     # ---------------------
#     # context.close()
#     # browser.close()


# # with sync_playwright() as playwright:
# #     run(playwright)