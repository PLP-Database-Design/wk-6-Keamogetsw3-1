# 🐞 CleanCity Bug Report Summary

**Project:** CleanCity – Waste Pickup Scheduler  
**Version:** 1.0  
**Prepared by:** QA Team  
**Date:** 18 November 2025  

---

## 🔍 Overview

This document provides a summary of all defects identified during manual and automated testing of the CleanCity application.

---

## ✅ Expected Behaviors

1. Allow users to register and log in to schedule waste pickup requests with valid dates, waste types, and instructions.  
2. Allow admins to log in.

---

## 🐛 Reported Bugs

### 🐞 BUG-001
- **Title:** Profile shows email username instead of Full Name after registration  
- **GitHub Link:** [D001](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/28)  
- **Requirement Affected:** User Registration – Profile Display  
- **Severity:** Cosmetic  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
After registering a new user with a proper Full Name, the profile page displays the username portion of the email (e.g., `user1` from `newuser@test.com`) instead of the Full Name (`New Test User`) provided during registration. This may cause confusion for users, as the system does not reflect the actual name they entered.

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.
2. Click on Register to register a new profile
3.  Register a new user with:  
   - **Full Name:** `New Test User`  
   - **Email:** `newuser@test.com`  
   - **Password:** `NewPass123`  
3. Log in with the newly registered account.  
4. Navigate to the **User Profile** page.  
5. Observe that the profile shows the email username instead of the Full Name.

#### Expected Result
The profile page should display the **Full Name** entered during registration.

#### Actual Result
The profile page displays the **username derived from the email** instead of the Full Name.

---

### 🐞 BUG-002
- **Title:** Existing user can log in with a different password than the one used during registration  
- **GitHub Link:** [#31](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31)  
- **Requirement Affected:** User Login – Authentication  
- **Severity:** Critical  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
An existing user is able to log in using a completely different password than the one set during registration. This is a major security issue because it allows unauthorized access to accounts.

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.
2. Click on Register to register a new profile
3.  Register a new user:  
   - Full Name: Test User  
   - Email: user1@test.com  
   - Password: TestPass123  
4. Log out.  
5. Attempt to log in using the same email but a different password (e.g., WrongPassword).  
6. Observe the system allows login despite the incorrect password.

#### Expected Result
The system should reject login attempts when the password does not match the one used during registration, displaying an error: "Invalid email or password."

#### Actual Result
The system allows login even with a different password.

---

### 🐞 BUG-003
- **Title:** System allows login with unregistered credentials  
- **GitHub Link:** [#32](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32)  
- **Requirement Affected:** User Login – Authentication Validation  
- **Severity:** Critical  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system logs in users even when the email and password do not belong to an unregistered account, bypassing authentication and posing a severe security risk.

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.
2. Open the login page.  
3. Enter unregistered credentials:  
   - Email: nonexist@test.com  
   - Password: AnyPassword  
4. Click **Login**.  
5. Observe the system logs in successfully.

#### Expected Result
The system should validate credentials and display:  
> “Invalid email or password.”

#### Actual Result
The system allows login and grants access with unregistered credentials.

---

### 🐞 BUG-004
- **Title:** Pick-up request submitted without user registration  
- **GitHub Link:** [#33](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33)  
- **Requirement Affected:** Pick-up Request – User Authentication  
- **Severity:** Critical  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users can submit a pick-up request **without logging in**, violating the requirement that all pick-ups must be authenticated.

#### Steps to Reproduce
1. Open the application.  
2. Navigate to the pick-up request form.  
3. Fill in valid details.  
4. Submit **without logging in**.  

#### Expected Result
Submission should be blocked and prompt the user to log in.

#### Actual Result
The pick-up request is submitted successfully without authentication.

---

### 🐞 BUG-005
- **Title:** Pickup is scheduled even with invalid date  
- **GitHub Link:** [D005](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/34) 
- **Requirement Affected:** Pickup Scheduling – Date Validation  
- **Severity:** Major 
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system allows scheduling pickups with **past dates**, violating scheduling rules.

#### Steps to Reproduce
1.
2. Navigate to the Pickup Request form.  
3. Enter:  
   - **Date:** Yesterday  
   - **Waste Type:** General  
   - **Location:** Nairobi  
   - **Instructions:** “Please ring doorbell”  
4. Submit the form.

#### Expected Result
Past dates should be rejected with a validation message.

#### Actual Result
The system accepts past dates and schedules the pickup.

---

### 🐞 BUG-006
- **Title:** System allows submission of pickup request with instructions exceeding 200 characters  
- **GitHub Link:** [#41](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41)  
- **Requirement Affected:** Pickup Request Input Validation  
- **Severity:** Minor 
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Instructions longer than 200 characters are accepted without validation, leading to potential data and UI issues.

#### Steps to Reproduce
1. Open Cleancity application
2. Log in and go to schedule pick up
3. Enter required info then instructions >200 characters.  
4. Submit the request.  
5. Observe that the system accepts the input.

#### Expected Result
Reject instructions exceeding 200 characters or truncate automatically.

#### Actual Result
Request is accepted without error.

---

### 🐞 BUG-007
- **Title:** System allows scheduling multiple pickups for the same date  
- **GitHub Link:** [#42](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42)  
- **Requirement Affected:** Pickup Scheduling – Prevent Duplicate Dates  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Duplicate pickups on the same date are allowed, causing potential operational confusion.

#### Steps to Reproduce
1. Schedule a pickup for a date.  
2. Schedule another pickup for the same date.  
3. Observe the system allows both.

#### Expected Result
Prevent duplicate pickups and show validation message.

#### Actual Result
Multiple pickups for the same date are accepted.

---

### 🐞 BUG-008
- **Title:** Menu bar expands excessively when resizing window, hiding content  
- **GitHub Link:** [D-008](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55)  
- **Requirement Affected:** Responsive Design  
- **Severity:** Major  
- **Environment:** Chrome / Desktop  
- **Type:** Non-Functional – Usability/Compatibility  

#### Summary
On smaller widths, the menu bar grows vertically and hides page content.

#### Steps to Reproduce
1. Open app in a desktop browser.  
2. Resize horizontally.  
3. Observe menu bar expanding and blocking content.

#### Expected Result
Menu should collapse or shrink, keeping content visible.

#### Actual Result
Menu expands uncontrollably, hiding all content.

---

### 🐞 BUG-009
- **Title:** Low-contrast text fails WCAG 2.1 AA  
- **GitHub Link:** D-009  
- **Requirement Affected:** Accessibility – WCAG Contrast  
- **Severity:** Major  
- **Environment:** Lighthouse Audit, Google Chrome  

#### Summary
Several UI elements do not meet the minimum contrast ratio.

#### Steps to Reproduce
1. Run Lighthouse Accessibility audit.  
2. Review contrast section.

#### Expected Result
All text must meet 4.5:1 contrast ratio.

#### Actual Result
Multiple elements fail the requirement.

---

### 🐞 BUG-010
- **Title:** Layout breaks at 200% zoom  
- **GitHub Link:** D-010  
- **Requirement Affected:** Accessibility – Zoom & Reflow  
- **Severity:** Medium  
- **Environment:** Dev, Google Chrome  

#### Summary
At 200% zoom, the menu covers content and breaks accessibility.

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Press `Ctrl` and `+` (Windows Laptop) to zoom in until the page reaches 200% zoom.  
3. Observe how the menu overlaps the main content. 

#### Expected Result
Content remains visible and accessible.

#### Actual Result
Menu blocks all content.

---

### 🐞 BUG-011
- **Title:** Missing alt text for meaningful images  
- **GitHub Link:** D-011  
- **Requirement Affected:** Accessibility – Alt Text  
- **Severity:** Medium  
- **Environment:** Development, Google Chrome  

#### Summary
Images on the Awareness page lack descriptive alt attributes.

#### Steps to Reproduce
1. Inspect images on Awareness page via DevTools.

#### Expected Result
All meaningful images have descriptive alt text.

#### Actual Result
Alt text missing, reducing accessibility.

---

### 🐞 BUG-012
- **Title:** Waste type filter returns incorrect results  
- **GitHub Link:** D-012  
- **Requirement Affected:** Pickup History – Filtering  
- **Severity:** High  

#### Summary
Filtering by waste type shows unrelated entries.

#### Steps to Reproduce
1. Open Pickup History.  
2. Select “Plastic”.

#### Expected Result
Only plastic pickups displayed.

#### Actual Result
All waste types still appear.

---

### 🐞 BUG-013
- **Title:** Pickup history list pagination not working  
- **GitHub Link:** D-013  
- **Requirement Affected:** Pickup History – Navigation  
- **Severity:** Medium  

#### Summary
Pagination buttons do not load new pages.

#### Steps to Reproduce
1. Click “Next Page” in Pickup History.

#### Expected Result
Next set of records loads.

#### Actual Result
Same page remains displayed.

---

### 🐞 BUG-014
- **Title:** Profile picture upload returns 500 server error  
- **GitHub Link:** D-014  
- **Requirement Affected:** User Profile – Media Upload  
- **Severity:** High  

#### Summary
Uploading an image triggers 500 Internal Server Error.

#### Steps to Reproduce
1. Upload JPEG/PNG file in Profile.

#### Expected Result
Image uploads successfully.

#### Actual Result
Server returns 500 error.

---

### 🐞 BUG-015
- **Title:** Map fails to load under slow internet connections  
- **GitHub Link:** D-015  
- **Requirement Affected:** Pickup Location – Map Rendering  
- **Severity:** Medium  

#### Summary
Map fails to load on slow networks.

#### Steps to Reproduce
1. Throttle network to “Slow 3G”.  
2. Open Pickup Request page.

#### Expected Result
Map loads with fallback or spinner.

#### Actual Result
Map fails to load.

---

### 🐞 BUG-016
- **Title:** Pickup confirmation email not sent  
- **GitHub Link:** D-016  
- **Requirement Affected:** Notifications – Pickup Confirmation  
- **Severity:** High  

#### Summary
Confirmation emails are not sent after scheduling a pickup.

#### Steps to Reproduce
1. Submit a pickup request.  
2. Check inbox.

#### Expected Result
Confirmation email sent immediately.

#### Actual Result
No email received.

---

### 🐞 BUG-017
- **Title:** To be added by Keamo

---

### 🐞 BUG-018
- **Title:** To be added by Keamo
