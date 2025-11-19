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
---
### 🐞 BUG-026
- **Title:** Admins cannot create a blog post  
- **GitHub Link:** [D026](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/75)  
- **Requirement Affected:** Content Management Requirements – Blog System  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to create new blog posts. When attempting to save a new post, the system fails to store the blog content or display it in the blog list. This blocks content creation entirely.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to the **Blog System** section.  
4. Attempt to create a new blog post with title and content.  
5. Save the post and check the blog list.  

#### Expected Result
The blog post should be saved successfully and appear in the blog list.  

#### Actual Result
Admins cannot create a blog post; the system fails to save it.

---

### 🐞 BUG-027
- **Title:** Admins cannot edit an existing blog post  
- **GitHub Link:** [D027](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/76)  
- **Requirement Affected:** Content Management Requirements – Blog System  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to edit existing blog posts. Updates made to a blog post’s content are not saved or reflected on the blog page. This prevents proper content management and updates.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to the **Blog System** section.  
4. Select an existing blog post and attempt to edit the content.  
5. Save changes and check the blog page.  

#### Expected Result
Updated content should be saved and displayed correctly on the blog page.  

#### Actual Result
Admins cannot edit a blog post; changes are not saved.

---

### 🐞 BUG-028
- **Title:** Admins cannot delete a blog post  
- **GitHub Link:** [D028](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/77)  
- **Requirement Affected:** Content Management Requirements – Blog System  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to delete blog posts. When attempting to remove a post, it remains visible in the blog list, preventing proper content management.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to the **Blog System** section.  
4. Attempt to delete an existing blog post.  
5. Verify that the blog post is removed from the list.  

#### Expected Result
The blog post should be removed and no longer visible on the blog page.  

#### Actual Result
Admins cannot delete a blog post; it remains visible in the list.

---
### 🐞 BUG-029
- **Title:** Profile picture upload fails with server error  
- **GitHub Link:** [D029](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/78)  
- **Requirement Affected:** Community Features – Community Feed  
- **Severity:** Cosmetic  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
When users attempt to upload a profile picture, the system returns a 500 server error. While this prevents users from displaying a profile image in the community feed, it does not affect other profile or feed functionality.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Profile Settings**.  
4. Attempt to upload a profile picture (any valid image file).  
5. Observe that the upload fails and a 500 server error is returned.  

#### Expected Result
Users should be able to upload a profile picture successfully, and it should display correctly in the community feed.  

#### Actual Result
Uploading an image returns a 500 server error; the profile picture is not saved or displayed in the feed.

---

### 🐞 BUG-030
- **Title:** Users cannot follow or unfollow other community members  
- **GitHub Link:** [D030](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/79)  
- **Requirement Affected:** Community Features – Community Feed  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users are unable to follow or unfollow other community members. This limits social interaction within the community feed but does not affect core application functionality.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Community Feed** or another user's profile.  
4. Attempt to follow or unfollow a community member.  
5. Observe that the action fails.  

#### Expected Result
Users should be able to follow and unfollow other community members successfully.  

#### Actual Result
Users cannot follow or unfollow other community members.

---

### 🐞 BUG-031
- **Title:** News feed does not display latest community activities  
- **GitHub Link:** [D031](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/80)  
- **Requirement Affected:** Community Features – Community Feed  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The news feed fails to update and does not display the latest community activities, such as posts, likes, or comments from followed users. This affects the visibility of interactions but does not block core functionality.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in with a registered user account.  
3. Navigate to **Community Feed**.  
4. Observe whether the latest posts, likes, and comments from followed users are displayed.  

#### Expected Result
The news feed should show the latest activities from followed users, including posts, likes, and comments.  

#### Actual Result
News feed does not update or show the latest community activities.

---

### 🐞 BUG-032
- **Title:** Admins cannot approve, reject, or modify pickup requests  
- **GitHub Link:** [D032](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/81)  
- **Requirement Affected:** Administrative Functions Requirements – Request Management  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to approve, reject, or modify pickup requests. This blocks key administrative workflow, preventing requests from being processed efficiently.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to the **Pickup Requests** section.  
4. Attempt to approve, reject, or modify any pickup request.  
5. Observe that the action cannot be performed.  

#### Expected Result
Admins should be able to approve, reject, or modify any pickup request successfully.  

#### Actual Result
Admin cannot approve, reject, or modify pickup requests.

---

### 🐞 BUG-033
- **Title:** Admins cannot assign or update pickup dates and times  
- **GitHub Link:** [D033](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/82)  
- **Requirement Affected:** Administrative Functions Requirements – Request Management  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to assign or update pickup dates and times. This prevents proper scheduling of pickups and delays operations.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to the **Pickup Requests** section.  
4. Attempt to assign or update a pickup date/time for a request.  
5. Observe that changes are not saved.  

#### Expected Result
Admins should be able to set or update pickup dates and times successfully.  

#### Actual Result
Admin cannot assign or update pickup dates/times; changes are not saved.

---

### 🐞 BUG-034
- **Title:** Admins cannot filter or search pickup requests correctly  
- **GitHub Link:** [D034](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/83)  
- **Requirement Affected:** Administrative Functions Requirements – Request Management  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The filtering and search functionality in the Pickup Requests section does not return correct results based on criteria, reducing admin efficiency.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to **Pickup Requests**.  
4. Attempt to filter or search requests using specific criteria.  
5. Observe that the results are incorrect or incomplete.  

#### Expected Result
The system should return accurate filtered or searched results according to the selected criteria.  

#### Actual Result
Filtering/searching does not return correct results.

---

### 🐞 BUG-035
- **Title:** Admins cannot receive or reply to feedback  
- **GitHub Link:** [D035](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/84)  
- **Requirement Affected:** Administrative Functions Requirements – Request Management  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to receive or reply to feedback submitted by users. This blocks communication and reduces the effectiveness of the feedback system.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to the **Feedback** section.  
4. Attempt to receive or reply to user feedback.  
5. Observe that the system does not allow the actions.  

#### Expected Result
Admins should be able to receive and reply to feedback properly.  

#### Actual Result
Admin unable to receive or reply to feedback.

---
### 🐞 BUG-036
- **Title:** Admins cannot view all registered users  
- **GitHub Link:** [D036](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/85)  
- **Requirement Affected:** Administrative Functions Requirements – User Management  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to view the complete list of all registered users. Only partial or no user information is displayed, limiting administrative oversight.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to **User Management** or **Registered Users** section.  
4. Observe that the full list of registered users is not displayed.  

#### Expected Result
Admins should be able to view a complete list of all registered system users.  

#### Actual Result
Admin cannot view the complete list of registered users.

---

### 🐞 BUG-037
- **Title:** Admins cannot change user roles  
- **GitHub Link:** [D037](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/86)  
- **Requirement Affected:** Administrative Functions Requirements – User Management  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to update user roles. Changes to user roles do not save or reflect immediately, preventing proper role management.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to **User Management** and select a user.  
4. Attempt to change the user’s role.  
5. Observe that the changes are not saved or reflected.  

#### Expected Result
Admins should be able to update user roles and see changes reflected immediately.  

#### Actual Result
Admin cannot update user roles; changes are not saved.

---

### 🐞 BUG-038
- **Title:** Admins cannot suspend or delete user accounts  
- **GitHub Link:** [D038](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/87)  
- **Requirement Affected:** Administrative Functions Requirements – User Management  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to suspend or delete user accounts. Attempts to perform these actions fail, preventing proper account management and enforcement of policies.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to **User Management** and select a user.  
4. Attempt to suspend or delete the account.  
5. Observe that the system does not allow the action.  

#### Expected Result
Admins should be able to suspend or delete user accounts successfully.  

#### Actual Result
Admin cannot suspend or delete user accounts; system does not update status.

---

### 🐞 BUG-039
- **Title:** Admins cannot moderate community posts and comments  
- **GitHub Link:** [D039](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/88)  
- **Requirement Affected:** Administration – Content Moderation  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to view, review, or manage posts/comments from the moderation panel. This blocks moderation activities, reducing the ability to manage inappropriate content in the community feed.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to **Community Feed → Moderation Panel**.  
4. Attempt to moderate posts or comments.  
5. Observe that actions fail and moderation is not possible.  

#### Expected Result
Admins should be able to view and manage all posts/comments through the moderation panel.  

#### Actual Result
Admins cannot moderate posts or comments.

---

### 🐞 BUG-040
- **Title:** Admins cannot delete inappropriate content  
- **GitHub Link:** [D040](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/89)  
- **Requirement Affected:** Administration – Content Moderation  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to delete inappropriate posts or comments. Attempts to delete content fail, leaving inappropriate content visible publicly.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to **Community Feed → Moderation Panel**.  
4. Attempt to delete a post or comment.  
5. Observe that the deletion action fails.  

#### Expected Result
Admins should be able to delete inappropriate posts/comments and remove them from public view.  

#### Actual Result
Admin cannot delete posts or comments.

---

### 🐞 BUG-041
- **Title:** User flags/reports do not appear in admin moderation queue  
- **GitHub Link:** [D041](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/90)  
- **Requirement Affected:** Administration – Content Moderation  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
When users flag or report inappropriate posts/comments, the reports do not appear in the admin moderation queue. This prevents admins from reviewing reported content and enforcing community rules.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as a regular user.  
3. Flag or report a post/comment in the Community Feed.  
4. Log in as an admin user and navigate to the **Moderation Panel**.  
5. Observe that the flagged report does not appear.  

#### Expected Result
Reports submitted by users should appear in the admin moderation queue for review.  

#### Actual Result
User reports do not appear in the moderation queue.

---

### 🐞 BUG-042
- **Title:** Admins cannot publish new blog posts  
- **GitHub Link:** [D042](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/91)  
- **Requirement Affected:** Content Management Requirements – Blog System  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Admins are unable to publish new blog posts. Attempts to create and save a blog post fail, preventing content from appearing in the blog list.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as an admin user.  
3. Navigate to **Blog Management → Create Post**.  
4. Enter blog content and attempt to publish.  
5. Observe that the post does not appear in the blog list.  

#### Expected Result
Admins should be able to create and publish blog posts, and posts should appear in the blog list.  

#### Actual Result
Blog posts fail to publish; content does not appear in the blog list.
---
### 🐞 BUG-043
- **Title:** Users cannot mark notifications as read  
- **GitHub Link:** [D043](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/92)  
- **Requirement Affected:** Notifications  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
When users attempt to mark notifications as read, the notifications remain in the unread state and the unread counter does not update. This affects usability and prevents users from accurately tracking which notifications have been addressed.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as a registered user.  
3. Click on the notification bell to view notifications.  
4. Attempt to mark one or more notifications as read.  
5. Observe that the notifications remain in the unread state and the unread counter does not decrease.  

#### Expected Result
Selected notifications should change to a "read" state and the unread counter should update accordingly.  

#### Actual Result
Notifications cannot be marked as read, and the unread counter does not update.

---

### 🐞 BUG-044
- **Title:** Contextual help and tooltips are missing  
- **GitHub Link:** [D044](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/93)  
- **Requirement Affected:** Support & Maintenance – Help System  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users are unable to see contextual help or tooltips in the application. This reduces usability and may confuse new or infrequent users about functionality.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate to different sections of the application.  
3. Hover over icons, buttons, or interactive elements.  
4. Observe that no contextual help or tooltips appear.  

#### Expected Result
Users should see contextual help and tooltips where applicable.  

#### Actual Result
Contextual help and tooltips are missing.

---

### 🐞 BUG-045
- **Title:** FAQ section is missing or inaccessible  
- **GitHub Link:** [D045](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/94)  
- **Requirement Affected:** Support & Maintenance – Help System  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The FAQ section is not visible or cannot be accessed by users. This prevents users from finding answers to common questions independently.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate to the **Help / FAQ** section.  
3. Attempt to access frequently asked questions.  
4. Observe that the FAQ section is missing or inaccessible.  

#### Expected Result
Users should be able to access the FAQ section and read answers to common questions.  

#### Actual Result
FAQ section is missing or cannot be accessed.

---

### 🐞 BUG-046
- **Title:** Support contact information is not visible  
- **GitHub Link:** [D046](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/95)  
- **Requirement Affected:** Support & Maintenance – Help System  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users cannot view support contact information, including email, phone, or chat options. This prevents users from reaching out for help when needed.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate to the **Help / Support** section.  
3. Attempt to find contact information for support.  
4. Observe that email, phone, or chat details are not displayed.  

#### Expected Result
Users should see complete support contact information, including email, phone, and chat options.  

#### Actual Result
Support contact information is missing or incomplete.
----
# CleanCity Bug Reports – Support & Help System

### 🐞 BUG-044
- **Title:** Contextual help and tooltips are missing  
- **GitHub Link:** [D044](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/93)  
- **Requirement Affected:** Support & Maintenance – Help System  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users are unable to see contextual help or tooltips in the application. This reduces usability and may confuse new or infrequent users about functionality.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate to different sections of the application.  
3. Hover over icons, buttons, or interactive elements.  
4. Observe that no contextual help or tooltips appear.  

#### Expected Result
Users should see contextual help and tooltips where applicable.  

#### Actual Result
Contextual help and tooltips are missing.

---

### 🐞 BUG-045
- **Title:** FAQ section is missing or inaccessible  
- **GitHub Link:** [D045](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/94)  
- **Requirement Affected:** Support & Maintenance – Help System  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The FAQ section is not visible or cannot be accessed by users. This prevents users from finding answers to common questions independently.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate to the **Help / FAQ** section.  
3. Attempt to access frequently asked questions.  
4. Observe that the FAQ section is missing or inaccessible.  

#### Expected Result
Users should be able to access the FAQ section and read answers to common questions.  

#### Actual Result
FAQ section is missing or cannot be accessed.

---

### 🐞 BUG-046
- **Title:** Support contact information is not visible  
- **GitHub Link:** [D046](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/95)  
- **Requirement Affected:** Support & Maintenance – Help System  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Users cannot view support contact information, including email, phone, or chat options. This prevents users from reaching out for help when needed.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate to the **Help / Support** section.  
3. Attempt to find contact information for support.  
4. Observe that email, phone, or chat details are not displayed.  

#### Expected Result
Users should see complete support contact information, including email, phone, and chat options.  

#### Actual Result
Support contact information is missing or incomplete.

---
### 🐞 BUG-048
- **Title:** Breadcrumbs do not display full page hierarchy  
- **GitHub Link:** -  
- **Requirement Affected:** User Interface Requirements – Navigation  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
On complex pages, the breadcrumb navigation only shows **"Profile"** when editing a page, and the full hierarchy of the page is missing. This affects user orientation and navigation clarity.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Log in as a user.  
3. Navigate to a complex page (e.g., profile editing with nested sections).  
4. Observe the breadcrumb displayed at the top of the page.  

#### Expected Result
Breadcrumbs should display the full, accurate hierarchy of the current page.  

#### Actual Result
Breadcrumb shows only **"Profile"**, and the hierarchy is missing.

---

### 🐞 BUG-049
- **Title:** Search bar does not return results or apply filters  
- **GitHub Link:** -  
- **Requirement Affected:** User Interface Requirements – Navigation  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The search bar and filters do not function correctly. Entering a search query or selecting filters does not update the article list, preventing users from finding content efficiently.  

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate to the articles or content listing page.  
3. Enter a query in the search bar or apply filters.  
4. Observe the results displayed.  

#### Expected Result
Search results and filters should update dynamically based on user input.  

#### Actual Result
Search queries and filters have no effect; the article list remains unchanged.
---
### 🐞 BUG-050
- **Title:** Date selection allows today and past dates  
- **GitHub Link:** [D050](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96)  
- **Requirement Affected:** Input Validation Requirements – Date Fields  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system allows selection of today or past dates, which violates the minimum date restriction (tomorrow). Users can submit invalid dates.  

#### Steps to Reproduce
1. Open the date picker on a form.  
2. Select today or a past date.  
3. Observe that the system does not show a validation error.  

#### Expected Result
Dates today and earlier should be rejected with a validation message.  

#### Actual Result
Dates today and earlier are accepted.

---

### 🐞 BUG-051
- **Title:** Date selection allows dates beyond 30 days  
- **GitHub Link:** [D051](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/97)  
- **Requirement Affected:** Input Validation Requirements – Date Fields  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The date picker allows selection of dates beyond 30 days from today, violating the maximum date constraint.  

#### Steps to Reproduce
1. Open the date picker on a form.  
2. Select a date more than 30 days from today.  
3. Observe that no validation error is shown.  

#### Expected Result
Dates >30 days from today should be rejected with a validation message.  

#### Actual Result
Dates beyond 30 days are accepted.

---

### 🐞 BUG-052
- **Title:** Name field accepts invalid lengths (<2 or >50 characters)  
- **GitHub Link:** [D052](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/98)  
- **Requirement Affected:** Input Validation Requirements – Name Fields  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system allows names shorter than 2 characters or longer than 50 characters. This breaks data consistency.  

#### Steps to Reproduce
1. Enter a name shorter than 2 characters or longer than 50 characters.  
2. Submit the form.  
3. Observe that the system accepts invalid input.  

#### Expected Result
Names <2 or >50 characters should be rejected.  

#### Actual Result
Names outside valid length are accepted.

---

### 🐞 BUG-053
- **Title:** Password field allows fewer than 8 characters  
- **GitHub Link:** [D053](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/99)  
- **Requirement Affected:** Input Validation Requirements – Password Fields  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The password field does not enforce a minimum of 8 characters, allowing weak passwords.  

#### Steps to Reproduce
1. Enter a password shorter than 8 characters.  
2. Submit the form.  
3. Observe that the password is accepted.  

#### Expected Result
Passwords <8 characters should be rejected with a validation error.  

#### Actual Result
Short passwords are accepted.

---

### 🐞 BUG-054
- **Title:** Instructions field allows more than 200 characters  
- **GitHub Link:** [D054](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/100)  
- **Requirement Affected:** Input Validation Requirements – Instructions Field  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The instructions field allows more than 200 characters, which may lead to display or storage issues.  

#### Steps to Reproduce
1. Enter more than 200 characters in the instructions field.  
2. Submit the form.  
3. Observe that no validation occurs.  

#### Expected Result
Instructions >200 characters should be rejected.  

#### Actual Result
Instructions >200 characters are accepted.

---

### 🐞 BUG-055
- **Title:** Unicode and international characters cause email send failure  
- **GitHub Link:** [D055](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/101)  
- **Requirement Affected:** Input Validation Requirements – Unicode & International Characters  
- **Severity:** Minor  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Using Unicode or international characters in email prevents sending emails correctly, though inputs are accepted.  

#### Steps to Reproduce
1. Enter Unicode characters in the email field.  
2. Attempt to send an email.  
3. Observe that the email fails to send.  

#### Expected Result
Emails with Unicode/international characters should be processed successfully.  

#### Actual Result
Cannot send email with symbols.

---

### 🐞 BUG-056
- **Title:** Very long inputs are accepted beyond maximum length  
- **GitHub Link:** [D056](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/102)  
- **Requirement Affected:** Input Validation Requirements – Input Length  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
Inputs exceeding maximum allowed length are accepted, which may cause database or display issues.  

#### Steps to Reproduce
1. Enter a value longer than the maximum length for any input field.  
2. Submit the form.  
3. Observe that the system accepts it.  

#### Expected Result
Inputs exceeding the maximum length should be rejected with a validation message.  

#### Actual Result
Very long inputs are accepted.
---
### 🐞 BUG-057
- **Title:** System responds slowly to user interactions, exceeding 1-second threshold  
- **GitHub Link:** [D057](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/103)  
- **Requirement Affected:** Performance – User Interaction Responsiveness  
- **Severity:** Major  
- **Environment:** Development, Google Chrome, Windows 10  

#### Summary
The system fails to respond to user interactions within the expected **1-second timeframe**. During testing, the Total Blocking Time (TBT) was measured at **1,720 ms**, exceeding the specified performance requirement. This may result in delayed feedback to the user and degrade the overall experience.

#### Steps to Reproduce
1. Open the CleanCity application in Google Chrome.  
2. Navigate through typical user interactions such as clicking buttons, opening menus, or submitting forms.  
3. Measure response time using browser  DevTools Performance tab.  
4. Observe that the system takes longer than 1 second to respond to interactions.

#### Expected Result
All user interactions should respond **within 1 second**.

#### Actual Result
Total Blocking Time recorded was **1,720 ms**, exceeding the 1-second performance requirement.
----
### 🐞 BUG-058
- **Title:** Map fails to load under slow internet connections  
- **GitHub Link:** D0058 
- **Requirement Affected:** Pickup Location – Map Rendering  
- **Severity:** Major 

#### Summary
Map fails to load on slow networks.

#### Steps to Reproduce
1. Throttle network to “Slow 3G”.  
2. Open Pickup Request page.

#### Expected Result
Map loads with fallback or spinner.

#### Actual Result
Map fails to load.

