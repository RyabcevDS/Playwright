from playwright.sync_api import Playwright, sync_playwright, expect


def test_check_authorization(
    playwright,
):  # Проверка авторизации с правильным логином и паролем
    browser = playwright.chromium.launch(headless=False) # Установить True, если хотим чтобы тесты проходили без открытия браузера
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")  # Вводим логин
    page.locator("#password").fill("secret_sauce")  # Вводим пароль
    page.locator("#login-button").click()  # Нажимаем на кнопку "Login"
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )  # Проверяем что авторизация прошла успешно и происходит редирект
    browser.close()


def test_check_wrong_authorization(
    playwright,
):  # Проверка авторизации с неправильным Логином и паролем
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("Wrong_login")  # Вводим неправильный логин
    page.locator("#password").fill("wrong_password")  # Вводим неправильный пароль
    page.locator("#login-button").click()  # Нажимаем на кнопку "Login"
    expect(
        page.locator(
            "#login_button_container > div > form > div.error-message-container.error > h3"
        )  # Проверка что видно ошибку об ошибке авторизации
    ).to_be_visible()
    browser.close()


def test_check_login_button_color(playwright):  # Проверка цвета кнопки авторизации
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    button_color = page.locator("#login-button").evaluate(
        "(button) => window.getComputedStyle(button).backgroundColor"
    )  # Получаем цвет кнопки
    assert (
        button_color == "rgb(61, 220, 145)"
    )  # Сравниваем полученный цвет кнопки с нужным
    browser.close()