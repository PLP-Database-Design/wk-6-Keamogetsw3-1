# CleanCity Application – QA Test Cases

## 📋 Document Information
**Document Version:** 1.1  
**Date:** 18 Novemeber 2025  
**Project:** CleanCity - Waste Pickup Scheduler  
**Prepared For:** QA Testing Teams 

---

## Functional Test Cases - Manual Testing

### **1. Authentication System**
---

#### 1.1 Registration Test Case

| Test Case ID | Objective                         | Expected Result              | Risk ID |
| ----- | --------------------------------- | ---------------------------- | --------- |
| TC-001 | Register new user with valid data | Account created successfully | R-001      |
| TC-002 | Register user with invalid email  | Validation error displayed   | R-001      |
| TC-003 | Register user with empty name     | Validation error displayed   | R-001      |
| TC-004 | Register user with empty email    | Validation error displayed   | R-001      |
| TC-005 | Register user with empty password | Validation error displayed   | R-001      |
---
#### 1.2 Login Test Cases

| Test Case ID | Objective                                | Expected Result                       | Risk ID |
|--------------|-----------------------------------------|---------------------------------------|-----------|
| TC-006      | Login with valid credentials             | Login successful                      | R-001      |
| TC-007      | Login with invalid password              | Error: "Invalid email or password"    | R-001      |
| TC-008      | Login with empty Email             | System should display email required error    | R-001      |
| TC-009      | Login with empty Password              | System should display password required error | R-001      |
| TC-010      | Login with non-existent user             | Error: "Invalid email or password"    | R-001      |
---
### 1.3 Logout Test Cases
| Test Case ID | Objective                                      | Expected Result                                               | Risk ID |
|--------------|------------------------------------------------|---------------------------------------------------------------|---------|
| TC-011       | Verify user can successfully log out           | User is logged out and redirected to the Home page           | R-001    |
| TC-012       | Verify user cannot access dashboard after logout | Attempting to access dashboard redirects to login page     | R-001    |
| TC-013      | Verify scheduling a pickup without login       | System should restrict access and redirect to login page      | R-001    |

---
### 1.4 User Session Management (localStorage)
| Test Case ID | Objective                                              | Expected Result                                                 | Risk ID |
|--------------|--------------------------------------------------------|-----------------------------------------------------------------|---------|
| TC-014  | Verify session data is stored in localStorage after login | localStorage contains session key | R-003    |
| TC-015  | Verify user session persists after page refresh        | User remains logged in; localStorage values persist | R-003    |
| TC-016  | Verify session persists after reopening browser tab    | User remains logged in; session data still stored in localStorage | R-003|
| TC-017  | Verify session data is cleared after logout            | localStorage entries removed | R-003    |
| TC-018  | Verify access restricted when localStorage cleared manually | User is logged oute after refresh | R-003    |

---
### 1.5 Role-Based Access Test Cases
| Test Case ID | Objective                                              | Expected Result                                                 | Risk ID |
|--------------|--------------------------------------------------------|-----------------------------------------------------------------|---------|
| TC-019  | Verify system creates a new user account with “User” role upon successful registration | System automatically assigns the “User” role to newly registered accounts | R-004 |
| TC-020  | Verify system supports two user roles: “User” and “Admin”. Each user can have only one valid role assigned | System supports two user roles: “User” and “Admin”| R-004  |
| TC-021  | Verify only Admins can access Admin Dashboard | “User” role doesnt show Admin dashboard. “Admin” role can access successfully | R-004  |
| TC-022  | Verify direct URL access to Admin Dashboard is blocked for non-admin users | System restricts access and redirects to “Access Denied” or “Login” page | R-004  |

---

### **2. 🗑️ Waste Management Requirements**

---
### 2.1 Pickup Scheduling
| Test Case ID | Objective                                              | Expected Result                                                 | Risk ID |
|--------------|--------------------------------------------------------|-----------------------------------------------------------------|---------|
| TC-023  | Verify system accepts submission and displays confirmation message (“Pickup scheduled successfully”) | Confirmation message showing that form is submitted and Pickup scheduled successfully | R-002 |
| TC-024  | Invalid pickup request (no data)                     | System shows validation errors for empty fields       | R-002   |
| TC-025  | Invalid pickup request (Yesterday’s date)            | System does not allow scheduling for past date        | R-002   |
| TC-026  | Invalid pickup request (empty Waste Type)            | System shows error indicating Waste Type is required | R-002   |
| TC-027  | Invalid pickup request (empty Location)              | System shows error indicating Location is required   | R-002   |
| TC-028  | Invalid pickup request (Very long text >200 chars)   | System truncates input or shows error for long text  | R-002   |
| FC-029  | The system shall prevent scheduling multiple pickups for the same date | System prevents creating duplicate pickups for the same date | R-002   |

### 2.2 Request Management Test Cases
| Test Case ID    | Objective                                                                                                     | Expected Result                                                                                       | Risk ID   |
| --------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------- |
| TC-030 | Verify that the system displays the user’s pickup request history.                                            | User can view a list of all past and current pickup requests with details (date, waste type, status). | R-002 |
| TC-031 | Verify that completed and cancelled requests appear correctly in the history.                                 | The system includes all request types (Completed, Cancelled, etc.) in the history view.               | R-002 |
| TC-032 | Verify that the user can cancel a pending pickup request.                                                     | The system successfully cancels the request and updates the status to “Cancelled.”                    | R-002 |
| TC-033 | Verify that the system does not allow cancelling completed or already cancelled requests.                     | User receives an appropriate error or message indicating cancellation is not possible.                | R-002 |
| TC-034 | Verify that users can modify pickup details (e.g., date, waste type) at least 24 hours before scheduled time. | The system allows modification and updates the request details successfully.                          | R-002 |
| TC-035 | Verify that users cannot modify pickup details within 24 hours of the scheduled time.                         | The system prevents modification and displays an appropriate warning message.                         | R-002 |
| TC-036 | Verify that the system displays correct request status for each pickup request.                               | Status is displayed as Pending, Confirmed, Completed, or Cancelled, based on the request’s state.     | R-002 |
| TC-037 | Verify that request status updates automatically after completion or cancellation.                            | The status changes dynamically according to the action taken (e.g., from Confirmed → Completed).      | R-002 |


---


---
### 📞 Support and Maintenance
### Table: Help System
| Test Case ID    | Objective                                                                                                     | Expected Result                                                                                       | Risk ID   |
| --------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------- |
| TC-093 |  Ensure users can access the FAQ section and all content is displayed correctly. | FAQ page loads with all questions and answers correctly |  |
| TC-094 | Verify that contact information for support is displayed | Support email, phone, and/or chat options are visible and clickable |  |

-----


-----

## ** Non-Functional Test Cases**
-----
This section focuses on testing the system's non-functional requirements, which define how the system performs rather than what it does. It includes aspects such as performance, usability, reliability, security and compatibility. Non-functional test cases ensure that the system meets quality standards and provides a good user experience under expected conditions.

------


------

---
## Functional Test Cases - Boundary and Edge Case Test Cases
| Test Case ID | Feature | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|----------------|

---

| TC No. | Feature              | Objective                                           | Expected Result                                   | Actual Result                                         | Status     | Risk Link |
|--------:|----------------------|----------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|-------------|------------|
| TC001  | Registration         | Register new user with valid data                   | Account created successfully                       | Account successfully created                          | ✅ Pass     | R002       |
| TC002  | Registration         | Register user with invalid email                    | Validation error displayed                         | Error was shown                                       | ✅ Pass     | R002       |
| TC003  | Registration         | Register user with empty name                       | Validation error displayed                         | Error was shown                                       | ✅ Pass     | R002       |
| TC004  | Login                | Login with correct credentials                      | Access granted                                     | Logged in successfully                                | ✅ Pass     | R003       |
| TC005  | Pickup Scheduling    | Schedule new pickup                                 | Request created successfully                       | Request created successfully                          | ✅ Pass     | R006       |
| TC006  | Pickup Scheduling    | Cancel pickup request                               | Request status updated to "Cancelled"              | Cancel operation failed                               | ❌ Fail     | R006       |
| TC007  | Blog Module          | Publish a new blog post                             | Post appears in blog list                          | Blog post failed to publish                           | ❌ Fail     | R007       |
| TC008  | Admin Panel          | Admin panel login                                   | Admin successfully logs in                         | Admin logged in successfully                          | ✅ Pass     | R008       |
| TC009  | Admin Dashboard      | Cannot receive or reply to feedback                 | Feedback system should accept and reply properly   | Admin unable to receive or reply to feedback          | ❌ Fail     | R008       |
| TC010  | Dashboard Filters    | Filter by status (Admin & User)                     | Only requests with selected status should display  | Filter not working in both dashboards                 | ❌ Fail     | R002       |
| TC011  | Dashboard Filters    | Filter by location (Admin & User)                   | Only requests in selected location should display  | Requests filtered correctly by location               | ✅ Pass     | R002       |
| TC012  | Admin Panel          | Update user status                                  | User status updates successfully                   | Status updated successfully                           | ✅ Pass     | R008       |






---

### **2. Non-Functional Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC011 | Performance | Load 5000+ pickup requests | UI should remain responsive | TBD | TBD | R016 |
| TC012 | Performance | Load 1000+ user accounts | Application remains stable | TBD | TBD | R016 |
| TC013 | Security | Test XSS payloads in inputs | Scripts should not execute | TBD | TBD | R012 |
| TC014 | Security | Test SQL injection payloads | Should be rejected / sanitized | TBD | TBD | R012 |
| TC015 | Usability | Validate responsive navigation | Works correctly on mobile and tablet | TBD | TBD | R009 |
| TC016 | Data Persistence | Validate localStorage storage | Data persists across page reloads | TBD | TBD | R013 |

---

### **3. Accessibility Test Cases**

| TC No.    | Feature        | Objective                                | Expected Result                                                 | Actual Result                                                             | Status | Risk Link |
| :-------- | :------------- | :--------------------------------------- | :-------------------------------------------------------------- | :------------------------------------------------------------------------ | :----- | :-------- |
| **TC017** | Awareness Page | Screen reader reads images               | Images have descriptive alt text                                | `alt` attribute missing for awareness page images                         | ❌ Fail | R010      |
| **TC018** | Forms          | Keyboard navigation on registration form | All fields accessible and focusable using **Tab** and **Enter** | Tabbing works smoothly and Enter button functions correctly on login page | ✅ Pass | R010      |
| **TC019** | Forms          | Color contrast check                     | Meets WCAG 2.1 AA standards (contrast ratio ≥ 4.5:1)            | Text readable; no low contrast detected                                   | ✅ Pass | R010      |
| **TC020** | Buttons        | Minimum touch target size                | Buttons are ≥ 44x44px on mobile                                 | Register: 80x48 ✅, Login: 76x45 ✅, Comment: 50x44 ✅                       | ✅ Pass | R010      |


---
4. CROSS ROWSER COMPATABILITY TESTING

| TC No. | Feature              | Objective                                           | Expected Result                                 | Actual Result                                      | Status     | Risk Link |
|--------:|----------------------|----------------------------------------------------|--------------------------------------------------|----------------------------------------------------|-------------|------------|
| TC021  | Registration         | Register new user with valid data                   | Account created successfully                     | Successfully registered new user in Chrome         | ✅ Pass     | R002       |
| TC022  | Login                | Login with correct credentials                      | Access granted                                   | Successfully logged in with correct password       | ✅ Pass     | R003       |
| TC023  | Login                | Login with wrong credentials                        | Error message displayed                          | Error “Wrong password” displayed as expected       | ✅ Pass     | R003       |
| TC024  | Login                | Login with the same credentials across all browsers | Invalid email or wrong password message          | Failed to login — “Invalid email or wrong password”| ❌ Fail     | R003       |
| TC025  | Dashboard Filters    | Filter by Status                                    | Only requests with selected status display       | Requests filtered correctly by status              | ✅ Pass     | R002       |
| TC026  | Dashboard Filters    | Filter by Location                                  | Only requests in selected location display       | Requests filtered correctly by location            | ✅ Pass     | R002       |
| TC027  | Pickup & Rescheduling| Verify pickup and rescheduling functions properly   | Request should be successfully rescheduled/picked| Function failed to reschedule/pickup request       | ❌ Fail     | R004       |
| TC028  | Awareness Page       | Verify awareness page loads and displays content    | Awareness page loads successfully                | Awareness page displayed correctly with all content| ✅ Pass     | R005       |

---

### 📞 Support and Maintenance
### Table: Help System
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC-  | Registration | Enter name with minimum characters (2) | Accepted and account created | TBD | TBD | R002 |
| TC- | Registration | Enter name with maximum characters (50) | Accepted and account created | TBD | TBD | R002 |
| TC027 | Registration | Enter email with special characters | Accepted if valid format | TBD | TBD | R002 |
---
### **5. Boundary and Edge Case Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC025 | Registration | Enter name with minimum characters (2) | Accepted and account created | TBD | TBD | R002 |
| TC026 | Registration | Enter name with maximum characters (50) | Accepted and account created | TBD | TBD | R002 |
| TC027 | Registration | Enter email with special characters | Accepted if valid format | TBD | TBD | R002 |
| TC028 | Registration | Enter password less than 8 characters | Validation error displayed | TBD | TBD | R014 |
| TC029 | Pickup Scheduling | Schedule pickup on minimum allowed date (tomorrow) | Accepted, request created | TBD | TBD | R006 |
| TC030 | Pickup Scheduling | Schedule pickup on maximum allowed date (30 days) | Accepted, request created | TBD | TBD | R006 |
| TC031 | Pickup Scheduling | Enter very long instructions (>200 chars) | Validation error displayed | TBD | TBD | R015 |
| TC032 | Community Module | Input Unicode characters in post/comment | Displayed correctly without errors | TBD | TBD | R011 |
| TC033 | Community Module | Input HTML or JS scripts | Sanitized, no script executed | TBD | TBD | R012 |
| TC034 | Profile Update | Empty or whitespace-only inputs | Validation error displayed | TBD | TBD | R002 |

---

## Automated Testing

### **1. Functional Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC035 | Registration | Register new user with valid data | Account created successfully | TBD | TBD | R002 |
| TC036 | Registration | Register user with invalid email | Validation error displayed | TBD | TBD | R002 |
| TC037 | Login | Login with correct credentials | Access granted | TBD | TBD | R003 |
| TC038 | Login | Login with wrong credentials | Error message displayed | TBD | TBD | R003 |
| TC039 | Pickup Scheduling | Schedule new pickup | Request created successfully | TBD | TBD | R006 |
| TC040 | Pickup Scheduling | Cancel pickup request | Request status updated to "Cancelled" | TBD | TBD | R006 |
| TC041 | Blog Module | Publish a new blog post | Post appears in blog list | TBD | TBD | R007 |
| TC042 | Community Module | Add a new post | Post appears in community feed | TBD | TBD | R011 |
| TC043 | Profile Management | Update profile information | Changes reflected in user profile | TBD | TBD | R002 |
| TC044 | Admin Panel | Mark pickup as scheduled | Status updated, UI refreshed | TBD | TBD | R008 |

---

### **2. Non-Functional Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC045 | Performance | Load 5000+ pickup requests | UI should remain responsive | TBD | TBD | R016 |
| TC046 | Performance | Load 1000+ user accounts | Application remains stable | TBD | TBD | R016 |
| TC047 | Security | Test XSS payloads in inputs | Scripts should not execute | TBD | TBD | R012 |
| TC048 | Security | Test SQL injection payloads | Should be rejected / sanitized | TBD | TBD | R012 |
| TC049 | Usability | Validate responsive navigation | Works correctly on mobile and tablet | TBD | TBD | R009 |
| TC050 | Data Persistence | Validate localStorage storage | Data persists across page reloads | TBD | TBD | R013 |

---

### **3. Accessibility Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC051 | Awareness Page | Screen reader reads images | Images have descriptive alt text | TBD | TBD | R010 |
| TC052 | Forms | Keyboard navigation on registration form | All fields accessible and focusable | TBD | TBD | R010 |
| TC053 | Forms | Color contrast check | Meets WCAG 2.1 AA standards | TBD | TBD | R010 |
| TC054 | Buttons | Minimum touch target size | Buttons are ≥44x44px on mobile | TBD | TBD | R010 |

---

### **4. Cross-Browser Compatibility Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC055 | Registration | Test in Chrome, Firefox, Safari, Edge | Form works consistently in all browsers | TBD | TBD | R017 |
| TC056 | Pickup Scheduling | Test in Chrome, Firefox, Safari, Edge | Requests can be created and viewed in all browsers | TBD | TBD | R017 |
| TC057 | Blog Module | Test in Chrome, Firefox, Safari, Edge | Blog posts render correctly in all browsers | TBD | TBD | R017 |
| TC058 | Community Module | Test in Chrome, Firefox, Safari, Edge | Posts, comments, and likes function in all browsers | TBD | TBD | R017 |

---



### 📞 Support and Maintenance
### Table: Help System

---

### **5. Boundary and Edge Case Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC059 | Registration | Enter name with minimum characters (2) | Accepted and account created | TBD | TBD | R002 |
| TC060 | Registration | Enter name with maximum characters (50) | Accepted and account created | TBD | TBD | R002 |
| TC061 | Registration | Enter email with special characters | Accepted if valid format | TBD | TBD | R002 |
| TC062 | Registration | Enter password less than 8 characters | Validation error displayed | TBD | TBD | R014 |
| TC063 | Pickup Scheduling | Schedule pickup on minimum allowed date (tomorrow) | Accepted, request created | TBD | TBD | R006 |
| TC064 | Pickup Scheduling | Schedule pickup on maximum allowed date (30 days) | Accepted, request created | TBD | TBD | R006 |
| TC065 | Pickup Scheduling | Enter very long instructions (>200 chars) | Validation error displayed | TBD | TBD | R015 |
| TC066 | Community Module | Input Unicode characters in post/comment | Displayed correctly without errors | TBD | TBD | R011 |
| TC067 | Community Module | Input HTML or JS scripts | Sanitized, no script executed | TBD | TBD | R012 |
| TC068 | Profile Update | Empty or whitespace-only inputs | Validation error displayed | TBD | TBD | R002 |
