# 🐞 CleanCity Bug Report Summary 

**Project:** CleanCity – Waste Pickup Scheduler  
**Version:** 1.0  
**Prepared by:** QA Team  
**Date:** 18 November 2025 

---

## 🔍 Overview

This document provides a summary of all defects identified during manual and automated testing of the CleanCity application.  

## ✅ Expected Behaviors

# 🐞 CLEAN CITY — COMPLETE BUG REPORT LIST (16 BUGS)

---

## 🐞 BUG-001  
**Title:** Profile shows email username instead of Full Name after registration  
**GitHub Link:** D-001  
**Requirement Affected:** User Registration – Profile Display  
**Severity:** Cosmetic  
**Environment:** Development, Google Chrome, Windows 10  

### Summary  
The profile page displays the email username instead of the Full Name entered during registration, causing confusion and reducing profile accuracy.

### Steps to Reproduce  
1. Register a new user with:  
   - Full Name: New Test User  
   - Email: newuser@test.com  
   - Password: NewPass123  
2. Log in.  
3. Open the User Profile page.  

### Expected Result  
The profile page should display the Full Name entered during registration.

### Actual Result  
The system displays the username portion of the email instead of the Full Name.

---

## 🐞 BUG-002  
**Title:** Existing user can log in using an incorrect password  
**GitHub Link:** D-002  
**Requirement Affected:** User Login – Authentication  
**Severity:** Critical  
**Environment:** Development, Google Chrome, Windows 10  

### Summary  
The system allows users to log in with any incorrect password, bypassing the authentication mechanism.

### Steps to Reproduce  
1. Register a user:  
   - Email: user1@test.com  
   - Password: TestPass123  
2. Log out.  
3. Attempt login with a wrong password (e.g., WrongPassword).  

### Expected Result  
System should reject incorrect credentials and display: **“Invalid email or password.”**

### Actual Result  
Login succeeds even with a completely incorrect password.

---

## 🐞 BUG-003  
**Title:** System logs in unregistered users  
**GitHub Link:** D-003  
**Requirement Affected:** User Login – Authentication Validation  
**Severity:** Critical  
**Environment:** Development, Google Chrome, Windows 10  

### Summary  
Users can log in with credentials that do not exist in the system, bypassing all authentication checks.

### Steps to Reproduce  
1. Open login page.  
2. Enter:  
   - Email: nonexist@test.com  
   - Password: AnyPassword  
3. Click Login.  

### Expected Result  
System must reject unregistered credentials.

### Actual Result  
System logs in the nonexistent user successfully.

---

## 🐞 BUG-004  
**Title:** Pickup request submitted without authentication  
**GitHub Link:** D-004  
**Requirement Affected:** Pickup Request – User Authentication  
**Severity:** High  
**Environment:** Development, Google Chrome, Windows 10  

### Summary  
The system allows pickup requests to be submitted by unauthenticated users, violating business rules.

### Steps to Reproduce  
1. Open CleanCity app.  
2. Navigate to Pickup Request form.  
3. Enter valid details.  
4. Submit without logging in.  

### Expected Result  
User must be required to log in before submitting a pickup request.

### Actual Result  
Pickup request is submitted successfully without authentication.

---

## 🐞 BUG-005  
**Title:** System allows scheduling pickup with a past date  
**GitHub Link:** D-005  
**Requirement Affected:** Pickup Scheduling – Date Validation  
**Severity:** Medium  
**Environment:** Development, Google Chrome, Windows 10  

### Summary  
Pickup requests can be scheduled using past dates, creating invalid service jobs.

### Steps to Reproduce  
1. Open Pickup Request form.  
2. Enter yesterday’s date.  
3. Submit form.  

### Expected Result  
System should reject past dates and display a validation error.

### Actual Result  
System accepts the request and schedules a pickup for a past date.

---

## 🐞 BUG-006  
**Title:** System accepts instructions exceeding 200 characters  
**GitHub Link:** D-006  
**Requirement Affected:** Pickup Request – Input Validation  
**Severity:** Medium  
**Environment:** Development, Google Chrome, Windows 10  

### Summary  
Instruction text longer than 200 characters is accepted without validation or truncation.

### Steps to Reproduce  
1. Open Pickup Request form.  
2. Enter a very long instruction (>200 characters).  
3. Submit.  

### Expected Result  
System should restrict instructions to 200 characters.

### Actual Result  
Request is submitted with the full, overly long text.

---

## 🐞 BUG-007  
**Title:** System allows multiple pickups for the same date  
**GitHub Link:** D-007  
**Requirement Affected:** Pickup Scheduling – Prevent Duplicate Dates  
**Severity:** Medium  
**Environment:** Development, Google Chrome, Windows 10  

### Summary  
Users can schedule multiple pickups on the same date, leading to redundant service requests.

### Steps to Reproduce  
1. Log in.  
2. Schedule a pickup for date X.  
3. Schedule another pickup for the same date.  

### Expected Result  
System should block duplicate pickup dates per user.

### Actual Result  
User can schedule multiple pickups on the same date.

---

## 🐞 BUG-008  
**Title:** Menu bar expands excessively when resizing window  
**GitHub Link:** D-008  
**Requirement Affected:** Responsive Design  
**Severity:** Major  
**Environment:** Chrome Desktop  
**Type:** Non-Functional – Usability/Compatibility  

### Summary  
When resizing the browser window, the menu bar grows vertically and covers the entire content.

### Steps to Reproduce  
1. Open the app.  
2. Shrink browser width gradually.  
3. Observe menu behavior.  

### Expected Result  
Menu should collapse or adapt without hiding page content.

### Actual Result  
Menu expands uncontrollably and blocks all visible content.

---

## 🐞 BUG-009  
**Title:** Low-contrast text fails WCAG 2.1 AA  
**GitHub Link:** D-009  
**Requirement Affected:** Accessibility – WCAG Contrast  
**Severity:** Major  
**Environment:** Lighthouse Audit, Google Chrome  

### Summary  
Several UI elements have insufficient contrast between background and text, failing WCAG 2.1 AA requirements.

### Steps to Reproduce  
1. Open Chrome DevTools → Lighthouse.  
2. Run Accessibility audit.  
3. Review the contrast section.  

### Expected Result  
All text should meet minimum 4.5:1 contrast ratio.

### Actual Result  
Multiple elements fail contrast requirements.

---

## 🐞 BUG-010  
**Title:** Layout breaks at 200% zoom  
**GitHub Link:** D-010  
**Requirement Affected:** Accessibility – Zoom & Reflow  
**Severity:** Medium  
**Environment:** Dev, Google Chrome  

### Summary  
At 200% zoom, the menu enlarges and hides all content, breaking accessibility standards.

### Steps to Reproduce  
1. Open the app.  
2. Zoom to 200%.  

### Expected Result  
Content should remain visible and accessible at high zoom levels.

### Actual Result  
Menu covers all content, making the page unusable.

---

## 🐞 BUG-011  
**Title:** Missing alt text for meaningful images  
**GitHub Link:** D-011  
**Requirement Affected:** Accessibility – Alt Text  
**Severity:** Medium  
**Environment:** Development, Google Chrome  

### Summary  
Several meaningful images on the Awareness page do not have descriptive alt attributes.

### Steps to Reproduce  
1. Go to the Awareness page.  
2. Inspect images via DevTools.  

### Expected Result  
All meaningful images should have descriptive alt text.

### Actual Result  
Images are missing alt attributes, making them inaccessible.

---

---

## 🐞 BUG-012  
**Title:** Waste type filter returns incorrect results  
**GitHub Link:** D-012  
**Requirement Affected:** Pickup History – Filtering  
**Severity:** High  

### Summary  
Filtering pickup history by waste type returns unrelated entries.

### Steps to Reproduce  
1. Go to Pickup History.  
2. Select waste type: “Plastic”.  

### Expected Result  
Only plastic-related pickups should appear.

### Actual Result  
Entries from all waste types still appear.

---

## 🐞 BUG-013  
**Title:** Pickup history list pagination not working  
**GitHub Link:** D-013  
**Requirement Affected:** Pickup History – Navigation  
**Severity:** Medium  

### Summary  
Pagination buttons do not load new pages; the list remains unchanged.

### Steps to Reproduce  
1. Open Pickup History.  
2. Click “Next Page”.  

### Expected Result  
Next set of pickup records should load.

### Actual Result  
Same page remains displayed with no change.

---

## 🐞 BUG-014  
**Title:** Profile picture upload returns 500 server error  
**GitHub Link:** D-014  
**Requirement Affected:** User Profile – Media Upload  
**Severity:** High  

### Summary  
Uploading a valid image triggers a 500 Internal Server Error.

### Steps to Reproduce  
1. Go to Profile.  
2. Upload JPEG or PNG file.  

### Expected Result  
Image should upload successfully and appear in the profile.

### Actual Result  
A 500 server error is returned.

---

## 🐞 BUG-015  
**Title:** Map fails to load under slow internet connections  
**GitHub Link:** D-015  
**Requirement Affected:** Pickup Location – Map Rendering  
**Severity:** Medium  

### Summary  
The embedded map fails to load when the internet connection is slow, leaving a blank section.

### Steps to Reproduce  
1. Throttle network to “Slow 3G”.  
2. Open Pickup Request page.  

### Expected Result  
Map should load with a fallback or spinner.

### Actual Result  
Map fails to load completely.

---

## 🐞 BUG-016  
**Title:** Pickup confirmation email not sent  
**GitHub Link:** D-016  
**Requirement Affected:** Notifications – Pickup Confirmation  
**Severity:** High  

### Summary  
Users do not receive confirmation emails after scheduling a pickup.

### Steps to Reproduce  
1. Submit a pickup request.  
2. Check email inbox.  

### Expected Result  
A confirmation email should be sent immediately.

### Actual Result  
No email is received.

