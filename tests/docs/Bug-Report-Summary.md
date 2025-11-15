# 🐞 CleanCity Bug Report Summary 

**Project:** CleanCity – Waste Pickup Scheduler  
**Version:** 1.0  
**Prepared by:** QA Team  
**Date:** 18 November 2025 

---

## 🔍 Overview

This document provides a summary of all defects identified during manual and automated testing of the CleanCity application.  

## ✅ Expected Behaviors

1. Allow users to schedule waste pickup requests with valid dates, waste types, and instructions.  

## 🐛 Reported Bugs

### 🐞 BUG-001
**Title:** Profile shows email username instead of Full Name after registration  
**GitHub Link:** D-001 
**Requirement Affected:** User Registration – Profile Display  
**Severity:** Comestic  
**Environment:** Development, Google Chrome, Windows 10  

#### Summary
After registering a new user with a proper Full Name, the profile page displays the username portion of the email (e.g., `user1` from `newuser@test.com`) instead of the Full Name (`New Test User`) provided during registration. This may cause confusion for users, as the system does not reflect the actual name they entered.

#### Steps to Reproduce
1. Register a new user with:
   - **Full Name:** `New Test User`
   - **Email:** `newuser@test.com`
   - **Password:** `NewPass123`
2. Log in with the newly registered account.  
3. Navigate to the **User Profile** page.  
4. Observe that the profile shows the email username instead of the Full Name.

#### Expected Result
The profile page should display the **Full Name** entered during registration.

#### Actual Result
The profile page displays the **username derived from the email** instead of the Full Name.

---

### 🐞 BUG-002  
**Title:** Existing user can log in with a different password than the one used during registration  
**GitHub Link:** [D-002](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31)  
**Requirement Affected:** User Login – Authentication  
**Severity:** Critical  
**Environment:** Development, Google Chrome, Windows 10  

#### Summary
An existing user is able to log in using a completely different password than the one set during registration. This is a major security issue because it allows unauthorized access to accounts, bypassing the intended authentication mechanism.  

#### Steps to Reproduce
1. Register a new user with:  
   - Full Name: Test User  
   - Email: user1@test.com
   - Password: TestPass123  
2. Log out of the account.  
3. Attempt to log in using the same email but a completely different password (e.g., WrongPassword).  
4. Observe that the system allows login despite the incorrect password.  

#### Expected Result
The system should reject login attempts when the password does not match the one used during registration, displaying an error: "Invalid email or password."  

#### Actual Result
The system allows the user to log in even with a password different from the one set during registration.

---

### 🐞 BUG-003  
**Title:** System allows login with unregistered credentials  
**GitHub Link:** [D-003](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32)  
**Requirement Affected:** User Login – Authentication Validation  
**Severity:** Critical  
**Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system successfully logs in users even when the provided email and password do not belong to any registered account. This issue completely bypasses the authentication process and poses a severe security risk, as unauthorized users can gain access without registration.  

#### Steps to Reproduce
1. Open the login page.  
2. Enter credentials that do not exist in the system, for example:  
   - Email: nonexist@test.com  
   - Password: AnyPassword  
3. Click **Login**.  
4. Observe that the system logs the user in successfully.  

#### Expected Result
The system should validate user credentials against the database and display an error message:  
> “Invalid email or password.”  

#### Actual Result
The system allows login and grants access even though the credentials are not registered in the database.

---

### 🐞 BUG-004  
**Title:** Pick-up request submitted without user registration  
**GitHub Link:** [D-004](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33)  
**Requirement Affected:** Pick-up Request – User Authentication  
**Severity:** High  
**Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system allows a user to submit a waste pick-up request **without registering or logging in**, which violates the functional requirement that all pick-ups must be performed by authenticated users.

#### Steps to Reproduce
1. Open the CleanCity application.  
2. Navigate to the pick-up request form.  
3. Fill in valid pick-up details.  
4. Submit the request **without creating an account or logging in**.  

#### Expected Result
The system should **prevent submission** and prompt the user to register or log in before creating a pick-up request.  

#### Actual Result
The pick-up request is successfully submitted without any authentication.
---

### 🐞 BUG-005
**Title:** The pickup is scheduled even with invalid date 
**GitHub Link:** D-005 
**Requirement Affected:** Pickup Scheduling – Date Validation  
**Severity:** Medium  
**Environment:** Development, Google Chrome, Windows 10  

---

### **Summary:**  
The system allows users to schedule a pickup with an **invalid (past) date**, such as yesterday. This violates the intended scheduling rule that only **future dates** should be accepted. As a result, users can submit and confirm invalid pickup requests, leading to inconsistencies in the request management system.

---

### **Steps to Reproduce:**  
1. Navigate to the **Pickup Request** form.  
2. Enter the following details:  
   - **Date:** Yesterday’s date  
   - **Waste Type:** General  
   - **Location:** Nairobi 
   - **Instructions:** “Please ring doorbell”  
3. Submit the request form.  

---

### **Expected Result:**  
The system should **not allow scheduling for past dates** and must display a **validation message** stating that only future dates are valid for scheduling.  

---

### **Actual Result:**  
The system **accepts the request with a past date**, allowing an invalid pickup to be scheduled.  

---

# 🐞 BUG-006

**Title:** System allows submission of pickup request with instructions exceeding 200 characters  
**GitHub Link:** [D-006](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41) 
**Requirement Affected:** Pickup Request Input Validation  
**Severity:** Medium  
**Environment:** Development, Google Chrome, Windows 10  

## Summary
When a user submits a pickup request with instructions longer than 200 characters, the system accepts the request without any validation or truncation. This can lead to potential data quality issues and display problems in the UI, as the system is not enforcing the expected character limit.  

## Steps to Reproduce
1. Navigate to the Pickup Request form.  
2. Enter a very long text (>200 characters) in the Instructions field.  
3. Submit the request.  
4. Observe that the system successfully accepts the request without errors.  

## Expected Result
The system should either truncate the instructions to 200 characters or display an error message preventing submission of overly long text.  

## Actual Result
The pickup request is successfully submitted with the full text exceeding 200 characters.  

---
### 🐞 BUG-007
**Title:** System allows scheduling multiple pickups for the same date  
**GitHub Link:** [D-007](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42)  
**Requirement Affected:** Pickup Scheduling – Prevent Duplicate Dates  
**Severity:** Medium  
**Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system is supposed to prevent scheduling multiple pickups on the same date. However, users can currently add two or more pickups with the same date, which may lead to operational confusion and duplicate service requests.

#### Steps to Reproduce
1. Log in to the system as a user.  
2. Schedule a pickup for a specific date (e.g., `2025-11-15`).  
3. Attempt to schedule another pickup for the **same date**.  
4. Observe that the system allows the second pickup to be created.  

#### Expected Result
The system should **prevent creating duplicate pickups** for the same date and display an error or validation message.

#### Actual Result
The system allows **two or more pickups** to be scheduled on the same date.


---

### 🐞 BUG-008  
**Title:** Menu bar expands excessively when resizing window, hiding all other content 
**GitHub Link:** [D-008](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) 
**Requirement Affected:**  Responsive Design  
**Severity:** Major   
**Environment:** Chrome / Desktop 
**Type:** Non-Functional – Usability/Compatibility 

#### Summary 
When the browser window is resized to smaller widths, the menu bar grows vertically and occupies the entire screen. No page content is visible at the smallest sizes.

#### Steps to Reproduce 
1. Open the application in a desktop browser.  
2. Slowly resize the browser window horizontally.  
3. Observe the menu bar increasing in size and taking over the entire viewport.

#### Expected Result 
The layout should adapt proportionally. The menu should collapse into a hamburger menu or shrink, and page content should remain visible.

#### Actual Result 
Menu bar expands uncontrollably, blocking all other content on small window sizes.

---

### 🐞 BUG-009  
**Title:** Low-contrast text fails WCAG 2.1 AA contrast requirements  
**GitHub Link:[D-009](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) 
**Requirement Affected:** Accessibility – WCAG 2.1 AA 
**Severity:** Major  
**Environment:** (Lighthouse Audit) Development, Google Chrome, Windows 10   
**Type:** Non-Functional – Accessibility / Usability  

---

#### Summary
The Lighthouse Accessibility audit identifies several UI elements with insufficient contrast between text and background colors. This makes text difficult to read for many users and violates WCAG 2.1 AA contrast standards (minimum 4.5:1 for normal text).

---

#### Steps to Reproduce
1. Open the application in Chrome.  
2. Open **DevTools → Lighthouse**.  
3. Run an **Accessibility** audit.  
4. Scroll to the **Contrast** section.  
5. Observe the list of elements flagged as failing contrast requirements.

---

#### Expected Result
All text and UI elements should meet WCAG 2.1 AA contrast ratios:  
- Normal text ≥ **4.5:1**  
- Large text / UI components ≥ **3:1**  
Text should remain clearly readable against its background under all conditions.

---

#### Actual Result
Lighthouse reports: *“Background and foreground colors do not have a sufficient contrast ratio.”*  

Manual checks were done to confirm that the contrast ratios for these elements fall below WCAG AA thresholds.

---

🐞 BUG-010  
Title: Layout breaks at 200% zoom — menu enlarges and hides content  
GitHub Link: [D-010](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59)  
Requirement Affected: Accessibility – Zoom & Reflow (WCAG 2.1 AA, 1.4.4)  
Severity: Medium  
Environment: Development, Google Chrome, Windows 10  

## Summary  
When the browser zoom level is increased to **200%**, the menu enlarges disproportionately and pushes all other page content out of view. This causes the page to become unusable at high zoom levels, failing WCAG 2.1 AA accessibility requirements.  

## Steps to Reproduce  
1. Open the system in Google Chrome.  
2. Navigate to any page containing the main menu.  
3. Increase the browser zoom level to **200%** (Ctrl + +).  
4. Observe the layout behavior.  

## Expected Result  
At 200% zoom, the layout should reflow properly, remain readable, and keep all content visible and accessible without overlap or loss of functionality.  

## Actual Result  
The menu becomes excessively enlarged, and all other page content becomes hidden or pushed off-screen, making the page unusable at 200% zoom.  

---

🐞 BUG-011  
Title: Missing alt text for meaningful images on Awareness page  
GitHub Link: [D-011](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/60) 
Requirement Affected: Accessibility – Image Alt Text (WCAG 2.1 AA, 1.1.1)  
Severity: Medium  
Environment: Development, Google Chrome, Windows 10  

## Summary  
The Awareness page contains meaningful images that do not include descriptive **alt** attributes. This violates accessibility guidelines and prevents screen reader users from understanding the purpose and context of the images.

## Steps to Reproduce  
1. Navigate to the Awareness page.  
2. Inspect the images displayed on the page using browser dev tools.  
3. Check the HTML for each image and confirm the presence of the **alt** attribute.  
4. Observe that some images have missing or empty alt text.

## Expected Result  
All meaningful images should contain clear, descriptive **alt text** that conveys the purpose or information represented by the image.

## Actual Result  
Several meaningful images on the Awareness page are missing **alt attributes**, resulting in inaccessible content for users relying on assistive technologies.

