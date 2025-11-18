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
- **GitHub Link:** [D002](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31)  
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
- **GitHub Link:** [D003](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32)  
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
- **GitHub Link:** [D004](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33)  
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
- **Title:** User cannot view past and current pickup request history  
- **GitHub Link:** [D012](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/61)  
- **Requirement Affected:** Pickup Request – History Display  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
When a user navigates to their dashboard, the system fails to display all past and current pickup requests with their details. Users are unable to verify previous pickups or track ongoing requests, affecting usability and user experience.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Observe that no past or current pickup requests are displayed.  

#### Expected Result
The system should display all past and current pickup requests with full details.  

#### Actual Result
User cannot view all past and current pickup requests with details.

---

### 🐞 BUG-013
- **Title:** Completed and cancelled pickup requests are not shown in dashboard  
- **GitHub Link:** [D013](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/62)  
- **Requirement Affected:** Pickup Request – History Display  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Completed and cancelled pickup requests fail to appear in the user's dashboard. This prevents users from confirming whether their requests were completed or cancelled.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Observe that completed and cancelled requests are missing.  

#### Expected Result
Completed and cancelled requests should be shown correctly in the dashboard.  

#### Actual Result
Completed and cancelled requests are not shown at all.

---

### 🐞 BUG-014
- **Title:** User cannot cancel a pending pickup request  
- **GitHub Link:** [D014](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/63)  
- **Requirement Affected:** Pickup Request – Cancellation  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users are unable to cancel a pickup request that is still pending. This prevents users from managing or updating their scheduled pickups.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Attempt to cancel a pending pickup request.  
5. Observe that the system does not allow cancellation.  

#### Expected Result
Pending requests should be cancellable, and their status should update to “Cancelled.”  

#### Actual Result
User cannot cancel a pending pickup request.

---

### 🐞 BUG-015
- **Title:** Completed or cancelled requests can potentially be cancelled again  
- **GitHub Link:** [D015](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/64)  
- **Requirement Affected:** Pickup Request – Cancellation Rules  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system does not prevent double cancellation for completed or already cancelled requests, which may cause inconsistencies in request status tracking.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Attempt to cancel a request that is already completed or cancelled.  

#### Expected Result
System should prevent double cancellation and notify the user.  

#### Actual Result
N/A (Test could not confirm prevention of double cancellation).

---

### 🐞 BUG-016
- **Title:** User cannot modify pickup details at least 24 hours before schedule  
- **GitHub Link:** [D016](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/65)  
- **Requirement Affected:** Pickup Request – Modification  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users are unable to update pickup request details even when they are allowed to modify them 24 hours before the scheduled time.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Attempt to modify a pending pickup request scheduled more than 24 hours in the future.  

#### Expected Result
User should be able to successfully update pickup details.  

#### Actual Result
Modification is not possible.

---

### 🐞 BUG-017
- **Title:** System allows modification within 24 hours of scheduled pickup  
- **GitHub Link:** [D017](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/66)  
- **Requirement Affected:** Pickup Request – Modification Restriction  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system fails to enforce the 24-hour restriction for modifying scheduled pickups, potentially causing logistical issues.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Attempt to modify a pickup request scheduled within the next 24 hours.  

#### Expected Result
System should prevent modification and display a warning message.  

#### Actual Result
N/A (Modification restriction is not enforced).

---

### 🐞 BUG-018
- **Title:** Pickup status not displayed correctly  
- **GitHub Link:** [D018](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/67)  
- **Requirement Affected:** Pickup Request – Status Display  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system fails to display the correct status (Pending, Confirmed, Completed, or Cancelled) for each pickup request, making it difficult for users to track their requests.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Observe the status of each pickup request.  

#### Expected Result
The system should correctly display each request’s status.  

#### Actual Result
Pickup status is not listed or visible.

---

### 🐞 BUG-019
- **Title:** Pickup status does not update dynamically after completion/cancellation  
- **GitHub Link:** [D019](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/68)  
- **Requirement Affected:** Pickup Request – Status Update  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
After a pickup request is completed or cancelled, the system does not update the status dynamically. Users cannot see real-time updates on their request status.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Complete or cancel a pickup request.  
5. Observe that the request status does not reflect the change.  

#### Expected Result
The status should update immediately to reflect completion or cancellation.  

#### Actual Result
Pickup status is not listed or visible.

------

### 🐞 BUG-020
- **Title:** Pickup request status does not update in real-time  
- **GitHub Link:** [D020](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/69)  
- **Requirement Affected:** Waste Management Requirements – Request Tracking  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system fails to update the status of pickup requests dynamically. Users must manually refresh the page to see the latest status, which can cause confusion and delay in tracking their requests.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Observe the status of a pickup request while it changes (e.g., from Pending to Confirmed).  

#### Expected Result
Status of each pickup request should update dynamically without requiring page refresh.  

#### Actual Result
Status does not update in real-time; the page must be refreshed to see changes.

---

### 🐞 BUG-021
- **Title:** Users do not receive notifications for pickup request status changes  
- **GitHub Link:** [D021](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/70)  
- **Requirement Affected:** Waste Management Requirements – Request Tracking  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users are not receiving any notifications (email, SMS, or in-app) when the status of their pickup requests changes. This can lead to missed pickups and significantly affects user experience.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Schedule a pickup request or use an existing request.  
4. Change the status of the pickup (e.g., Confirmed or Completed).  
5. Observe that the user does not receive any notification.  

#### Expected Result
Users should receive notifications whenever the status of a pickup request changes.  

#### Actual Result
Users do not receive notifications for status changes.

---

### 🐞 BUG-022
- **Title:** Feedback not associated with completed pickup  
- **GitHub Link:** [D022](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/71)  
- **Requirement Affected:** Waste Management Requirements – Request Tracking  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users can submit feedback after a pickup is completed, but the feedback is not correctly associated with the corresponding completed pickup. This prevents proper tracking and reporting of user feedback.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Select a completed pickup request and submit feedback.  
5. Observe that the feedback is not linked to the completed pickup.  

#### Expected Result
Feedback should be stored and associated with the completed pickup request.  

#### Actual Result
Users can add feedback, but it is not associated with the completed pickup.


# CleanCity Bug Reports – Dashboard & Analytics Module

### 🐞 BUG-023
- **Title:** Dashboard does not display personalized information for logged-in users  
- **GitHub Link:** [D023](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/72)  
- **Requirement Affected:** Dashboard & Analytics Requirements  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The user dashboard fails to display personalized information such as recent pickup requests, upcoming scheduled pickups, achievement badges, and quick action buttons. This prevents users from accessing relevant information and negatively impacts the user experience.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Observe that no personalized information is displayed.  

#### Expected Result
The dashboard should show personalized content including recent pickups, upcoming pickups, achievement badges, and quick action buttons.  

#### Actual Result
Dashboard does not show any personalized information.

---

### 🐞 BUG-024
- **Title:** Environmental impact metrics not displayed on dashboard  
- **GitHub Link:** [D024](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/73)  
- **Requirement Affected:** Dashboard & Analytics Requirements  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The dashboard fails to calculate and display the user's environmental impact metrics, including total waste diverted, CO2 emissions saved, and trees equivalent saved. This prevents users from seeing meaningful analytics.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Observe that no environmental impact metrics are displayed.  

#### Expected Result
The dashboard should calculate and display total waste diverted, CO2 emissions saved, and trees equivalent saved.  

#### Actual Result
None of the impact metrics is shown.

---

### 🐞 BUG-025
- **Title:** Badges for achievements display incorrectly on dashboard  
- **GitHub Link:** [D025](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/74)  
- **Requirement Affected:** Dashboard & Analytics Requirements  
- **Severity:** Cosmetic  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
While badges are displayed on the dashboard, there may be minor presentation or association issues affecting how achievements appear to the user. This does not prevent users from seeing their achievements but may affect clarity or styling.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Dashboard**.  
4. Observe the display of achievement badges.  

#### Expected Result
Badges should be clearly displayed, associated correctly with achievements, and visually consistent.  

#### Actual Result
Badges are displayed on the dashboard, but minor issues may exist in presentation or association.



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




--

### 🐞 BUG-017
- **Title:** To be added by Keamo

---

### 🐞 BUG-018
- **Title:** To be added by Keamo
