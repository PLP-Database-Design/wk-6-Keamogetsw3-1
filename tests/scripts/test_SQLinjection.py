from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_payloads(email, password):
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:3000/")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        ).click()

        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-email"))
        )
        password_input = driver.find_element(By.ID, "login-password")

        email_input.clear()
        password_input.clear()

        email_input.send_keys(email)
        password_input.send_keys(password)

        driver.find_element(By.XPATH, "//button[text()='Login']").click()

        try:
            WebDriverWait(driver, 5).until(EC.url_contains("profile"))
            print(f"[SUCCESS] Login succeeded for: {email}")
        except:
            errors = driver.find_elements(By.CLASS_NAME, "error-message")
            if errors:
                for error in errors:
                    print(f"[VALIDATION ERROR] {error.text}")
            else:
                print(f"[FAILURE] Login failed for: {email} (no visible validation message)")

    finally:
        input("Press Enter to close the browser...")
        driver.quit()


# === Positive Test (control test) ===
print("=== POSITIVE TEST ===")
login_payloads("user1@test.com", "TestPass123")


# === SQL Injection Negative Tests ===
sql_payloads = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' UNION SELECT * FROM users --"
]

print("\n=== SQL INJECTION TESTS ===")
for payload in sql_payloads:
    print(f"\n[TESTING PAYLOAD] {payload}")
    login_payloads(payload, "test")
