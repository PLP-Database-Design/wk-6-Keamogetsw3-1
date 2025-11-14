# Import the required Selenium modules
from selenium import webdriver                     # Provides the WebDriver class for browser automation
from selenium.webdriver.common.by import By         # Used to locate elements on a web page
from selenium.webdriver.support.ui import WebDriverWait  # Used to wait for certain conditions to be met
from selenium.webdriver.support import expected_conditions as EC  # Defines expected conditions for waits  

def test_web_interaction():
    # Initialize a new Chrome browser instance
    driver = webdriver.Chrome()
    
    try:
        # Open the target web application (local development server)
        driver.get("https://academy.powerlearnprojectafrica.org/")
        
        # Wait up to 30 seconds for the "PLP Academy" link to be clickable before interacting
        plp_academy = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "PLP Academy"))
        )
        
        # Click the "PLP Academy" link
        plp_academy.click()
        
        # Print the current URL after clicking for debugging or verification
        print("Current URL after clicking PLP Academy:", driver.current_url)
        
        # Verify that the current URL contains "plp" to confirm navigation was successful
        assert "PLP Academy" in driver.current_url.lower(), "Navigation to PLP Academy failed"
    
    finally:
        # Close the browser window and end the WebDriver session
        driver.quit()

# Run the test
test_web_interaction()
