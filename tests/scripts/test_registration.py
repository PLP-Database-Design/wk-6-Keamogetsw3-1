from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def register_user(name, email, password):
    # Initialize a new Chrome browser instance
    driver = webdriver.Chrome()
    try:
        # Open the target web application (local development server)
        driver.get("http://localhost:3000/")
        
        # Open registration page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        ).click()
        
        # Wait for form fields
        full_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "register-name"))
        )
        email_input = driver.find_element(By.ID, "register-email")
        password_input = driver.find_element(By.ID, "register-password")
        
        # Fill form
        full_name_input.clear()
        email_input.clear()
        password_input.clear()
        full_name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        
        # Submit form
        driver.find_element(By.XPATH, "//button[text()='Register']").click()
        
        # Check for either success or validation errors
        try:
            # Wait for URL to change to login (successful registration)
            WebDriverWait(driver, 5).until(EC.url_contains("login"))
            print(f"[SUCCESS] Registration succeeded for: {email}")
        except:
            # Capture validation error messages on the page
            errors = driver.find_elements(By.CLASS_NAME, "error-message")
            if errors:
                for error in errors:
                    print(f"[VALIDATION ERROR] {error.text}")
            else:
                print(f"[FAILURE] Registration failed for: {email} (no visible validation message)")

    finally:
        input("Press Enter to close the browser...")
        driver.quit()


# === Run Positive Test ===
register_user("Valid Name", "valid@email.com", "ValidPass123") # Valid details

# === Run Negative Tests ===
register_user("Valid Name", "invalid-email", "ValidPass123")     # Invalid email
register_user("", "valid@email.com", "ValidPass123")         # Empty name
register_user("Valid Name", "", "ValidPass123")                  # Empty email
register_user("Valid Name", "valid@email.com", "")            # Empty password
