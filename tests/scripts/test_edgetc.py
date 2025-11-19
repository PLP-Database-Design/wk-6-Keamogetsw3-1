from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

def login_user_and_schedule(email, password):
    # Initialize Chrome
    driver = webdriver.Chrome()
    
    try:
        # Open web app
        driver.get("http://localhost:3000/")
        
        # Go to login page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        ).click()
        
        # Wait for email/password fields
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-email"))
        )
        password_input = driver.find_element(By.ID, "login-password")
        
        # Fill login form
        email_input.clear()
        password_input.clear()
        email_input.send_keys(email)
        password_input.send_keys(password)
        
        # Submit login form
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        
        # Wait for profile page or validation errors
        try:
            WebDriverWait(driver, 5).until(EC.url_contains("profile"))
            print(f"[SUCCESS] Login succeeded for: {email}")
            
            # --- Schedule a Pickup ---
            # Navigate to Pickup Scheduling page
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Schedule Pickup"))
            ).click()
