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
| TC023        | Verify scheduling a pickup without login         | System should restrict access and redirect to login page | R002    | Negative test case |

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
| TC034        | Invalid pickup request (Very long text >200 chars)                                                   | System truncates input or shows error for long text                                   | R006    | Negative test case |
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
| TC046        | Verify that users receive notifications for pickup request status changes.    | User receives notifications (email, SMS, or in-app) whenever the status of a pickup changes. | R010    | Positive test case |
| TC047        | Verify that users can add feedback after a pickup is completed.               | Users can submit feedback, and the system stores it associated with the completed pickup.    | R002    | Positive test case |

---
### **3. 📊 Dashboard & Analytics Requirements**
---
#### Table 3.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                                              | Expected Result                                                                                                                                | Risk ID | Notes              |
| ------------ | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------ |
| TC048        | Verify that the user dashboard displays personalized information for logged-in users   | Dashboard shows recent pickup requests, upcoming scheduled pickups, achievement badges, and quick action buttons                               | R013    | Positive test case |
| TC049        | Verify that the system shall calculate and display user's environmental impact metrics | Dashboard correctly calculates and displays total waste diverted, CO2 emissions saved, and trees equivalent saved                              | R013    | Positive test case |
| TC050        | Verify that the system awards badges for various achievements                          | User is awarded badges based on milestones (e.g., number of pickups completed, environmental impact) and badges are displayed on the dashboard | R013    | Positive test case |

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
#### Table 5.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                          | Expected Result                                                                   | Risk Link | Notes              |
| ------------ | ------------------------------------------------------------------ | --------------------------------------------------------------------------------- | --------- | ------------------ |
| TC066        | Verify that users can view and edit their profile information      | Users can view their profile details and successfully edit and save changes       | R013      | Positive test case |
| TC067        | Verify that users can upload a profile picture                     | Users can upload a profile picture and it is displayed correctly on their profile | R013      | Positive test case |


---
#### **5.2 👥 Social Features Test Cases**
#### Table 5.2.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                            | Expected Result                                                                | Risk Link | Notes              |
| ------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------ | --------- | ------------------ |
| TC068        | Verify that users can follow other community members | Users can follow/unfollow other community members successfully                 | R005      | Positive test case |
| TC069        | Verify that news feed displays community activities  | News feed shows latest activities (posts, likes, comments) from followed users | R005      | Positive test case |

---
### **6. ⚙️ Administrative Functions Requirements**
---
#### **6.1 Request Management Test Cases**
#### Table 6.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                                         | Expected Result                                                          | Risk Link | Notes              |
| ------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------ | --------- | ------------------ |
| TC070        | Verify that admins can view all pickup requests                   | Admins can see a list of all pickup requests with details                | R004      | Positive test case |
| TC071        | Verify that admins can approve, reject, or modify pickup requests | Admins can successfully approve, reject, or edit requests                | R004      | Positive test case |
| TC072        | Verify that admins can assign pickup dates and times              | Admins can assign or update pickup dates and times and changes are saved | R004      | Positive test case |
| TC073        | Verify that admins can filter and search pickup requests          | Filtering and search return correct requests based on criteria           | R004      | Positive test case |
| TC074  | Verify that admins can receive or reply to feedback | Feedback system should accept and reply properly | R004|  |

---
#### **6.2 User Management  Test Cases**
#### Table 6.2.1 Test cases for **manual testing** 📝
| Test Case ID | Objective | Expected Result | Risk Link  | Notes |
|--------------|-------------|----------------|----------------| ----------------|
| TC075  | Verify that admins can view all registered users |  Admin can successfully view a complete list of all registered system users | R004| |
| TC076  | Verify that admins can change user roles  | Admin can update user roles and changes are saved and reflected immediately  | R004| |
| TC077 | Verify that admins can suspend or delete accounts |   Admin can suspend or delete user accounts and the system updates the status | R004 | |
| TC078 | Verify that system provides user activity reports| Admin can view activity reports  | R004| |

---
#### **6.3 Content Moderation Test Cases**
#### Table 6.3.1 Test cases for **manual testing** 📝
| Test Case ID | Objective | Expected Result | Risk Link  | Notes |
|--------------|-------------|----------------|----------------| ----------------|
| TC079  | |  | R004| |
|  TC080 | |  | R004| |
|  TC081 | |  | R004| |
| TC082| |  | | R004|
| TC083| |  | | R004 |

---
### ***7. 🔔 Notification System Requirements**
---
#### 7.1 System Notifications
#### Table 7.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective | Expected Result | Risk Link  | Notes |
|--------------|-------------|----------------|----------------| ----------------|
| TC084  | |  | R010 | |
| TC085 | |  | R010 | |
| TC086 | |  | R010 | |
| TC087 | |  | R010 | |

---
### **8. 🔒  Data Management Requirements**
---
### 8.1 Data Persistence (localStorage)
#### Table 8.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective                                              | Expected Result                                                 | Risk ID |
|--------------|--------------------------------------------------------|-----------------------------------------------------------------|---------|
| TC088   | Verify session data is stored in localStorage after login | localStorage contains session key | R003    |
| TC089   | Verify user session persists after page refresh        | User remains logged in; localStorage values persist | R003    |
| TC090   | Verify session persists after reopening browser tab    | User remains logged in; session data still stored in localStorage | R003|
| TC091 | Verify session data is cleared after logout            | localStorage entries removed | R003    |
| TC092  | Verify access restricted when localStorage cleared manually | User is logged oute after refresh | R003    |

---

### 9. 📞 Support and Maintenance
### 9.1 Help System
#### Table 9.1.1 Test cases for **manual testing** 📝
| Test Case ID    | Objective                                                                                                     | Expected Result                                                                                       | Risk ID   | Notes|
| --------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------- | --------------|
| TC093 |  Ensure users can access the FAQ section and all content is displayed correctly. | FAQ page loads with all questions and answers correctly | R010 |
| TC094 | Verify that contact information for support is displayed | Support email, phone, and/or chat options are visible and clickable | R010 |
| TC095 | |  | | R010 |

---

## **📊 Non-Functional Test Cases**

This section focuses on testing the system's non-functional requirements, which define how the system performs rather than what it does. It includes aspects such as performance, usability, reliability, security, and compatibility. Non-functional test cases ensure that the system meets quality standards and provides a good user experience under expected conditions.

---
### 10. 📞 Support and Maintenance
### 10.1 System Monitoring
#### Table 9.1.1 Test cases for **manual testing** 📝
| Test Case ID | Objective | Expected Result | Risk Link  | Notes |
|--------------|-------------|----------------|----------------| ----------------|
|  TC096 | |  | | R014 |
|  TC097 | |  | | R014|

---
### 11. 📱 User Interface Requirements
---
#### 11.1 Responsive Design
#### Table 10.1.1: Test cases for **manual testing** 📝
| Test Case ID |  Objective | Expected Result | Risk Link  |
|--------------|------------|----------------|----------------|
|TC98 | Verify responsiveness when resizing the browser window dynamically | Layout adapts in real-time without breaking or losing functionality | R008 |
|TC99 | Verify the system displays correctly on desktop screens (1920×1080 and above)| All UI elements render properly and no horizontal scrolling occurs| R008 |

---
#### Table 11.1.2: Test cases for **automated testing** 📝
| Test Case ID |  Objective | Expected Result | Risk Link  |
|--------------|------------|----------------|----------------|
|TC100 | Verify the system displays correctly on tablet screens (768px to 1024px) | Layout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur | R008 |
|TC101 | Verify the system displays correctly on mobile phones (320px to 767px)| Layout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur| R008 |

---
#### 11.2 Accessibility
### Table 10.2.1: Test cases for Accessibility (Manual Testing )
| Test Case ID | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|
|TC102 |Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | All text and UI elements meet required contrast ratios | R008|
|TC103 |Verify zooming to 200% does not break layout | Page remains usable and responsive at 200% zoom | R008 |
|TC104 |Verift that the system support keyboard navigation | All fields accessible and focusable using **Tab** and **Enter** | R008 |
|TC105 |Verify all meaningful images have descriptive alt text | Images have descriptive alt text | R-008 |

---
#### Table 11.2.2: Test cases for Accessibility (automated Testing )
| Test Case ID | Objective | Expected Result | Risk Link  |
|--------------|----------|------------|----------------|
|TC106 |Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | All text and UI elements meet required contrast ratios | R008|
|TC107 |Verify Screen Reader Announces Form Field Labels Correctly| Screen reader announce each field correctly| R008 |

---
#### 11.3 Navigation
#### Table 10.3.1: Test cases for manual testing
| Test Case ID |  Objective | Expected Result | Risk Link  |
|--------------|------------|----------------|----------------|
|TC108 | Verify navigation menu is easy to understand | Navigation menu is clearly visible with descriptive labels and accessible on all main pages | R008 |
|TC109 | Verify navigation menu links work correctly  | Each menu item redirects to the correct page without errors | R008 |
|TC110 | Verift that the system show breadcrumbs for complex pages |Breadcrumbs appear and show the correct page hierarchy |  R008 |
|TC111 | Verify search bar visibility and returns relevant results | Search bar is visible and shows results relevant to the keyword are displayed | R008 |

---
### 12. 🔒  Data Management Requirements
---
#### 12.1 Data Persistence
#### Table 11.1.1: Test cases for manual testing
| Test Case ID | Objective | Expected Result | Risk Link  | Notes |
|--------------|-------------|----------------|----------------| ----------------|
|  TC114 | |  | R007 |  |
|  TC115 | |  | R007 |  |

#### Table 12.1.2: Test cases for Automated testing
| Test Case ID | Objective | Expected Result | Risk Link  | Notes |
|--------------|-------------|----------------|----------------| ----------------|
| TC112  | |  | R006 | |
| TC113  | |  | R007| |

---
### 13. 🚀 Performance Requirements
---

#### 13.1 Response Time
#### Table 13.1.1: Test cases for Automated testing
| Test Case ID | Objective | Expected Result | Risk Link  |  |
|--------------|----------|------------|----------------|----------------|
|TC116  |  | | R008 | |
|TC117  |  | | R008 | |

---

#### 13.2 Browser Compatibility
#### Table 13.2.1: Test cases for Manual testing
| Test Case ID | Objective | Expected Result | Risk Link |  Notes |
|--------------|----------|------------|----------------|----------------|
| TC118 | Verify system works on Google Chrome (latest 2 versions) by performing core functionalities (login, form submission, navigation)| Application functions correctly without layout issues, errors, or crashes| R009 |
| TC119 | Verify system works on Mozilla Firefox (latest 2 versions) by performing core functionalities (login, form submission, navigation)| Application functions correctly without layout issues, errors, or crashes | R009 |
| TC120 | Verify system works on Microsoft Edge (latest 2 versions) by performing core functionalities (login, form submission, navigation)| Application functions correctly without layout issues, errors, or crashes | R009 |

------
### 14 📋 Error Handling Requirements
---
#### 14.1 User-Friendly Errors
#### Table 14.1.1: Test cases for Manual testing
| Test Case ID | Objective                                                            | Expected Result                                                                                | Risk Link | Notes        |
| ------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------- | ------------ |
| **TC125**    | Verify that the system provides guidance for resolving common issues | For common issues (e.g., invalid input, login failure), the system shows guidance or help tips |  R006  | **Positive Test Case** |

---

#### Table 14.1.2: Test cases for Automated testing
| Test Case ID | Objective                                       | Expected Result                                                | Risk Link | Notes        |
| ------------ | ----------------------------------------------- | -------------------------------------------------------------- | --------- | ------------ |
| **TC121**    | Verify system handles network errors on Fast 3G | Network errors under Fast 3G connection are handled gracefully | R011     | **Positive** |
| **TC122**    | Verify system handles network errors on Slow 3G | Network errors under Slow 3G connection are handled gracefully | R011 | **Negative** |
| **TC123**    | Verify system handles Offline scenario          | Offline mode shows friendly message + blocks network actions   | R011       | **Positive** |
| **TC124**    | Verify error messages are clear and actionable  | All error messages are easy to understand and guide the user   | R010      | **Positive** |

---
#### 14.2 Form Validation
#### Table 14.2.1: Test cases for Automated testing
| Test Case ID | Objective                                                         | Expected Result                                                                                                     | Risk Link | Notes        |
| ------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------- | ------------ |
| **TC126**    | Verify that the system validates forms in real-time               | Form fields are validated instantly as the user types or selects options; invalid input triggers immediate feedback | R006| **Positive** |
| **TC127**    | Verify that the system prevents form submission with invalid data | Form cannot be submitted when required fields are empty or invalid; user is notified of errors                      | R006 | **Positive** |
| **TC128**    | Verify that the system highlights validation errors clearly       | Invalid fields are visually highlighted so user can identify and fix them easily                                    | R006 | **Positive** |

---

## Boundary and Edge Case Test Cases**

### Table 15.1 Manual testing
| Test Case ID | Objective                                                                          | Expected Result                                                | Risk Link | Notes        |
| ------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------- | ------------ |
| **TC129**    | Verify date selection rejects today and past dates; allows minimum date (tomorrow) | Dates today and earlier are rejected with validation message   | R006 | **Negative** |
| **TC130**    | Verify date selection rejects dates beyond 30 days                                 | Dates >30 days from today are rejected with validation message | R006  | **Negative** |

---
### Table 15.2 Automated Testing
| Test Case ID | Objective                                            | Expected Result                                                     | Risk Link | Notes        |
| ------------ | ---------------------------------------------------- | ------------------------------------------------------------------- | --------- | ------------ |
| **TC131**    | Verify name field accepts 2–50 characters            | Names with <2 or >50 characters are rejected; valid length accepted | R006  | **Negative** |
| **TC132**    | Verify email field accepts valid format              | Invalid emails rejected; valid emails accepted                      | R006   | **Positive** |
| **TC133**    | Verify password field enforces minimum 8 characters  | Passwords <8 characters are rejected                                | R006 | **Negative** |
| **TC134**    | Verify instructions field accepts 0–200 characters   | Instructions >200 characters are rejected                           | R006| **Negative** |
| **TC135**    | Verify special characters in name/email/instructions | System accepts valid special characters                             | R006   | **Positive** |
| **TC136**    | Verify Unicode and international characters work     | System accepts Unicode/international characters                     | R006 | **Negative** |
| **TC137**    | Verify very long inputs are rejected                 | Inputs exceeding maximum length are rejected                        | R006 | **Negative** |
| **TC138**    | Verify empty or whitespace-only inputs are rejected  | Empty or whitespace-only inputs are rejected                        | R006 | **Positive** |
