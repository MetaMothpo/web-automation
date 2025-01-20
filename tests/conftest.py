import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import TestConfig

@pytest.fixture(scope="function")
def driver():
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # Increase implicit wait to 20 seconds
    driver.implicitly_wait(20)
    driver.maximize_window()
    
    yield driver
    
    # Teardown
    driver.quit() 