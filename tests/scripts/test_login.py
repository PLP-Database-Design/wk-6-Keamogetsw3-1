from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_user(email, password):
    # Initialize a new Chrome browser instance
    driver = webdriver.Chrome()
    try:
        # Open the target web application (local development server)
        driver.get("http://localhost:3000/")
        
        # Open registration page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        ).click()
        
        # Wait for form fields
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-email"))
        )
        password_input = driver.find_element(By.ID, "login-password")
        
        # Fill form
        email_input.clear()
        password_input.clear()
        email_input.send_keys(email)
        password_input.send_keys(password)
        
        # Submit form
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        
        # Check for either success or validation errors
        try:
            # Wait for URL to change to login (successful registration)
            WebDriverWait(driver, 5).until(EC.url_contains("profile"))
            print(f"[SUCCESS] Login succeeded for: {email}")
        except:
            # Capture validation error messages on the page
            errors = driver.find_elements(By.CLASS_NAME, "error-message")
            if errors:
                for error in errors:
                    print(f"[VALIDATION ERROR] {error.text}")
            else:
                print(f"[FAILURE] Login failed for: {email} (no visible validation message)")

    finally:
        input("Press Enter to close the browser...")
        driver.quit()


# === Run Positive Test ===
login_user("user1@test.com ", "TestPass123") # Valid details

# === Run Negative Tests ===
login_user("user1@test.com ", "WrongPassword")            # Incorrect password
login_user("invalid-email", "TestPass123")                # Invalid email
login_user("", "ValidPass123")                            # Empty email
login_user("user1@test.com ", "")                         # Empty password
login_user("unregistereduser@test.com ", "ValidPass123")  # unregistered user
