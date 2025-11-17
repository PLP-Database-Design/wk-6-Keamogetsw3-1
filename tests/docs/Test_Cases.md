# CleanCity: Waste Pickup Scheduler - Test Cases

## 📋 Document Information
**Document Version:** 1.1  
**Date:** 18 Novemeber 2025  
**Project:** CleanCity - Waste Pickup Scheduler  
**Prepared For:** QA Testing Teams 

---

## Functional Test Cases

### **1 🔐 Authentication System Requirements**
---
#### **1.1 👤 User Registration Test Cases**

#### Table 1.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                         | Expected Result              | Risk ID | Notes              |
| ------------ | --------------------------------- | ---------------------------- | ------- | ------------------ |
| TC001       | Register new user with valid data | Account created successfully | R001   | Positive Test Case |
| TC002       | Register user with invalid email  | Validation error displayed   | R001   | Negative Test Case |
| TC003       | Register user with empty name     | Validation error displayed   | R001   | Negative Test Case |
| TC004       | Register user with empty email    | Validation error displayed   | R001   | Negative Test Case |
| TC005       | Register user with empty password | Validation error displayed   | R001   | Negative Test Case |

#### 1.1.2 Test cases for **Selenium automated testing** 🤖
| Test Case ID | Objective                         | Expected Result              | Risk ID | Notes              |
| ------------ | --------------------------------- | ---------------------------- | ------- | ------------------ |
| TC006       | Register new user with valid data | Account created successfully | R001   | Positive Test Case |
| TC007       | Register user with invalid email  | Validation error displayed   | R001   | Negative Test Case |
| TC008       | Register user with empty name     | Validation error displayed   | R001   | Negative Test Case |
| TC009       | Register user with empty email    | Validation error displayed   | R001   | Negative Test Case |
| TC010       | Register user with empty password | Validation error displayed   | R001   | Negative Test Case |

---

#### 1.2 👤 User Login Test Cases

#### Table 1.2.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                    | Expected Result                               | Risk ID | Notes            |
| ------------ | ---------------------------- | --------------------------------------------- | ------- | ---------------- |
| TC011        | Login with valid credentials | Login successful                              | R001    | Positive Test Case |
| TC012        | Login with invalid password  | Error: "Invalid email or password"            | R001    | Negative Test Case |
| TC013        | Login with empty Email       | System should display email required error    | R001    | Negative Test Case |
| TC014        | Login with empty Password    | System should display password required error | R001    | Negative Test Case  |
| TC015        | Login with non-existent user | Error: "Invalid email or password"            | R001    | Negative Test Case  |

#### 1.2.2 Test cases for **Selenium automated testing** 🤖
| Test Case ID | Objective                    | Expected Result                               | Risk ID | Notes            |
| ------------ | ---------------------------- | --------------------------------------------- | ------- | ---------------- |
| TC016        | Login with valid credentials | Login successful                              | R001    | Positive Test Case |
| TC017        | Login with invalid password  | Error: "Invalid email or password"            | R001    | Negative Test Case |
| TC018        | Login with empty Email       | System should display email required error    | R001    | Negative Test Case |
| TC019        | Login with empty Password    | System should display password required error | R001    | Negative Test Case  |
| TC020        | Login with non-existent user | Error: "Invalid email or password"            | R001    | Negative Test Case  |

---

##### 1.3 👤 User Logout Test Cases
#### Table 1.3.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                        | Expected Result                                          | Risk ID | Notes              |
| ------------ | ------------------------------------------------ | -------------------------------------------------------- | ------- | ------------------ |
| TC021        | Verify user can successfully log out             | User is logged out and redirected to the Home page       | R001    | Positive test case |
| TC022        | Verify user cannot access dashboard after logout | Attempting to access dashboard redirects to login page   | R001    | Negative test case |
| TC023        | Verify scheduling a pickup without login         | System should restrict access and redirect to login page | R001    | Negative test case |

#### 1.3.2 Test cases for **Selenium automated testing** 🤖
| Test Case ID | Objective                                        | Expected Result                                          | Risk ID | Notes              |
| ------------ | ------------------------------------------------ | -------------------------------------------------------- | ------- | ------------------ |
| TC024        | Verify user can successfully login then log out  | User is logged out and redirected to the Home page       | R001    | Positive test case |

---

##### 1.4 👤 Role-Based Access Test Cases
#### Table 1.4.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                                                                  | Expected Result                                                                | Risk ID | Notes              |
| ------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------- | ------------------ |
| TC025        | Verify system creates a new user account with “User” role upon successful registration                     | System automatically assigns the “User” role to newly registered accounts      | R004    | Positive test case |
| TC026        | Verify system supports two user roles: “User” and “Admin”. Each user can have only one valid role assigned | System supports two user roles: “User” and “Admin”                             | R004    | Positive test case |
| TC027        | Verify only Admins can access Admin Dashboard                                                              | “User” role doesn't show Admin dashboard. “Admin” role can access successfully | R004    | Negative test case |
| TC028        | Verify direct URL access to Admin Dashboard is blocked for non-admin users                                 | System restricts access and redirects to “Access Denied” or “Login” page       | R004    | Negative test case |


---
### **2. 🗑️ Waste Management Requirements**
---
#### **2.1 🚚 Pickup Scheduling**
#### Table 2.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                                                            | Expected Result                                                                       | Risk ID | Notes              |
| ------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------- | ------------------ |
| TC029        | Verify system accepts submission and displays confirmation message (“Pickup scheduled successfully”) | Confirmation message showing that form is submitted and Pickup scheduled successfully | R002    | Positive test case |
| TC030        | Invalid pickup request (no data)                                                                     | System shows validation errors for empty fields                                       | R002    | Negative test case |
| TC031        | Invalid pickup request (Yesterday’s date)                                                            | System does not allow scheduling for past date                                        | R002    | Negative test case |
| TC032        | Invalid pickup request (empty Waste Type)                                                            | System shows error indicating Waste Type is required                                  | R002    | Negative test case |
| TC033        | Invalid pickup request (empty Location)                                                              | System shows error indicating Location is required                                    | R002    | Negative test case |
| TC034        | Invalid pickup request (Very long text >200 chars)                                                   | System truncates input or shows error for long text                                   | R002    | Negative test case |
| TC035        | The system shall prevent scheduling multiple pickups for the same date                               | System prevents creating duplicate pickups for the same date                          | R002    | Negative test case |


#### Table 2.1.2 Test cases for **Selenium automated testing** 🤖
| Test Case ID | Objective                                                                                            | Expected Result                                                                       | Risk ID | Notes              |
| ------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------- | ------------------ |
| TC036        | Verify system accepts submission and displays confirmation message (“Pickup scheduled successfully”) | Confirmation message showing that form is submitted and Pickup scheduled successfully | R002    | Positive test case |
---

#### **2.2 📋 Request Management**
#### Table 2.2.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                                                                     | Expected Result                                                                                       | Risk ID | Notes              |
| ------------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------- | ------------------ |
| TC037        | Verify that the system displays the user’s pickup request history.                                            | User can view a list of all past and current pickup requests with details (date, waste type, status). | R002    | Positive test case |
| TC038        | Verify that completed and cancelled requests appear correctly in the history.                                 | The system includes all request types (Completed, Cancelled, etc.) in the history view.               | R002    | Positive test case |
| TC039        | Verify that the user can cancel a pending pickup request.                                                     | The system successfully cancels the request and updates the status to “Cancelled.”                    | R002    | Positive test case |
| TC040        | Verify that the system does not allow cancelling completed or already cancelled requests.                     | User receives an appropriate error or message indicating cancellation is not possible.                | R002    | Negative test case |
| TC041        | Verify that users can modify pickup details (e.g., date, waste type) at least 24 hours before scheduled time. | The system allows modification and updates the request details successfully.                          | R002    | Positive test case |
| TC042        | Verify that users cannot modify pickup details within 24 hours of the scheduled time.                         | The system prevents modification and displays an appropriate warning message.                         | R002    | Negative test case |
| TC043        | Verify that the system displays correct request status for each pickup request.                               | Status is displayed as Pending, Confirmed, Completed, or Cancelled, based on the request’s state.     | R002    | Positive test case |
| TC044        | Verify that request status updates automatically after completion or cancellation.                            | The status changes dynamically according to the action taken (e.g., from Confirmed → Completed).      | R002    | Positive test case |
---

### **2.3 📋 Request Trackingt**
#### Table 2.3.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                                     | Expected Result                                                                              | Risk ID | Notes              |
| ------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------- | ------------------ |
| TC045        | Verify that the system provides real-time status updates for pickup requests. | Status of each pickup request updates dynamically without requiring page refresh.            | R002    | Positive test case |
| TC046        | Verify that users receive notifications for pickup request status changes.    | User receives notifications (email, SMS, or in-app) whenever the status of a pickup changes. | R002    | Positive test case |
| TC047        | Verify that users can add feedback after a pickup is completed.               | Users can submit feedback, and the system stores it associated with the completed pickup.    | R002    | Positive test case |

---
### **3. 📊 Dashboard & Analytics Requirements**
---
#### Table 3.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                                              | Expected Result                                                                                                                                | Risk ID | Notes              |
| ------------ | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------ |
| TC048        | Verify that the user dashboard displays personalized information for logged-in users   | Dashboard shows recent pickup requests, upcoming scheduled pickups, achievement badges, and quick action buttons                               | R002    | Positive test case |
| TC049        | Verify that the system shall calculate and display user's environmental impact metrics | Dashboard correctly calculates and displays total waste diverted, CO2 emissions saved, and trees equivalent saved                              | R002    | Positive test case |
| TC050        | Verify that the system awards badges for various achievements                          | User is awarded badges based on milestones (e.g., number of pickups completed, environmental impact) and badges are displayed on the dashboard | R002    | Positive test case |

---
### **4. 📝 Content Management Requirements**
---
#### **4.1 ✍️ Blog System**
#### Table 4.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                       | Expected Result                                                  | Risk Link | Notes              |
| ------------ | --------------------------------------------------------------- | ---------------------------------------------------------------- | --------- | ------------------ |
| TC051        | Verify that the blog list page loads successfully               | Blog page loads and displays available blog posts                | R005      | Positive test case |
| TC052        | Verify that users can view a single blog post                   | Blog post content (title, date, body, images) displays correctly | R005      | Positive test case |
| TC053        | Verify that users can interact with blog content (like/comment) | User can click like or submit a comment successfully             | R005      | Positive test case |
| TC054        | Verify that admins can create a blog post                       | Blog post is saved and appears in the list                       | R005      | Positive test case |
| TC055        | Verify that admins can edit an existing blog post               | Updated content is saved and reflected on the blog page          | R005      | Positive test case |
| TC056        | Verify that admins can delete a blog post                       | Blog post is removed and no longer visible                       | R005      | Positive test case |
| TC057        | Verify that categories/tags can be assigned to a blog post      | Tag/category appears on post and filtering works                 | R005      | Positive test case |

---
#### **4.2 👁️ Awareness Section**
#### Table 4.2.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                                   | Expected Result                                                                           | Risk Link | Notes              |
| ------------ | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------- | ------------------ |
| TC058        | Verify that rotating eco tips are displayed every 5 seconds                 | Eco tips rotate automatically every 5 seconds                                             | R005      | Positive test case |
| TC059        | Verify that users can access interactive quizzes about environmental topics | Quiz opens and users can answer questions interactively                                   | R005      | Positive test case |
| TC060        | Verify that quiz scores are tracked and explanations are provided           | After completing a quiz, the score is displayed and correct answer explanations are shown | R005      | Positive test case |
| TC061        | Verify that environmental infographics with statistics are displayed        | Infographics appear with accurate statistics and proper formatting                        | R005      | Positive test case |
| TC062        | Verify that action buttons link to other features                           | Clicking action buttons navigates to the correct related feature or page                  | R005      | Positive test case |

---
#### **4.3 🤝 Community Feed**
#### Table 4.2.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                        | Expected Result                                                          | Risk Link | Notes              |
| ------------ | ---------------------------------------------------------------- | ------------------------------------------------------------------------ | --------- | ------------------ |
| TC063        | Verify that users can create community posts  share tips and experiences  | Users can create and submit a post, and it appears in the community feed | R005      | Positive test case |
| TC064        | Verify that users can like and comment on community posts        | Users can like or comment, and interactions are reflected immediately    | R005      | Positive test case |
| TC065        | Verify that community posts are displayed in chronological order | Posts are ordered from newest to oldest in the feed   | R005      | Positive test case |

---
### **5. 👥 Community Features Requirements**
---
#### **5.1 👤 User Profiles Test Cases**

---
#### **5.2 👥 Social Features Test Cases**
| Test Case ID | Objective                                            | Test Type | Expected Result                                                                | Actual Result                                                | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | ---------------------------------------------------- | --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------ | ------ | --------- | -------- | ----------- | ---------- |
| TC068        | Verify that users can follow other community members | Manual    | Users can follow/unfollow other community members successfully                 | Unable to follow/unfollow other community members            | Fail ❌ | D001      | Major    | Keamogetswe | 2025-11-17 |
| TC069        | Verify that news feed displays community activities  | Manual    | News feed shows latest activities (posts, likes, comments) from followed users | News feed did not update or show latest community activities | Fail ❌ | D002      | Major    | Keamogetswe | 2025-11-17 |

---
---
| Test Case ID | Feature | Objective | Expected Result | Risk Link  | Notes |
|--------------|----------|------------|----------------|----------------| ----------------|
| |  | |  | |

### 1.4 User Session Management (localStorage)
| Test Case ID | Objective                                              | Expected Result                                                 | Risk ID |
|--------------|--------------------------------------------------------|-----------------------------------------------------------------|---------|
| TC-014  | Verify session data is stored in localStorage after login | localStorage contains session key | R-003    |
| TC-015  | Verify user session persists after page refresh        | User remains logged in; localStorage values persist | R-003    |
| TC-016  | Verify session persists after reopening browser tab    | User remains logged in; session data still stored in localStorage | R-003|
| TC-017  | Verify session data is cleared after logout            | localStorage entries removed | R-003    |
| TC-018  | Verify access restricted when localStorage cleared manually | User is logged oute after refresh | R-003    |

---


### **2. 🗑️ Waste Management Requirements**

---
### 2.1 Pickup Scheduling



### 2.2 Request Management Test Cases


### 🔒  Data Management Requirements
#### Data Persistence
| Test Case ID | Objective | Expected Result | Risk Link  |
|--------------|------------|----------------|----------------|
|TC | Verify that user data is stored in localStorage | User data should be present in localStorage in the correct format |  |
|TC | Verify data persists across browser sessions | Previously stored user data should be available and correctly displayed |  |
| |  | |  |
| |  | |  |

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

## **Non-Functional Test Cases**

This section focuses on testing the system's non-functional requirements, which define how the system performs rather than what it does. It includes aspects such as performance, usability, reliability, security, and compatibility. Non-functional test cases ensure that the system meets quality standards and provides a good user experience under expected conditions.

------
### 📱 User Interface Requirements
---
### Table .1: Test cases for Responsive Design
| Test Case ID |  Objective | Expected Result | Risk Link  |
|--------------|------------|----------------|----------------|
|TC-0 | Verify responsiveness when resizing the browser window dynamically | Layout adapts in real-time without breaking or losing functionality | R-008 |
|TC-0 | Verify the system displays correctly on desktop screens (1920×1080 and above)| All UI elements render properly and no horizontal scrolling occurs| R-008 |
|TC-0 | Verify the system displays correctly on tablet screens (768px to 1024px) | Layout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur | R-008 |
|TC-0 | Verify the system displays correctly on mobile phones (320px to 767px)| Layout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur| R-008 |


### Table .2: Test cases for Accessibility (Manual Testing )
| Test Case ID | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|
|TC-0 |Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | All text and UI elements meet required contrast ratios | R-008|
|TC-0 |Verify zooming to 200% does not break layout | Page remains usable and responsive at 200% zoom | R-008 |
|TC-0 |Verift that the system support keyboard navigation | All fields accessible and focusable using **Tab** and **Enter** | R-008 |
|TC-0 |Verify all meaningful images have descriptive alt text | Images have descriptive alt text | R-008 |
|TC-0 |Verify Screen Reader Announces Form Field Labels Correctly| Screen reader announce each field correctly| R-008 |

### Table .2: Test cases for Accessibility (Lighthouse - Dev Tools )
| Test Case ID | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|
|TC-0 |Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | All text and UI elements meet required contrast ratios | R-008|
|TC-0 |  | | R-008 |
|TC-0 |  | | R-008 |
|TC-0 |  | | R-008 |

### Table .2: Test cases for Accessibility (SonarQube)
| Test Case ID | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|
|TC-0 |Verify that form fields include labels or ARIA-labels |  | R-008|
|TC-0 |  |  | R-008 |
|TC-0 |  | | R-008 |
|TC-0 |  | | R-008 |


### Table .1: Test cases for Navigation
| Test Case ID |  Objective | Expected Result | Risk Link  |
|--------------|------------|----------------|----------------|
|TC-0 | Verify navigation menu is easy to understand | Navigation menu is clearly visible with descriptive labels and accessible on all main pages | R013 |
|TC-0 | Verify navigation menu links work correctly  | Each menu item redirects to the correct page without errors | R013 |
|TC-0 | Verift that the system show breadcrumbs for complex pages |Breadcrumbs appear and show the correct page hierarchy |  R013 |
|TC-0 | Verify search bar visibility and returns relevant results | Search bar is visible and shows results relevant to the keyword are displayed | R013 |

---
### 🔒  Data Management Requirements
#### Data Persistence
| Test Case ID | Objective | Expected Result | Risk Link  |
|--------------|------------|----------------|----------------|
|TC | Verify that the system shall handle localStorage limitations gracefully| System should show a clear error message or handle overflow without crashing |  |

#### Data Validation
| Test Case ID | Feature | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|----------------|
| |  | |  |

---

### 🚀 Performance Requirements
#### Response Time


| Test Case ID | Feature | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|----------------|
| |  | |  |

#### Browser Compatibility
| Test Case ID | Feature | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|----------------|
| TC | Verify system works on Google Chrome (latest 2 versions) by performing core functionalities (login, form submission, navigation)| |  |
| TC | Verify system works on Mozilla Firefox (latest 2 versions) by performing core functionalities (login, form submission, navigation)| |  |
| TC | Verify system works on Microsoft Edge (latest 2 versions) by performing core functionalities (login, form submission, navigation)| |  |
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


---




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
