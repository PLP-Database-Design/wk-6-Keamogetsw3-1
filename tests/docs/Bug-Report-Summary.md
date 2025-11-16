# 🐞 CleanCity Bug Report Summary 

**Project:** CleanCity – Waste Pickup Scheduler  
**Version:** 1.0  
**Prepared by:** QA Team  
**Date:** 18 November 2025 

---

## 🔍 Overview

This document provides a summary of all defects identified during manual and automated testing of the CleanCity application.  

## ✅ Expected Behaviors

# 🐞 BUG-001
**Title:** Profile displays email username instead of Full Name  
**GitHub Link:** D-001  
**Requirement Affected:** User Registration – Profile Display  
**Severity:** Cosmetic  
**Environment:** Development | Chrome | Windows 10  

## Summary  
After successful registration, the User Profile page displays the username portion of the email (e.g., *user1* from *user1@test.com*) instead of the full name entered during registration. This causes user confusion and violates the expected display rule.

## Steps to Reproduce
1. Register a new user:
   - Full Name: *New Test User*
   - Email: *newuser@test.com*
   - Password: *NewPass123*
2. Log in with the new account.
3. Navigate to **Profile Page**.
4. Observe the displayed name.

## Expected Result  
The profile should display the **Full Name** entered during registration.

## Actual Result  
The profile displays the **email username** instead of the actual Full Name.

---

# 🐞 BUG-002
**Title:** Login accepts incorrect password  
**GitHub Link:** D-002  
**Requirement Affected:** User Login – Authentication  
**Severity:** Critical  
**Environment:** Development | Chrome | Windows 10  

## Summary  
A user can log into the system using an incorrect password. This is a severe security flaw as authentication is bypassed.

## Steps to Reproduce
1. Register a user:
   - Email: *user1@test.com*
   - Password: *TestPass123*
2. Log out.
3. Attempt login using **any wrong password**.
4. Observe login result.

## Expected Result  
System should reject incorrect passwords with the error:  
**“Invalid email or password.”**

## Actual Result  
System logs the user in using **incorrect credentials**.

---

# 🐞 BUG-003
**Title:** System allows login with unregistered credentials  
**GitHub Link:** D-003  
**Requirement Affected:** Authentication Validation  
**Severity:** Critical  

## Summary  
Users can log in with credentials that do not exist in the database.

## Steps to Reproduce  
1. Open login page.  
2. Enter:
   - Email: *nonexist@test.com*
   - Password: *AnyPassword*
3. Click **Login**.

## Expected Result  
System should validate against database and reject.

## Actual Result  
System logs in without verifying credentials.

---

# 🐞 BUG-004
**Title:** Pick-up request submitted without user authentication  
**GitHub Link:** D-004  
**Requirement Affected:** Pickup Request Authentication  
**Severity:** High  

## Summary  
Pickup requests can be submitted even when the user is not logged in.

## Expected Result  
System must require login before allowing pickup submission.

## Actual Result  
Pickup is accepted without authentication.

---

# 🐞 BUG-005
**Title:** System accepts pickup date in the past  
**GitHub Link:** D-005  
**Requirement Affected:** Scheduling – Date Validation  
**Severity:** Medium  

## Summary  
Users can schedule pickup requests using past dates.

---

# 🐞 BUG-006
**Title:** Pickup instructions accept more than 200 characters  
**GitHub Link:** D-006  
**Requirement Affected:** Input Validation  
**Severity:** Medium  

## Summary  
System accepts long instructions exceeding 200 characters without validation.

---

# 🐞 BUG-007
**Title:** Duplicate pickup dates allowed  
**GitHub Link:** D-007  
**Requirement Affected:** Scheduling – Duplicate Prevention  
**Severity:** Medium  

## Summary  
User can schedule multiple pickups on the same date.

---

# 🐞 BUG-008
**Title:** Menu bar expands uncontrollably on small screen sizes  
**GitHub Link:** D-008  
**Requirement Affected:** Responsive Design  
**Severity:** Major  

## Summary  
When the viewport width shrinks, the menu expands vertically and covers the entire screen.

---

# 🐞 BUG-009
**Title:** Low-contrast text violates WCAG 2.1 AA  
**GitHub Link:** D-009  
**Requirement Affected:** Accessibility – Contrast  
**Severity:** Major  

## Summary  
Lighthouse audit reports insufficient text-to-background contrast.

---

# 🐞 BUG-010
**Title:** Layout breaks at 200% zoom  
**GitHub Link:** D-010  
**Requirement Affected:** Zoom & Reflow (WCAG 2.1 AA)  
**Severity:** Medium  

## Summary  
At 200% zoom, menu enlarges excessively and hides main content.

---

# 🐞 BUG-011
**Title:** Missing alt text on Awareness page images  
**GitHub Link:** D-011  
**Requirement Affected:** Accessibility – Alt Text  
**Severity:** Medium  

## Summary  
Meaningful images on the Awareness page lack descriptive alt attributes.

---

# ➕ **ADDITIONAL PROFESSIONAL BUGS ADDED (NOT IN YOUR LIST)**

---

# 🐞 BUG-012
**Title:** Registration form does not validate password strength  
**GitHub Link:** D-012  
**Severity:** High  
**Requirement:** Security – Password Standards  

## Summary  
Users can register using weak passwords like “12345”, violating security requirements.

---

# 🐞 BUG-013
**Title:** Pickup request map auto-location fails on slow networks  
**GitHub Link:** D-013  
**Severity:** Medium  
**Requirement:** Location Detection  

## Summary  
Map location does not load when internet speed is poor; system remains stuck on a loading spinner.

---

# 🐞 BUG-014
**Title:** Logout button does not clear session data  
**GitHub Link:** D-014  
**Severity:** High  
**Requirement:** Session Management  

## Summary  
After logout, the user can press the browser **Back** button and regain access to protected pages.

---

# 🐞 BUG-015
**Title:** Awareness page images load very slowly due to unoptimized media  
**GitHub Link:** D-015  
**Severity:** Low  
**Requirement:** Performance Optimization  

## Summary  
Images are not compressed and exceed 1MB, causing slow loading.

---

# 🐞 BUG-016
**Title:** Form fields do not show inline error messages  
**GitHub Link:** D-016  
**Severity:** Medium  
**Requirement:** Usability – Form Validation UI  

## Summary  
Validation errors only appear in the console, not visually on the UI.

---

# 🐞 BUG-017
**Title:** Profile picture upload accepts unsupported file types  
**GitHub Link:** D-017  
**Severity:** Medium  
**Requirement:** File Upload Validation  

## Summary  
System accepts .exe, .zip, and other invalid file formats during avatar upload.

---

# 🐞 BUG-018
**Title:** Pickup history table does not paginate after 10+ records  
**GitHub Link:** D-018  
**Severity:** Low  
**Requirement:** UI – Data Listing  

## Summary  
List keeps growing indefinitely, breaking layout and performance.

---

# 🐞 BUG-019
**Title:** “Forgot Password” feature does not send reset email  
**GitHub Link:** D-019  
**Severity:** Critical  
**Requirement:** Password Recovery  

## Summary  
Reset email endpoint returns 200 OK but no email is actually delivered.

---

# 🐞 BUG-020
**Title:** Awareness page article titles overlap images on mobile view  
**GitHub Link:** D-020  
**Severity:** High  
**Requirement:** Responsive Design  

## Summary  
Text overlays image content, making both unreadable.

