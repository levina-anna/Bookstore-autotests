import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import api_domain


class CostTableTest(unittest.TestCase):
    def setUp(self):
        # Инициализация драйвера (в этом примере используется Chrome)
        self.driver = webdriver.Chrome()
        self.driver.get(f"{api_domain}/cost_table/")

    def test_select_category(self):
        driver = self.driver

        # Выбор категории "Романы"
        select = Select(driver.find_element(By.ID, "category"))
        select.select_by_visible_text("Романы")

        # Нажатие на кнопку "Применить"
        driver.find_element(By.XPATH, "//button[text()='Применить']").click()

        # Ожидание загрузки результатов
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "tbody"))
        )

        # Проверка результатов
        rows = driver.find_elements(By.XPATH, "//tbody/tr")
        self.assertTrue(len(rows) > 0, "В таблице нет строк.")

        # Здесь можно добавить дополнительные проверки, например, соответствие названий книг категории "Романы"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
