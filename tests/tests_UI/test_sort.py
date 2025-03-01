from playwright.sync_api import Page, expect


def test_sort_from_low_to_high(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")  # Авторизация с правильными данными
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator(".product_sort_container").select_option(
        "lohi"
    )  # Выбираем сортировку от дешевого к дорогому

    prices = page.locator(
        ".inventory_item_price"
    ).all_inner_texts()  # Находим все цены по классу "inventory_item_price"

    prices_float = [
        float(price.replace("$", "")) for price in prices
    ]  # Убираем "$" из цены, чтобы получить список из чисел в формате Float

    assert prices_float == sorted(
        prices_float
    )  # Проверяем список цен совпадает с отсортированным списком цен

    browser.close()


def test_sort_from_high_to_low(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator(".product_sort_container").select_option("hilo")

    prices = page.locator(".inventory_item_price").all_inner_texts()

    prices_float = [float(price.replace("$", "")) for price in prices]

    assert prices_float == sorted(
        prices_float, reverse=True
    )  # Проверяем список цен совпадает с отсортированным в обратном подярядке списком цен

    browser.close()
