from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import domain


def test_filter_by_category():
    # Настройка опций Chrome
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 1. Зайти на страницу /cost_table/
        driver.get(f"{domain}/cost_table/")
        print("Страница открыта")

        # Ожидаем элемент выпадающего списка
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "category"))
        )
        print("Выпадающий список стал видимым")

        # 2. Выбрать категорию "Novels"
        category_select = Select(driver.find_element(By.ID, "category"))
        category_select.select_by_visible_text("Novels")
        print("Категория 'Novels' выбрана")

        # 3. Нажать на кнопку "Apply"
        apply_button = driver.find_element(By.XPATH, "//button[text()='Apply']")
        apply_button.click()
        print("Кнопка 'Apply' нажата")

        # Ожидаем отображения таблицы с книгами
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "tbody"))
        )
        print("Таблица с книгами отобразилась")

        # 4. Собираем список названий книг в таблице
        book_titles = [book.text for book in driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(2)")]

        # Список ожидаемых названий книг в категории "Novels"
        expected_book_titles = ["To Kill a Mockingbird", "The Catcher in the Rye"]

        # 5. Проверяем, что в таблице есть хотя бы одна книга из категории "Novels"
        assert any(title in expected_book_titles for title in
                   book_titles), "В таблице нет ни одной книги из категории 'Novels'"
        print("Тест пройден, в таблице присутствует книга из категории 'Novels'")

    finally:
        driver.quit()
        print("Браузер закрыт")
