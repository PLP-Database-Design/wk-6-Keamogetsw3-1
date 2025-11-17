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
| TC023      | Verify scheduling a pickup without login  | Manual| System should restrict access and redirect to login page | Pick-up succefully submitted   | Fail ❌ |[D-004](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33)        | Major       | Keamogetswe | 2025-11-12 |
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
| TC031  | Invalid pickup request (Yesterday’s date)            | Manual| System does not allow scheduling for past date   | Confirmation message displayed  | Fail ❌ | [D-005](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/)       |  Medium  |    Keamogetswe      |    2025-11-13       |
| TC032  | Invalid pickup request (empty Waste Type) | Manual | System shows error indicating Waste Type is required |  System showed error indicating Waste Type is required | Pass ✅  | — | — | Keamogetswe  |  2025-11-14  |
| TC033  | Invalid pickup request (empty Location)   | Manual| System shows error indicating Location is required |   System showed error indicating Location is required |  Pass ✅  | — |  —  | Keamogetswe  | 2025-11-14  |
| TC034  | Invalid pickup request (Very long text >200 chars)   | Manual| System truncates input or shows error for long text  | Confirmation message displayed   |  Fail ❌| [D-0061](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41) | Medium |  Keamogetswe  | 2025-11-14  |
| TC035  | The system shall prevent scheduling multiple pickups for the same date | Manual| System prevents creating duplicate pickups for the same date |   Confirmation message displayed   | Fail ❌ | [D-007](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42)| Medium|  Keamogetswe  | 2025-11-14 |
| TC036  | Valid pickup request - Verify system accepts submission and displays confirmation message (“Pickup scheduled successfully”)   | Automated | Pickup request is successfully created | Confirmation message displayed   | Pass ✅   | —  | —  | Keamogetswe| 2025-11-16 |
---

#### Table 2.2: 📋 Request Management
| Test Case ID | Objective                                                                  | Test Type | Expected Result                                                     | Actual Result                                                       | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | -------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------ | --------- | -------- | ----------- | ---------- |
| TC037        | Verify the system displays the user’s pickup request history.              | Manual    | User can view all past and current pickup requests with details.    | User cannot view all past and current pickup requests with details. | Fail ❌ | D00       | Major    | Keamogetswe | 2025-11-13 |
| TC038        | Verify completed and cancelled requests appear in history.                 | Manual    | Completed and cancelled requests are shown correctly.               | Completed and cancelled requests are not shown at all               | Fail ❌ | D00       | Major    | Keamogetswe | 2025-11-13 |
| TC039        | Verify user can cancel a pending pickup request.                           | Manual    | Pending request changes status to “Cancelled.”                      | Rser cannot cancel a pending pickup request. | Fail ❌ | D000    | Critical | Sally Trizer  | 2025-11-12 |
| TC040        | Verify completed or cancelled requests cannot be cancelled again.          | Manual    | System prevents double cancellation.                                | N/A  | Fail ❌ | D000 | Major    | Sally Trizer  | 2025-11-12 |
| TC041        | Verify modification of pickup details at least 24 hours before schedule.   | Manual    | User can update details successfully.                               | N/A       | Fail ❌ | D000 | Major    | Sally Trizer   | 2025-11-12 |
| TC042        | Verify modification not allowed within 24 hours of scheduled time.         | Manual    | System prevents modification and shows warning.                     |N/A                                                            | Fail ❌ | D000       | Medium   | Sally Trizer   | 2025-11-12 |
| TC043        | Verify system displays correct request status for each pickup.             | Manual    | Status correctly shows Pending, Confirmed, Completed, or Cancelled. | Pickup status are not listed or visible                                                             | Fail ❌ | D000      | Major    | Sally Trizer   | 2025-11-12 |
| TC044        | Verify request status updates automatically after completion/cancellation. | Manual    | Status updates dynamically after change.                            |        Pickup status are not listed or visible  | Fail ❌ | D000 | Major    | Sally Trizer   | 2025-11-12 |

---

#### Table 2.3: 📋 Request Tracking

| Test Case ID | Objective                                                                     | Test Type | Expected Result                                                                              | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ----------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC045        | Verify that the system provides real-time status updates for pickup requests. | Manual    | Status of each pickup request updates dynamically without requiring page refresh.            |               |    Fail ❌    | —         | —        |     Sally Trizer   |  2025-11-16 |
| TC046        | Verify that users receive notifications for pickup request status changes.    | Manual    | User receives notifications (email, SMS, or in-app) whenever the status of a pickup changes. |               |    Fail ❌    | —         | —        |     Sally Trizer   | 2025-11-16  |
| TC047        | Verify that users can add feedback after a pickup is completed.               | Manual    | Users can submit feedback, and the system stores it associated with the completed pickup.    |               |   Pass ✅      | —         | —   |  Keamogetswe  | 2025-11-16  |

---
### **3. 📊 Dashboard & Analytics Requirements**
---
#### Table 3.1:
| Test Case ID | Objective                                                                              | Test Type | Expected Result                                                                                                   | Actual Result                                                       | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | -------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------ | --------- | -------- | ----------- | ---------- |
| TC048        | Verify that the user dashboard displays personalized information for logged-in users   | Manual    | Dashboard shows recent pickup requests, upcoming scheduled pickups, achievement badges, and quick action buttons  | Dashboard does not show anything personlised information |Fail ❌ | D-000  | Minor  | Keamogetswe | 2025-11-16  |
| TC049        | Verify that the system shall calculate and display user's environmental impact metrics | Manual    | Dashboard correctly calculates and displays total waste diverted, CO2 emissions saved, and trees equivalent saved |None of the impact metric is shown | Fail ❌| D-000 |   Minor | Keamogetswe | 2025-11-16  |
| TC050        | Verify that the system awards badges for various achievements                          | Manual    | User is awarded badges based on milestones and badges are displayed on the dashboard | badges are displayed on the dashboard  | Fail ❌  | D000 | Minor | Keamogetswe  | 2025-11-16 |

---
### **4. 📝 Content Management Requirements**
---
#### Table 4.1 ✍️ Blog System Test case execusion report
| Test Case ID | Objective                                                       | Test Type  | Expected Result                                                  | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | --------------------------------------------------------------- | ---------- | ---------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC051        | Verify that the blog list page loads successfully | Manual| Blog page loads and displays available blog posts | Blog page loads and displays available blog posts | Pass ✅ | — |  —   |    Keamogetswe    |   2025-11-12   |
| TC052        | Verify that users can view a single blog post | Manual | Blog post content (title, date, body, images) displays correctly | Blog post content (title, date, body, images) displays correctly |Pass ✅ |  — |  — | Keamogetswe |    2025-11-16  |
| TC053        | Verify that users can interact with blog content (like/comment) | Manual | User can click like or submit a comment successfully| User can click like or submit a comment successfully |Pass ✅ | — | — |Keamogetswe |   2025-11-16   |
| TC054        | Verify that admins can create a blog post| Manual | Blog post is saved and appears in the list | Admins cannot create a blog post | Fail ❌ |  D000 | Major | Sally Trizer |   2025-11-12   |
| TC055        | Verify that admins can edit an existing blog post| Manual | Updated content is saved and reflected on the blog page | Admins cannot edit a blog post | Fail ❌ |D000 | Major |Keamogetswe |    2025-11-16  |
| TC056        | Verify that admins can delete a blog post | Manual | Blog post is removed and no longer visible |Admins cannot de;ete a blog post | Fail ❌ | D000 | Major  | Keamogetswe |  2025-11-16     |
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
| TC067        | Verify that users can upload a profile picture                | Manual    | Users can upload a profile picture and it is displayed correctly on their profile | Uploading image returns a 500 server error                                  | Fail ❌ | D003      | Major    | Keamogetswe | 2025-11-16 |


---
#### Table 5.2  🤝 Community Feed Test case execusion report
| Test Case ID | Objective                                            | Test Type | Expected Result                                                                | Actual Result                                                | Status | Defect ID | Severity | Tester      | Date       |
| ------------ | ---------------------------------------------------- | --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------ | ------ | --------- | -------- | ----------- | ---------- |
| TC068        | Verify that users can follow other community members | Manual    | Users can follow/unfollow other community members successfully                 | Unable to follow/unfollow other community members            | Fail ❌ | D001      | Minor    | Keamogetswe | 2025-11-17 |
| TC069        | Verify that news feed displays community activities  | Manual    | News feed shows latest activities (posts, likes, comments) from followed users | News feed did not update or show latest community activities | Fail ❌ | D002      | Minor    | Keamogetswe | 2025-11-17 |

---
### **6. ⚙️ Administrative Functions Requirements**
---

#### Table 6.1 Request Management Test case execusion report
| Test Case ID | Test Description                                           | Test Type          | Expected Result                                                               | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ---------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC070    | Verify that admins can view all pickup requests            | Manual | Admin can view a full list of all pickup requests with complete details       |               |        |           |          |        |      |
| TC071   | Verify that admins can approve, reject, or modify requests | Manual | Admin can successfully approve, reject, or modify any pickup request          |               |        |           |          |        |      |
| TC072   | Verify that admins can assign pickup dates and times       | Manual | Admin can set or update pickup dates/times and changes are saved successfully |               |        |           |          |        |      |
| TC073    | Verify that admins can filter and search pickup requests   | Manual | The system returns correct filtered or searched results based on criteria     |               |        |           |          |        |      |


---
#### Table 6.2 User Management Test case execusion report
| Test Case ID | Test Description                                  | Test Type | Expected Result                                                             | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ------------------------------------------------- | --------- | --------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC074    | Verify that admins can view all registered users  | Manual    | Admin can successfully view a complete list of all registered system users  |               |        |           |          |        |      |
| TC075    | Verify that admins can change user roles          | Manual    | Admin can update user roles and changes are saved and reflected immediately |               |        |           |          |        |      |
| TC076    | Verify that admins can suspend or delete accounts | Manual    | Admin can suspend or delete user accounts and the system updates the status |               |        |           |          |        |      |
| TC077    | Verify that system provides user activity reports | Manual    | Admin can view activity reports including logins, actions, and timestamps   |               |        |           |          |        |      |


---
#### Table 6.3: Content Moderation Test case execusion report
| Test Case ID | Test Description                                             | Test Type | Expected Result                                                                   | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ------------------------------------------------------------ | --------- | --------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC078    | Verify that admins can moderate community posts and comments | Manual    | Admin can view, review, and manage all posts/comments from the moderation panel   |               |        |           |          |        |      |
| TC079   | Verify that admins can delete inappropriate content          | Manual    | Admin can successfully delete posts/comments and they no longer appear publicly   |               |        |           |          |        |      |
| TC080  | Verify that users can flag/ report inappropriate content     | Manual    | Users can flag posts/comments and reports appear in the admin moderation queue    |               |        |           |          |        |      |
| TC081  | Verify that admins can create announcements                  | Manual    | Admin can create announcements and they appear on the community/announcement page |               |        |           |          |        |      |

---
### **7. 🔔 Notification System Requirements**
---
#### Table 7.1: System Notifications Test case execusion report
| Test Case ID | Test Description                                                                                               | Test Type | Expected Result                                                              | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | -------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC082 | Verify that the system displays a notification bell with unread count                                          | Manual    | Notification bell is visible and shows the correct unread notification count |               |        |           |          |        |      |
| TC083  | Verify that the system shows notifications for pickup updates, blogs, community interactions, and achievements | Manual    | All notification types appear correctly in the notification list             |               |        |           |          |        |      |
| TC084 | Verify that users can mark notifications as read                                                               | Manual    | Selected notifications change to “read” state and unread counter updates     |               |        |           |          |        |      |
| TC085 | Verify that the system provides a full notification history                                                    | Manual    | Notification history page displays past notifications in chronological order |               |        |           |          |        |      |
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
| Test Case ID | Objective                                                       | Test Type | Expected Result                                                 | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | --------------------------------------------------------------- | --------- | --------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC090        | Verify that the system provides contextual help and tooltips    | Manual    | Users can see contextual help and tooltips where applicable     |               |        |           |          |        |      |
| TC091        | Verify that the system includes a FAQ section                   | Manual    | Users can access the FAQ section and read answers               |               |        |           |          |        |      |
| TC092        | Verify that the system provides contact information for support | Manual    | Users can view support contact information (email, phone, chat) |  


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
| TC097  | Verify the system displays correctly on tablet screens (768px to 1024px) | Manual | ayout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur  | |  | — | —  | |  |
| TC098  | Verify the system displays correctly on mobile phones (320px to 767px) | Manual | Layout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur | |  | — | —  | |  |
---

#### Table 11.2: Accessibility (📱 User Interface Requirements ) - (Manual testing )
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC099  | Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | Manual | All text and UI elements meet required contrast ratios | Text readable; no low contrast detected | Pass ✅  | — | — | Sally Trizer  | 2025-11-12 |
| TC100  | Verify zooming to 200% does not break layout | Manual  | Page remains usable and responsive at 200% zoom | When zoomed to 200%, the menu enlarges excessively, pushing or hiding other content. Only the menu is visible at this zoom level | Fail ❌ | [D-010](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59)  | Medium  | Keamogetswe | 2025-11-14 |
| TC110  | Verift that the system support keyboard navigation | Manual | All fields accessible and focusable using Tab and Enter | Tabbing works smoothly and Enter button functions correctly |  Pass ✅ | — | —  | Sally Trizer | 2025-11-12 |
| TC111  | Verify all meaningful images have descriptive alt text | Manual  | Images have descriptive alt text | alt attribute missing for awareness page images | Fail ❌ | [D-011](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59)  | Medium | Sally Trizer | 2025-11-12 |
| TC112  | Verify screen reader announces Form Field Labels correctly | Manual | Screen reader announce each field correctly | |  | — | —  |  Sally Trizer |  |
| TC113  | Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | Lighthouse - Dev Tools | All text and UI elements meet required contrast ratios | Low Contrast Text Fails WCAG 2.1 AA | Fail ❌ | [D-009](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) | Major | Keamogetswe | 2025-11-14 |

---
#### Table 11.3:  Navigation Test Cases execution report
| Test Case ID | Objective                                                   | Test Type       | Expected Result                                                                 | Actual Result                                                                 | Status | Defect ID | Severity | Tester       | Date       |
|--------------|-------------------------------------------------------------|------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------|-----------|----------|--------------|------------|
| TC114| Verify navigation menu is easy to understand                 | Non-Functional   | Navigation menu is clearly visible with descriptive labels                      | Navigation menu displays correctly and is easy to understand                 | Pass ✅   | —         | —        | Keamogetswe | 2025-11-16 |
| TC115  | Verify navigation menu links work correctly                  | Non-Functional   | Each navigation link should redirect to the correct page                         | All navigation redirects function as expected                                | Pass ✅    | —         | —        |Keamogetswe | 2025-11-16 |
| TC116 | Verify system shows correct breadcrumbs on complex pages     | Non-Functional   | Breadcrumbs should display full, accurate page hierarchy                         | Breadcrumb shows only **"Profile"** when editing; hierarchy missing          | Fail ❌   | | Minor   | Keamogetswe | 2025-11-16 |
| TC117   | Verify search bar visibility and relevant results functionality | Non-Functional | Search results and filters should update based on input                          | Search & filter **do nothing**; article list remains unchanged               | Fail ❌  | | Medium    | Keamogetswe | 2025-11-16 |

---
## **12. 🔒 Data Management Requirements**
---

#### Table 12.1: Data Validation Test case execusion report
| Test Case ID | Objective                                                          | Test Type | Expected Result                                                                                       | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ------------------------------------------------------------------ | --------- | ----------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC118        | Verify that the system validates all user inputs before processing | Automated | Invalid or incomplete inputs are rejected; appropriate error messages displayed                       |               |        |           | High     |        |      |
| TC119        | Verify that the system prevents SQL injection attacks              | Automated | SQL injection attempts are blocked; system remains secure and stable                                  |               |        |           | Critical |        |      |
| TC120        | Verify that the system prevents XSS attacks                        | Automated | Scripts or malicious content in input fields are sanitized; system does not execute malicious scripts |               |        |           | Critical |        |      |
| TC121        | Verify that user-generated content is sanitized before storage     | Automated | All special characters and HTML tags are sanitized; stored content is safe to display                 |               |        |           | High     |        |      |

---
## **13. 🚀 Performance Requirements**
---
#### Table 13.1: Response Time Test case execusion report
| Test Case ID | Objective                                                                           | Test Type | Expected Result                                                                      | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ----------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------ | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC122        | Verify that the system loads pages within 3 seconds on standard internet connection | Automated | All pages load within 3 seconds under normal network conditions                      |               |        |           | High     |        |      |
| TC123        | Verify that the system responds to user interactions within 1 second                | Automated | All user interactions (clicks, form submissions, navigation) respond within 1 second |               |        |           | High     |        |      |

---
#### Table 13.2: 🌐 Cross-Browser Compatibility Testing

| Test Case ID | Objective | Test Type | Expected Result | Actual Result | Status | Defect ID | Severity | Tester | Date |
|--------------|-----------|-----------|-----------------|---------------|--------|-----------|----------|--------|------|
| TC124 | Verify system works on Google Chrome (latest 2 versions) | Manual | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | — | Sally Trizer  | 2025-11-11 |
| TC125 | Verify system works on Mozilla Firefox (latest 2 versions) | Manual | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | Sally Trizer | 2025-11-12  |
| TC126 | Verify system works on Microsoft Edge (latest 2 versions) | Manual | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | — | Sally Trizer | 2025-11-12 |

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
| Test Case ID | Objective                                                         | Test Type | Expected Result                                                                                                        | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ----------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC132        | Verify that the system validates forms in real-time               | Automated | Form fields are validated instantly as the user types or selects options; invalid input triggers immediate feedback    |               |        |           | High     |        |      |
| TC133        | Verify that the system prevents form submission with invalid data | Automated | Form cannot be submitted when required fields are empty or invalid; user is notified of errors                         |               |        |           | High     |        |      |
| TC134        | Verify that the system highlights validation errors clearly       | Automated | Invalid fields are visually highlighted (e.g., red border, error message) so the user can identify and fix them easily |               |        |           | Medium   |        |      |

----
# Boundary Testing and Edge Case Test execution report
----
#### Table 15: Boundary Testing and Edge Case Test execution report
| Test Case ID | Objective                                                              | Test Type | Expected Result                                                        | Actual Result | Status | Defect ID | Severity | Tester | Date |
| ------------ | ---------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------- | ------------- | ------ | --------- | -------- | ------ | ---- |
| TC135        | Verify date selection allows minimum date (tomorrow)                   | Automated | Dates before tomorrow are rejected; tomorrow and later are allowed     |               |        |           | High     |        |      |
| TC136        | Verify date selection rejects today and past dates                     | Automated | Dates today and earlier are rejected with validation message           |               |        |           | High     |        |      |
| TC137        | Verify date selection rejects dates beyond 30 days                     | Automated | Dates >30 days from today are rejected with validation message         |               |        |           | High     |        |      |
| TC138        | Verify name field accepts 2-50 characters                              | Automated | Names with <2 or >50 characters are rejected; valid length is accepted |               |        |           | Medium   |        |      |
| TC139        | Verify email field accepts valid format                                | Automated | Invalid email formats are rejected; valid emails accepted              |               |        |           | High     |        |      |
| TC140        | Verify password field enforces minimum 8 characters                    | Automated | Passwords <8 characters are rejected                                   |               |        |           | High     |        |      |
| TC141        | Verify instructions field accepts 0-200 characters                     | Automated | Instructions exceeding 200 characters are rejected                     |               |        |           | Medium   |        |      |
| TC144        | Verify special characters in name/email/instructions                   | Automated | System accepts valid special characters in inputs without errors       |               |        |           | Medium   |        |      |
| TC145        | Verify Unicode and international characters in name/email/instructions | Automated | System accepts Unicode and international characters correctly          |               |        |           | Medium   |        |      |
| TC146        | Verify very long inputs are rejected                                   | Automated | Inputs exceeding maximum length are rejected with validation           |               |        |           | High     |        |      |
| TC147        | Verify empty or whitespace-only inputs are rejected                    | Automated | Inputs that are empty or whitespace-only are rejected                  |               |        |           | High     |        |      |
