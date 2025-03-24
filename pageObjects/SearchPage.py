from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_product(self, product_name):
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "search")))
        search_box.clear()
        search_box.send_keys(product_name)

    def select_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='ui-menu-item']/a"))).click()

    def select_product(self, product_name):
        product_xpath = f"//a[contains(text(), '{product_name}')]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, product_xpath))).click()
