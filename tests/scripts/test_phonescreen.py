from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def phone_size():
    # Initialize a new Chrome browser instance
    driver = webdriver.Chrome()
    try:
        # Open the target web application (local development server)
        driver.get("http://localhost:3000/")
        driver.set_window_size(320, 767)
       
       

    finally:
        input("Press Enter to close the browser...")
        driver.quit()



phone_size() 

