from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import api_domain


def test_filter_by_category():
    # Настройка опций Chrome для запуска в headless режиме
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Шаг 1: Открытие страницы
        driver.get(f"{api_domain}/cost_table/")
        print("Страница открыта")

        # Ожидание элемента выпадающего списка
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "category"))
        )
        print("Выпадающий список стал видимым")

        category_select = Select(driver.find_element(By.ID, "category"))
        category_select.select_by_visible_text("Novels")
        print("Категория 'Novels' выбрана")

        # Нажатие на кнопку "Применить"
        apply_button = driver.find_element(By.XPATH, "//button[text()='Apply']")
        apply_button.click()
        print("Кнопка 'Применить' нажата")

        # Ожидание отображения таблицы с книгами
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "tbody"))
        )
        print("Таблица с книгами отобразилась")

        # Здесь можно добавить дополнительные проверки и выводить результаты в консоль
        # Например, получить и распечатать названия книг из таблицы

    finally:
        driver.quit()
        print("Браузер закрыт")
