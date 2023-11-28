from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oc.kg/")
    page.locator("#bestsellers div").filter(has_text="TOP-20 к новогодним каникулам По версии нашего каталога").locator("div").get_by_role("link").click()
    page.get_by_role("link", name="Ирония судьбы, или с легким паром").click()
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
