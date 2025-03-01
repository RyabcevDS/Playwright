from playwright.sync_api import Playwright, sync_playwright, expect


def test_purchase(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")  # Вводим логин
    page.locator("#password").fill("secret_sauce")  # Вводим пароль
    page.locator("#login-button").click()  # Нажимаем на кнопку "Login"
    page.locator(
        "#add-to-cart-sauce-labs-backpack"
    ).click()  # Добавляем товар в корзину
    page.locator("#shopping_cart_container > a").click()  # Переходим в корзину
    page.locator("#checkout").click()  # Переходим на оплату
    page.locator("#first-name").fill("Dima")  # Вводим имя получателя
    page.locator("#last-name").fill("Ryabcev")  # Вводим фамилию получателя
    page.locator("#postal-code").fill("133332213")  # Вводим индекс
    page.locator("#continue").click()
    page.locator("#finish").click()
    expect(
        page.locator("text=Thank you for your order!")
    )  # Проверяем текст об успешности
    expect(page.locator("#back-to-products")).to_be_visible()
    browser.close()