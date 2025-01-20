from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, by, value):
        return self.wait.until(
            EC.element_to_be_clickable((by, value))
        )

    def find_clickable_element(self, by, value):
        return self.wait.until(
            EC.element_to_be_clickable((by, value))
        )

    def click(self, by, value):
        element = self.wait.until(
            EC.visibility_of_element_located((by, value))
        )
        self.wait.until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def input_text(self, by, value, text):
        element = self.wait.until(
            EC.visibility_of_element_located((by, value))
        )
        element.clear()
        element.send_keys(text)

    def select_dropdown(self, by, value, option):
        element = self.wait.until(
            EC.visibility_of_element_located((by, value))
        )
        Select(element).select_by_value(option) 