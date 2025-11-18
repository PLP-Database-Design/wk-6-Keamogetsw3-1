# Test Case Execution Report
This section provides a detailed summary of the test cases executed during Phase 3 (test execution) of this project.  
The purpose of this report is to validate that the application meets its functional requirements.

---
# **Functional Testing**

### **1 🔐 Authentication System Requirements**
---
#### Table 1.1 👤 User Registration Test Cases

| Test Case ID | Test Description                           | Test Type  | Expected Result                        | Actual Result                  | Status | Defect ID | Severity | Tester        | Date       |
| ------------ | ------------------------------------------ | ---------- | -------------------------------------- | ------------------------------ | ------ | --------- | -------- | ------------- | ---------- |
| TC001        | Verify registration with valid credentials | Manual | User should be registered successfully | User successfully registered   | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC002        | Verify registration with invalid email     | Manual | System should ask for valid email      | System asked for correct email | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC003        | Verify registration with empty name field  | Manual | System should ask for Name             | System asked for full name     | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC004        | Verify registration with empty email       | Manual | System should ask for Email            | System asked for Email         | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC005        | Verify registration with empty password    | Manual| System should ask for Password         | System asked for Password      | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC006        | Verify registration with valid credentials | Automated | User should be registered successfully | User successfully registered   | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC007        | Verify registration with invalid email     | Automated | System should ask for valid email      | System asked for correct email | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC008        | Verify registration with empty name field  | Automated | System should ask for Name             | System asked for full name     | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC009        | Verify registration with empty email       | Automated | System should ask for Email            | System asked for Email         | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC010        | Verify registration with empty password    | Automated | System should ask for Password         | System asked for Password      | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |

---
#### Table 1.2 👤 User Login Test Cases

| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC011      | Verify login with valid credentials       | Manual | User should be logged in successfully | User successfully logged in  | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC012      | Verify login with invalid password        | Manual| System should display error  | User succefully logged in | Fail ❌ | [D-002](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31)       | Critical     | Keamogetswe | 2025-11-11 |
| TC013      | Verify login without email       | Manual| System should display email required error | Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC014      | Verify login without password    | Manual | System should display password required error| Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC015      | Verify login with non-existent user       | Manual | System should display error           | User logged in succefully   | Fail ❌ |[D-003](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32)        | Critical       | Keamogetswe | 2025-11-12 |
| TC016      | Verify login with valid credentials       | Automated | User should be logged in successfully | User successfully logged in  | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC017      | Verify login with invalid password        | Automated  | System should display error  | User succefully logged in | Fail ❌ | [D-002](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31)       | Critical     | Keamogetswe | 2025-11-11 |
| TC018      | Verify login without email       | Automated  | System should display email required error | Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC019      | Verify login without password    | Automated | System should display password required error| Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC020      | Verify login with non-existent user       | Automated  | System should display error           | User logged in succefully   | Fail ❌ |[D-003](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32)        | Critical       | Keamogetswe | 2025-11-10 |

---

#### Table 1.3 👤 User Logout Test Cases
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC021      | Verify logout       | Manual| User should be logged out successfully | User successfully logged out  | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC022      | Verify user cannot access dashboard after logout  | Manual | Attempting to access dashboard redirects to login page  | User redirected to login page | Pass ✅ | — | —  | Keamogetswe | 2025-11-12 |
| TC023      | Verify scheduling a pickup without login  | Manual| System should restrict access and redirect to login page | Pick-up succefully submitted   | Fail ❌ |[D-004](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33)        | Critical      | Keamogetswe | 2025-11-12 |
| TC024      | Verify user can successfully login then log out | Automated | User should be logged out successfully | |  |  |  |  |  |

---
#### Table 1.4: 👤 Role-Based Access Test Cases
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC025 | Verify system creates a new user account with “User” role upon successful registration | Manual  | System automatically assigns the “User” role to newly registered accounts |  System assigned the “User” role to newly registered accounts| Pass ✅  | — | — | Keamogetswe  | 2025-11-12 |
| TC026 | Verify system supports two user roles: “User” and “Admin”. each user can have only one valid role assigned| Manual  | System supports two user roles: “User” and “Admin” |  System supports two user roles: “User” and “Admin” and correctly assign role| Pass ✅  | — | — | Keamogetswe  | 2025-11-12 |
| TC027 | Verify only Admins can access Admin Dashboard | Manual  | “User” role doesnt show Admin dashboard. “Admin” role can access successfully | “User” role doesnt show Admin dashboard. “Admin” role can access successfully | Pass ✅  | — | — | Keamogetswe. Sally Trizer | 2025-11-12 |
| TC028 |Verify direct URL access to Admin Dashboard is blocked for non-admin users | Manual | System restricts access and redirects to “Access Denied” or “Login” page | System restricts access and shows "This page isn’t working" | Pass ✅  | — | — | Keamogetswe | 2025-11-12 |

---
### **2. 🗑️ Waste Management Requirements**
---

#### Table 2.1: 🚚 Pickup Scheduling Test Cases
| Test Case ID | Test Description                                      | Test Type  | Expected Result                                         | Actual Result | Status | Defect ID | Severity | Tester | Date       |
|--------------|------------------------------------------------------|-----------|--------------------------------------------------------|---------------|--------|-----------|---------|--------|-----------|
| TC029  | Valid pickup request - Verify system accepts submission and displays confirmation message (“Pickup scheduled successfully”)   | Manual | Pickup request is successfully created | Confirmation message displayed   | Pass ✅   | —  | —  | Sally Trizer  | 2025-11-12 |
| TC030  | Invalid pickup request (no data)                     | Manual| System shows validation errors for empty fields    | System shows validation errors for empty fields  | Pass ✅ |  —  |  —  |   Keamogetswe   | 2025-11-13 |
| TC031  | Invalid pickup request (Yesterday’s date)            | Manual| System does not allow scheduling for past date   | Confirmation message displayed  | Fail ❌ | [D-005](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/34) |  Major |    Keamogetswe      |    2025-11-13       |
| TC032  | Invalid pickup request (empty Waste Type) | Manual | System shows error indicating Waste Type is required |  System showed error indicating Waste Type is required | Pass ✅  | — | — | Keamogetswe  |  2025-11-14  |
| TC033  | Invalid pickup request (empty Location)   | Manual| System shows error indicating Location is required |   System showed error indicating Location is required |  Pass ✅  | — |  —  | Keamogetswe  | 2025-11-14  |
| TC034  | Invalid pickup request (Very long text >200 chars)   | Manual| System truncates input or shows error for long text  | Confirmation message displayed   |  Fail ❌| [D-006](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41) | Minor |  Keamogetswe  | 2025-11-14  |
| TC035  | The system shall prevent scheduling multiple pickups for the same date | Manual| System prevents creating duplicate pickups for the same date |   Confirmation message displayed   | Fail ❌ | [D-007](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42)| Major |  Keamogetswe  | 2025-11-14 |
| TC036  | Valid pickup request - Verify system accepts submission and displays confirmation message (“Pickup scheduled successfully”)   | Automated | Pickup request is successfully created | Confirmation message displayed   | Pass ✅   | —  | —  | Keamogetswe| 2025-11-16 |
---

#### Table 2.2: 📋 Request Management
| Test Case ID | Objective                                                                  | Test Type | Expected Result                 # CleanCity Test Report – Pickup Request Module

| ID    | Objective                                                        | Test Type | Expected Result                                             | Actual Result                                              | Status   | Defect ID                                                                                       | Severity | Tester         | Date       |
|-------|-----------------------------------------------------------------|-----------|------------------------------------------------------------|------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------|---------|----------------|------------|
| TC037 | Verify the system displays the user’s pickup request history.   | Manual    | User can view all past and current pickup requests with details. | User cannot view all past and current pickup requests with details. | Fail ❌  | [D012](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/61) | Major   | Keamogetswe    | 2025-11-13 |
| TC038 | Verify completed and cancelled requests appear in history.      | Manual    | Completed and cancelled requests are shown correctly.     | Completed and cancelled requests are not shown at all      | Fail ❌  | [D013](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/62) | Major   | Keamogetswe    | 2025-11-13 |
| TC039 | Verify user can cancel a pending pickup request.                | Manual    | Pending request changes status to “Cancelled.”            | User cannot cancel a pending pickup request.              | Fail ❌  | [D014](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/63) | Major   | Sally Trizer   | 2025-11-12 |
| TC040 | Verify completed or cancelled requests cannot be cancelled again.| Manual   | System prevents double cancellation.                       | N/A                                                        | Fail ❌  | [D015](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/64) | Major   | Sally Trizer   | 2025-11-12 |
| TC041 | Verify modification of pickup details at least 24 hours before schedule. | Manual | User can update details successfully.                      | N/A                                                        | Fail ❌  | [D016](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/65) | Major   | Sally Trizer   | 2025-11-12 |
| TC042 | Verify modification not allowed within 24 hours of scheduled time. | Manual  | System prevents modification and shows warning.           | N/A                                                        | Fail ❌  | [D017](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/66) | Major   | Sally Trizer   | 2025-11-12 |
| TC043 | Verify system displays correct request status for each pickup.  | Manual    | Status correctly shows Pending, Confirmed, Completed, or Cancelled. | Pickup status are not listed or visible                     | Fail ❌  | [D018](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/67) | Major   | Sally Trizer   | 2025-11-12 |
| TC044 | Verify request status updates automatically after completion/cancellation. | Manual | Status updates dynamically after change.                  | Pickup status are not listed or visible                     | Fail ❌  | [D019](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/68) | Major   | Sally Trizer   | 2025-11-12 |


---

#### Table 2.3: 📋 Request Tracking

| Test Case ID | Objective                                                                     | Test Type | Expected Result                                                                              | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ----------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC045        | Verify that the system provides real-time status updates for pickup requests. | Manual    | Status of each pickup request updates dynamically without requiring page refresh.            |               |    Fail ❌    |[D020](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/69) | Major |     Sally Trizer   |  2025-11-16 |
| TC046        | Verify that users receive notifications for pickup request status changes.    | Manual    | User receives notifications (email, SMS, or in-app) whenever the status of a pickup changes. |               |    Fail ❌    | [D021](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/70) | Major   |     Sally Trizer   | 2025-11-16  |
| TC047        | Verify that users can add feedback after a pickup is completed.               | Manual    | Users can submit feedback, and the system stores it associated with the completed pickup.    |          Users can add feedback but it not asscoiated with complete pick up     |  Fail ❌    | [D022](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/71) | Major |  Keamogetswe  | 2025-11-16  |

---
### **3. 📊 Dashboard & Analytics Requirements**
---
#### Table 3.1:
| Test Case ID | Objective                                                                              | Test Type | Expected Result                                                                                                   | Actual Result                                                       | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | -------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------ | --------- | -------- | ----------- | ---------- |
| TC048        | Verify that the user dashboard displays personalized information for logged-in users   | Major   | Dashboard shows recent pickup requests, upcoming scheduled pickups, achievement badges, and quick action buttons  | Dashboard does not show anything personlised information |Fail ❌ | [D023](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/72) | Minor  | Keamogetswe | 2025-11-16  |
| TC049        | Verify that the system shall calculate and display user's environmental impact metrics | Minor    | Dashboard correctly calculates and displays total waste diverted, CO2 emissions saved, and trees equivalent saved |None of the impact metric is shown | Fail ❌| [D024](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/73)|   Minor | Keamogetswe | 2025-11-16  |
| TC050        | Verify that the system awards badges for various achievements                          | Manual    | User is awarded badges based on milestones and badges are displayed on the dashboard | badges are displayed on the dashboard  | Fail ❌  | [D025](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/74) | Cosmetic | Keamogetswe  | 2025-11-16 |

---
### **4. 📝 Content Management Requirements**
---
#### Table 4.1 ✍️ Blog System Test case execusion report
| Test Case ID | Objective                                                       | Test Type  | Expected Result                                                  | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | --------------------------------------------------------------- | ---------- | ---------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC051        | Verify that the blog list page loads successfully | Manual| Blog page loads and displays available blog posts | Blog page loads and displays available blog posts | Pass ✅ | — |  —   |    Keamogetswe    |   2025-11-12   |
| TC052        | Verify that users can view a single blog post | Manual | Blog post content (title, date, body, images) displays correctly | Blog post content (title, date, body, images) displays correctly |Pass ✅ |  — |  — | Keamogetswe |    2025-11-16  |
| TC053        | Verify that users can interact with blog content (like/comment) | Manual | User can click like or submit a comment successfully| User can click like or submit a comment successfully |Pass ✅ | — | — |Keamogetswe |   2025-11-16   |
| TC054        | Verify that admins can create a blog post| Manual | Blog post is saved and appears in the list | Admins cannot create a blog post | Fail ❌ |  [D026](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/75)| Major | Sally Trizer |   2025-11-12   |
| TC055        | Verify that admins can edit an existing blog post| Manual | Updated content is saved and reflected on the blog page | Admins cannot edit a blog post | Fail ❌ |[D027](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/76)| Major |Keamogetswe |    2025-11-16  |
| TC056        | Verify that admins can delete a blog post | Manual | Blog post is removed and no longer visible |Admins cannot de;ete a blog post | Fail ❌ | [D028](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/77)| Major  | Keamogetswe |  2025-11-16     |
| TC057        | Verify that categories/tags can be assigned to a blog post | Manual | Tag/category appears on post and filtering works |  Tag/category appears on post and filtering works | Pass ✅ | — | — | Keamogetswe | 2025-11-16 |

---
#### Table 4.2  👁️ Awareness Section Test case execusion report
| Test Case ID | Objective                                                                   | Test Type  | Expected Result                                                                           | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | --------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC058        | Verify that rotating eco tips are displayed every 5 seconds  | Manual | Eco tips rotate automatically every 5 seconds|    Eco tips rotate automatically every 5 seconds | Pass ✅ | — | — | Keamogetswe | 2025-11-16 |
| TC059        | Verify that users can access interactive quizzes about environmental topics | Manual  | Quiz opens and users can answer questions interactively| Quiz opens and users can answer questions interactively | Pass ✅  | — | — | Keamogetswe | 2025-11-16 |
| TC060        | Verify that quiz scores are tracked and explanations are provided | Manual  | After completing a quiz, the score is displayed and correct answer explanations are shown | After completing a quiz, the score is displayed and correct answer explanations are shown | Pass ✅  | — | — | Keamogetswe | 2025-11-16 |
| TC061        | Verify that environmental infographics with statistics are displayed | Manual  | Infographics appear with accurate statistics and proper formatting | Infographics appear with accurate statistics and proper formatting | Pass ✅  | — | — | Keamogetswe | 2025-11-16 |
| TC062        | Verify that action buttons link to other features | Manual | Clicking action buttons navigates to the correct related feature or page | Clicking action buttons navigates to the correct related feature or page  | Pass ✅  | — | — | Keamogetswe | 2025-11-16 |

---
#### Table 4.3  🤝 Community Feed Test case execusion report
| Test Case ID | Objective                                                        | Test Type | Expected Result                                                          | Actual Result                                                            | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | ---------------------------------------------------------------- | --------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------ | --------- | -------- | ----------- | ---------- |
| TC063        | Verify that users can create community posts                     | Manual    | Users can create and submit a post, and it appears in the community feed | Users can create and submit a post and it appears in the community feed | Pass ✅ | —  | —   | Keamogetswe | 2025-11-15 |
| TC064        | Verify that users can like and comment on community posts        | Manual    | Users can like or comment, and interactions are reflected immediately    | Users can like or comment and interactions are reflected immediately    | Pass ✅ | —         | —  | Keamogetswe | 2025-11-15 |
| TC065        | Verify that community posts are displayed in chronological order | Manual    | Posts are ordered from newest to oldest in the feed | Posts are ordered from newest to oldest in the feed  | Pass ✅ | —   | —   | Keamogetswe | 2025-11-15 |

---
### **5. 👥 Community Features Requirements**
---
#### Table 5.1  🤝 Community Feed Test case execusion report
| Test Case ID | Objective                                                     | Test Type | Expected Result                                                                   | Actual Result                                                               | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | ------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------ | --------- | -------- | ----------- | ---------- |
| TC066        | Verify that users can view and edit their profile information | Manual    | Users can view their profile details and successfully edit and save changes       | Users can view their profile details and successfully edit and save changes | Pass ✅ | —         | —        | Keamogetswe | 2025-11-09 |
| TC067        | Verify that users can upload a profile picture                | Manual    | Users can upload a profile picture and it is displayed correctly on their profile | Uploading image returns a 500 server error                                  | Fail ❌ | [D029](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/78)    | Comestic   | Keamogetswe | 2025-11-16 |


---
#### Table 5.2  🤝 Community Feed Test case execusion report
| Test Case ID | Objective                                            | Test Type | Expected Result                                                                | Actual Result                                                | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | ---------------------------------------------------- | --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------ | ------ | --------- | -------- | ----------- | ---------- |
| TC068        | Verify that users can follow other community members | Manual    | Users can follow/unfollow other community members successfully                 | Unable to follow/unfollow other community members            | Fail ❌ |[D030](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/79) | Minor    | Keamogetswe | 2025-11-17 |
| TC069        | Verify that news feed displays community activities  | Manual    | News feed shows latest activities (posts, likes, comments) from followed users | News feed did not update or show latest community activities | Fail ❌ | [D031](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/80)   | Minor    | Keamogetswe | 2025-11-17 |

---
### **6. ⚙️ Administrative Functions Requirements**
---
### Table 6.1: Admin login and registratin


#### Table 6.2 Request Management Test case execusion report
| Test Case ID | Test Description                                           | Test Type          | Expected Result                                                               | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ---------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC070    | Verify that admins can view all pickup requests | Manual | Admin can view a full list of all pickup requests with complete details | Admin can view a full list of all pickup requests but not the complete details  | Pass ✅ |  — |  — | Keamogetswe| 2025-11-17 |
| TC071   | Verify that admins can approve, reject or modify requests | Manual | Admin can successfully approve, reject or modify any pickup request | Admin can successfully approve, reject or modify any pickup request  | Fail ❌ | [D032](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/81) | Major | Keamogetswe |2025-11-17 |
| TC072   | Verify that admins can assign pickup dates and times       | Manual | Admin can set or update pickup dates/times and changes are saved successfully | Admin cannot set or update pickup dates/times and changes are saved successfully |   Fail ❌ |  [D033](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/82)   | Major | Keamogetswe | 2025-11-17 |
| TC073    | Verify that admins can filter and search pickup requests | Manual | The system returns correct filtered or searched results based on criteria | The system cannot returns correct filtered or searched results based on criteria  |   Fail ❌ | [D034](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/83) |  Minor  | Sally Trizer  | 2025-11-13 |
| TC077    | Verify that admins can receive or reply to feedback | Manual    | Feedback system should accept and reply properly   | Admin unable to receive or reply to feedback  | Fail ❌ |  [D035](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/84) | Major | Sally Trizer  | 2025-11-13  |


---
#### Table 6.3 User Management Test case execusion report
| Test Case ID | Test Description                                 | Test Type | Expected Result                                                               | Actual Result | Status   | Defect ID | Severity | Tester        | Date       |
| ------------ | ------------------------------------------------ | --------- | ----------------------------------------------------------------------------- | ------------- | -------- | --------- | -------- | ------------- | ---------- |
| TC074        | Verify that admins can view all registered users | Manual    | Admin can successfully view a complete list of all registered system users   | Admin unable to view the complete list of registered users | Fail ❌  | [D036](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/85) | Major    | Keamogetswe   | 2025-11-17 |
| TC075        | Verify that admins can change user roles        | Manual    | Admin can update user roles and changes are saved and reflected immediately  | Admin cannot update user roles | Fail ❌  | [D037](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/86) | Major    | Keamogetswe   | 2025-11-17 |
| TC076        | Verify that admins can suspend or delete accounts | Manual    | Admin can suspend or delete user accounts and the system updates the status   | Admin unable to suspend or delete accounts | Fail ❌  | [D038](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/87) | Major    | Keamogetswe   | 2025-11-17 |
| TC077        | Verify that system provides user activity reports | Manual    | Admin can view activity reports                                               | Activity reports displayed correctly | Pass ✅  | —  | — | Keamogetswe   | 2025-11-17 |


---
#### Table 6.3: Content Moderation Test case execusion report
| Test Case ID | Test Description                                             | Test Type | Expected Result                                                                   | Actual Result                                   | Status   | Defect ID | Severity | Tester         | Date       |
| ------------ | ------------------------------------------------------------ | --------- | --------------------------------------------------------------------------------- | ----------------------------------------------- | -------- | --------- | -------- | -------------- | ---------- |
| TC078        | Verify that admins can moderate community posts and comments | Manual    | Admin can view, review, and manage all posts/comments from the moderation panel   | Admin unable to moderate posts/comments        | Fail ❌  | [D039](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/88) | Major    | Keamogetswe   | 2025-11-15 |
| TC079        | Verify that admins can delete inappropriate content          | Manual    | Admin can successfully delete posts/comments and they no longer appear publicly   | Admin unable to delete inappropriate content   | Fail ❌  | [D040](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/89) | Major    | Keamogetswe   | 2025-11-15 |
| TC080        | Verify that users can flag/report inappropriate content     | Manual    | Users can flag posts/comments and reports appear in the admin moderation queue    | Reports do not appear in the moderation queue  | Fail ❌  | [D041](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/90) | Major    | Keamogetswe   | 2025-11-15 |
| TC081        | Verify that admins can create announcements                  | Manual    | Admin can create announcements and they appear on the community/announcement page | Announcements created successfully             | Pass ✅  | -         | -        | Keamogetswe   | 2025-11-15 |
| TC082        | Verify that admins can publish a new blog post               | Manual    | Post appears in blog list                                                        | Blog post failed to publish                     | Fail ❌  | [D042](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/91) | Major    | Sally Trizer  | 2025-11-15 |


---
### **7. 🔔 Notification System Requirements**
---
#### Table 7.1: System Notifications Test case execusion report
| Test Case ID | Test Description                                                                                               | Test Type | Expected Result                                                              | Actual Result                                                      | Status   | Defect ID | Severity | Tester        | Date       |
| ------------ | -------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------- | --------- | -------- | ------------- | ---------- |
| TC082        | Verify that the system displays a notification bell with unread count                                          | Manual    | Notification bell is visible and shows the correct unread notification count | Notification bell displayed correctly                             | Pass ✅  | -         | -        | Keamogetswe   | 2025-11-15 |
| TC083        | Verify that the system shows notifications for pickup updates, blogs, community interactions, and achievements | Manual    | All notification types appear correctly in the notification list             | Notifications displayed correctly                                   | Pass ✅  | -         | -        | Keamogetswe   | 2025-11-15 |
| TC084        | Verify that users can mark notifications as read                                                               | Manual    | Selected notifications change to “read” state and unread counter updates     | Notifications cannot be marked as read; unread counter not updated | Fail ❌  | [D043](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/92) | Minor    | Keamogetswe   | 2025-11-15 |
| TC085        | Verify that the system provides a full notification history                                                    | Manual    | Notification history page displays past notifications in chronological order | Notification history displayed correctly                             | Pass ✅  | -         | -        | Keamogetswe   | 2025-11-15 |

---
### **8 🔒 Data Management Requirements**
---
#### Table 8.1: Data Persistence Test case execusion report
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC086      | Verify session data is stored in localStorage after login    | Manual | localStorage contains session key | localStorage contains a key  `User` | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC087 | Verify user session persists after page refresh | Manual | User remains logged in; localStorage values persist  |User remains logged in; localStorage values persist | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC088 | Verify that session persists after reopening browser tab | Manual  | User remains logged in; localStorage still holds session data  |User remains logged in; localStorage values persist | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC089 | Verify that session data is cleared after logout | Manual | localStorage entry `User` is removed| localStorage entry `User` is removed|Pass ✅ |  — | — | Keamogetswe | 2025-11-12 |
| TC090  | Verify access restriction after localStorage is cleared manually | Manual  | User logged out and redirected to home page| User logged out and redirected to sign in page             |   Pass ✅          | — | — | Keamogetswe | 2025-11-12 |

---
###  **9 📞 Support & Maintenance**
---
#### Table 9.1: Help System Test case execusion report
| Test Case ID | Objective                                                       | Test Type | Expected Result                                                 | Actual Result                                                   | Status   | Defect ID | Severity | Tester        | Date       |
| ------------ | --------------------------------------------------------------- | --------- | --------------------------------------------------------------- | ---------------------------------------------------------------- | -------- | --------- | -------- | ------------- | ---------- |
| TC090        | Verify that the system provides contextual help and tooltips    | Manual    | Users can see contextual help and tooltips where applicable     | Contextual help and tooltips are missing or not displayed       | Fail ❌  | [D044](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/93) | Minor    | Keamogetswe   | 2025-11-18 |
| TC091        | Verify that the system includes a FAQ section                   | Manual    | Users can access the FAQ section and read answers               | FAQ section is missing or inaccessible                           | Fail ❌  | [D045](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/94) | Minor    | Keamogetswe   | 2025-11-18 |
| TC092        | Verify that the system provides contact information for support | Manual    | Users can view support contact information (email, phone, chat) | Support contact information not visible or incomplete           | Fail ❌  | [D046](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/95) | Minor    | Keamogetswe   | 2025-11-18 |



---
# 📊 Non-Functional Testing
---
## **10 📞 Support & Maintenance**
#### Table 10.1: System Monitoring case execusion report
| Test Case ID | Objective                                                     | Test Type | Expected Result                                                                                                      | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC093        | Verify that user actions are logged correctly for debugging   | Manual/automated    | All user actions (login, create, update, delete) are recorded with timestamp, user ID, and action type               |               |        |           | Medium   |        |      |
| TC094        | Verify that system captures and logs errors correctly         | Manual/automated    | All system errors (invalid input, server errors, exceptions) are logged with timestamp, error type, and user context |               |        |           | High     |        |      |                                                  |               |        |           | High     |        |      |

---
## **11. 📱 User Interface Requirements**
===

#### Table 11.1: Responsive Design Test case execusion report
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC095  | Verify responsiveness when resizing the browser window dynamically | Manual| Layout adapts in real-time without breaking or losing functionality |Menu bar expands excessively when resizing window, hiding all other content | Fail ❌ | [D-008](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) | Major | Keamogetswe| 2025-11-14 |
| TC096  | Verify the system displays correctly on desktop screens (1920×1080 and above) | Manual | All UI elements render properly and no horizontal scrolling occurs| All UI elements rendered properly and no horizontal scrolling occurs| Pass ✅ | — | —  | Keamogetswe| 2025-11-14 |
| TC097  | Verify the system displays correctly on tablet screens (768px to 1024px) | Automated | ayout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur  | Pass ✅ |  | — | —  |Keamogetswe| 2025-11-17 |
| TC098  | Verify the system displays correctly on mobile phones (320px to 767px) | Manual | Layout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur | Menu bar expands excessively when resizing window, hiding all other content | Fail ❌  | [D047](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96)| Critical | Keamogetswe| 2025-11-17 |
---

#### Table 11.2: Accessibility (📱 User Interface Requirements ) - (Manual testing )
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC099  | Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | Manual | All text and UI elements meet required contrast ratios | Text readable; no low contrast detected | Pass ✅  | — | — | Sally Trizer  | 2025-11-12 |
| TC100  | Verify zooming to 200% does not break layout | Manual  | Page remains usable and responsive at 200% zoom | When zoomed to 200%, the menu enlarges excessively, pushing or hiding other content. Only the menu is visible at this zoom level | Fail ❌ | [D-010](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59)  | Medium  | Keamogetswe | 2025-11-14 |
| TC110  | Verift that the system support keyboard navigation | Manual | All fields accessible and focusable using Tab and Enter | Tabbing works smoothly and Enter button functions correctly |  Pass ✅ | — | —  | Sally Trizer | 2025-11-12 |
| TC111  | Verify all meaningful images have descriptive alt text | Manual  | Images have descriptive alt text | alt attribute missing for awareness page images | Fail ❌ | [D-011](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59)  | Medium | Sally Trizer | 2025-11-12 |
| TC112  | Verify screen reader announces Form Field Labels correctly | Manual | Screen reader announce each field correctly | NVDA can announce the field correctly | Pass ✅ | — | —  |Keamogetswe| 2025-11-14 |
| TC113  | Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | Lighthouse - Dev Tools | All text and UI elements meet required contrast ratios | Low Contrast Text Fails WCAG 2.1 AA | Fail ❌ | [D-009](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) | Major | Keamogetswe | 2025-11-14 |

---
#### Table 11.3:  Navigation Test Cases execution report
| Test Case ID | Objective                                                   | Test Type       | Expected Result                                                                 | Actual Result                                                                 | Status | Defect ID | Severity | Tester       | Date       |
|--------------|-------------------------------------------------------------|------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------|-----------|----------|--------------|------------|
| TC114| Verify navigation menu is easy to understand                 | Non-Functional   | Navigation menu is clearly visible with descriptive labels                      | Navigation menu displays correctly and is easy to understand                 | Pass ✅   | —         | —        | Keamogetswe | 2025-11-16 |
| TC115  | Verify navigation menu links work correctly                  | Non-Functional   | Each navigation link should redirect to the correct page                         | All navigation redirects function as expected                                | Pass ✅    | —         | —        |Keamogetswe | 2025-11-16 |
| TC116        | Verify system shows correct breadcrumbs on complex pages  | Manual  | Breadcrumbs should display full, accurate page hierarchy       | Breadcrumb shows only **"Profile"** when editing; hierarchy missing | Fail ❌  | [D048](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96)| Minor    | Keamogetswe   | 2025-11-16 |
| TC117        | Verify search bar visibility and relevant results functionality | Manual | Search results and filters should update based on input        | Search & filter **do nothing**; article list remains unchanged      | Fail ❌  | [D048](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96)  | Minor    | Keamogetswe   | 2025-11-16 |

---
## **12. 🔒 Data Management Requirements**
---

#### Table 12.1: Data Validation Test case execusion report
| Test Case ID | Objective                                                          | Test Type | Expected Result                                                                                       | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ------------------------------------------------------------------ | --------- | ----------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC118        | Verify that the system validates all user inputs before processing | Automated | Invalid or incomplete inputs are rejected; appropriate error messages displayed                       |               | Pass ✅    | —         | —        |Keamogetswe | 2025-11-17 |
| TC119        | Verify that the system prevents SQL injection attacks              | Automated | SQL injection attempts are blocked; system remains secure and stable                                  |  Injection attempt rejected, no login | Pass ✅    | —         | —        |Keamogetswe | 2025-11-17 |
| TC120        | Verify that the system prevents XSS attacks                        | Manual| Scripts or malicious content in input fields are sanitized; system does not execute malicious scripts |  system does not execute malicious scripts  |  Pass ✅    | —         | —        |Keamogetswe | 2025-11-18 |
| TC121        | Verify that user-generated content is sanitized before storage     | Automated | All special characters and HTML tags are sanitized; stored content is safe to display                 |               |        |           | High     |        |      |

---
## **13. 🚀 Performance Requirements**
---
#### Table 13.1: Response Time Test case execusion report
| Test Case ID | Objective                                                                           | Test Type | Expected Result                                                                      | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ----------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------ | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC122        | Verify that the system loads pages within 3 seconds on standard internet connection | Automated | All pages load within 3 seconds under normal network conditions                      |               |        |           | High     |        |      |
| TC123        | Verify that the system responds to user interactions within 1 second                | Automated | All user interactions (clicks, form submissions, navigation) respond within 1 second |               |        |           | High     |        |      |


13.2 CROSS BROWSER TESTING
---
| Test Case ID | Objective | Test Type | Expected Result | Actual Result | Status | Defect ID | Severity | Tester | Date |
|--------------|-----------|-----------|-----------------|---------------|--------|-----------|----------|--------|------|
| TC124 | Verify system works on Google Chrome (latest 2 versions) | Non-Functional | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | — | Sally Trizer  | 2025-11-11 |
| TC125 | Verify system works on Mozilla Firefox (latest 2 versions) | Non-Functional | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | Sally Trizer | 2025-11-12  |
| TC16 | Verify system works on Microsoft Edge (latest 2 versions) | Non-Functional | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | — | Sally Trizer | 2025-11-12 |


---
## **14. 📋 Error Handling Requirements**
---
#### Table 14.1: User-Friendly Errors Testing
| Test Case ID | Objective                                           | Test Type | Expected Result                                                                                                 | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | --------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC127      | Verify system handles network errors on Fast 3G     | Automated | Network errors under Fast 3G connection are handled gracefully; user sees a clear message and can retry actions |               |        |           | High     |        |      |
| TC128      | Verify system handles network errors on Slow 3G     | Automated | Network errors under Slow 3G connection are handled gracefully; user sees a clear message and can retry actions |               |        |           | High     |        |      |
| TC129      | Verify system handles Offline / no network scenario | Automated | When offline, system shows a user-friendly offline message and prevents actions that require network            |               |        |           | High     |        |      |
| TC130        | Verify that the system displays clear, actionable error messages     | Automated | All error messages are easy to understand and provide actionable guidance to the user                                 |               |        |           | High     |        |      |
| TC131        | Verify that the system provides guidance for resolving common issues | Automated | For common issues (e.g., invalid input, login failure), the system shows guidance or help tips to resolve the problem |               |        |           | High     |        |      |

---
#### Table 14.2: Form Validation Testing
| Test Case ID | Objective                                                         | Test Type | Expected Result                                                                                                        | Actual Result                                                               | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | ----------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------ | --------- | -------- | ----------- | ---------- |
| TC132        | Verify that the system validates forms in real-time               | Automated | Form fields are validated instantly as the user types or selects options; invalid input triggers immediate feedback    | Form fields validated instantly; invalid input triggered immediate feedback | Pass ✅ | —         | —        | Keamogetswe | 2025-11-14 |
| TC133        | Verify that the system prevents form submission with invalid data | Automated | Form cannot be submitted when required fields are empty or invalid; user is notified of errors                         | Form submission blocked for invalid/empty fields; error messages displayed  | Pass ✅ | —         | —        | Keamogetswe | 2025-11-14 |
| TC134        | Verify that the system highlights validation errors clearly       | Automated | Invalid fields are visually highlighted (e.g., red border, error message) so the user can identify and fix them easily | Invalid fields highlighted with red border and error messages displayed     | Pass ✅ | —         | —        | Keamogetswe | 2025-11-14 |


----
# Boundary Testing and Edge Case Test execution report
----
#### Table 15: Boundary Testing and Edge Case Test execution report
| Test Case ID | Objective                                                              | Test Type | Expected Result                                                        | Actual Result                                         | Status   | Defect ID | Severity  | Tester        | Date       |
| ------------ | ---------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------- | ---------------------------------------------------- | -------- | --------- | --------- | ------------- | ---------- |
| TC136        | Verify date selection rejects today and past dates; allows minimum date (tomorrow) | Automated | Dates today and earlier are rejected with validation message           | Dates today and earlier accepted                     | Fail ❌  | [D050](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96) | Major     | Keamogetswe   | 2025-11-17 |
| TC137        | Verify date selection rejects dates beyond 30 days                     | Automated | Dates >30 days from today are rejected with validation message         | Dates beyond 30 days accepted                        | Fail ❌  | [D051](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/97) | Major     | Keamogetswe   | 2025-11-17 |
| TC138        | Verify name field accepts 2-50 characters                              | Automated | Names with <2 or >50 characters are rejected; valid length is accepted | Names outside 2-50 characters accepted             | Fail ❌  | [D052](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/98) | Major     | Keamogetswe   | 2025-11-17 |
| TC139        | Verify email field accepts valid format                                | Automated | Invalid email formats are rejected; valid emails accepted              | Email validation works correctly                     | Pass ✅  | -         | -         | Keamogetswe   | 2025-11-17 |
| TC140        | Verify password field enforces minimum 8 characters                    | Automated | Passwords <8 characters are rejected                                   | Passwords <8 characters accepted                    | Fail ❌  | [D053](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/99) | Major     | Keamogetswe   | 2025-11-17 |
| TC141        | Verify instructions field accepts 0-200 characters                     | Automated | Instructions exceeding 200 characters are rejected                     | Instructions >200 characters accepted              | Fail ❌  | [D054](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/100) | Minor     | Keamogetswe   | 2025-11-17 |
| TC144        | Verify special characters in name/email/instructions                   | Automated | System accepts valid special characters in inputs without errors       | Works correctly                                     | Pass ✅  | -         | -         | Keamogetswe   | 2025-11-17 |
| TC145        | Verify Unicode and international characters in name/email/instructions | Automated | System accepts Unicode and international characters correctly          | Cannot send email with symbol                       | Fail ❌  | [D055](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/101) | Minor     | Keamogetswe   | 2025-11-17 |
| TC146        | Verify very long inputs are rejected                                   | Automated | Inputs exceeding maximum length are rejected with validation           | Very long inputs accepted                            | Fail ❌  | [D056](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/102) | Major     | Keamogetswe   | 2025-11-17 |
| TC147        | Verify empty or whitespace-only inputs are rejected                    | Automated | Inputs that are empty or whitespace-only are rejected                  | Works correctly                                     | Pass ✅  | -         | -         | Keamogetswe   | 2025-11-17 |
