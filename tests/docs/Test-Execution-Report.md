# Test Case Execution Report
This section provides a detailed summary of the test cases executed during Phase 3 (test execution) of this project.  
The purpose of this report is to validate that the application meets its functional requirements.

---
## **Functional Testing**

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








#### Table 1.2: Login Test Cases
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC006      | Verify login with valid credentials       | Functional | User should be logged in successfully | User successfully logged in  | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC007      | Verify login with invalid password        | Functional | System should display error  | User succefully logged in | Fail ❌ | [D-002](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31)       | Critical     | Keamogetswe | 2025-11-11 |
| TC008      | Verify login without email       | Functional | System should display email required error | Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC009      | Verify login without password    | Functional | System should display password required error| Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC010      | Verify login with non-existent user       | Functional | System should display error           | User logged in succefully   | Fail ❌ |[D-003](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32)        | Critical       | Keamogetswe | 2025-11-12 |

#### Table 1.3: Logout Test Cases
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC011      | Verify logout       | Functional | User should be logged out successfully | User successfully logged out  | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC012      | Verify user cannot access dashboard after logout  | Functional | Attempting to access dashboard redirects to login page  | User redirected to login page | Pass ✅ | — | —  | Keamogetswe | 2025-11-12 |
| TC013      | Verify scheduling a pickup without login  | Functional | System should restrict access and redirect to login page | Pick-up succefully submitted   | Fail ❌ |[D-004](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33)        | Major       | Keamogetswe | 2025-11-12 |

#### Table 1.4: User Session Management (localStorage) Test Cases
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC014      | Verify session data is stored in localStorage after login    | Functional | localStorage contains session key | localStorage contains a key  `User` | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC015 | Verify user session persists after page refresh | Functional | User remains logged in; localStorage values persist  |User remains logged in; localStorage values persist | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC016 | Verify that session persists after reopening browser tab | Functional | User remains logged in; localStorage still holds session data  |User remains logged in; localStorage values persist | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC017 | Verify that session data is cleared after logout | Functional | localStorage entry `User` is removed| localStorage entry `User` is removed|Pass ✅ |  — | — | Keamogetswe | 2025-11-12 |
| TC018  | Verify access restriction after localStorage is cleared manually | Functional | User logged out and redirected to home page| User logged out and redirected to sign in page             |   Pass ✅          | — | — | Keamogetswe | 2025-11-12 |

#### Table 1.5: Role-Based Access Test Cases
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC019 | Verify system creates a new user account with “User” role upon successful registration | Functional | System automatically assigns the “User” role to newly registered accounts |  System assigned the “User” role to newly registered accounts| Pass ✅  | — | — | Keamogetswe  | 2025-11-12 |
| TC020 | Verify system supports two user roles: “User” and “Admin”. each user can have only one valid role assigned| Functional | System supports two user roles: “User” and “Admin” |  System supports two user roles: “User” and “Admin” and correctly assign role| Pass ✅  | — | — | Keamogetswe  | 2025-11-12 |
| TC021 | Verify only Admins can access Admin Dashboard | Functional | “User” role doesnt show Admin dashboard. “Admin” role can access successfully | “User” role doesnt show Admin dashboard. “Admin” role can access successfully | Pass ✅  | — | — | Keamogetswe. Sally Trizer | 2025-11-12 |
| TC022 |Verify direct URL access to Admin Dashboard is blocked for non-admin users | Functional | System restricts access and redirects to “Access Denied” or “Login” page | System restricts access and shows "This page isn’t working" | Pass ✅  | — | — | Keamogetswe | 2025-11-12 |

#### Table 1.6: Pickup Scheduling Test Cases
| Test Case ID | Test Description                                      | Test Type  | Expected Result                                         | Actual Result | Status | Defect ID | Severity | Tester | Date       |
|--------------|------------------------------------------------------|-----------|--------------------------------------------------------|---------------|--------|-----------|---------|--------|-----------|
| TC023  | Valid pickup request - Verify system accepts submission and displays confirmation message (“Pickup scheduled successfully”)   | Functional | Pickup request is successfully created | Confirmation message displayed   | Pass ✅   | —  | —  | Sally Trizer  | 2025-11-12 |
| TC024  | Invalid pickup request (no data)                     | Functional | System shows validation errors for empty fields    | System shows validation errors for empty fields  | Pass ✅ |  —  |  —  |   Keamogetswe   | 2025-11-13 |
| TC025  | Invalid pickup request (Yesterday’s date)            | Functional | System does not allow scheduling for past date   | Confirmation message displayed  | Fail ❌ | [D-005](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/)       |  Medium  |    Keamogetswe      |    2025-11-13       |
| TC026  | Invalid pickup request (empty Waste Type) | Functional | System shows error indicating Waste Type is required |  System showed error indicating Waste Type is required | Pass ✅  | — | — | Keamogetswe  |  2025-11-14  |
| TC027  | Invalid pickup request (empty Location)   | Functional | System shows error indicating Location is required |   System showed error indicating Location is required |  Pass ✅  | — |  —  | Keamogetswe  | 2025-11-14  |
| TC028  | Invalid pickup request (Very long text >200 chars)   | Functional | System truncates input or shows error for long text  | Confirmation message displayed   |  Fail ❌| [D-0061](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41) | Medium |  Keamogetswe  | 2025-11-14  |
| TC029  | The system shall prevent scheduling multiple pickups for the same date | Functional | System prevents creating duplicate pickups for the same date |   Confirmation message displayed   | Fail ❌ | [D-007](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42)| Medium|  Keamogetswe  | 2025-11-14   |

#### Table 1.7: Request Management Test Cases
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC030  | Verify the system displays the user’s pickup request history.              | Functional    | User can view all past and current pickup requests with details.    | |    | —             | —            | |  |
| TC031   | Verify completed and cancelled requests appear in history.                 | Functional    | Completed and cancelled requests are shown correctly.               ||  |  | | | 2025-11-13 |
| TC032   | Verify user can cancel a pending pickup request.                           | Functional    | Pending request changes status to “Cancelled.”                      |   |  | —             | —            | | 2025-11-13 |
| TC033  | Verify completed or cancelled requests cannot be cancelled again.          | Functional    | System prevents double cancellation.                                | |     | —             | —            | | 2025-11-13 |
| TC034   | Verify modification of pickup details at least 24 hours before schedule.   | Functional    | User can update details successfully.                               |  |       | —             | —            | | 2025-11-13 |
| TC035 | Verify modification not allowed within 24 hours of scheduled time.         | Functional    | System prevents modification and shows warning.                     |    |   |  | | | 2025-11-13 |
| TC036   | Verify system displays correct request status for each pickup.             | Functional    | Status correctly shows Pending, Confirmed, Completed, or Cancelled. | |        | —             | —            | Keamogetswe | 2025-11-13 |
| TC037 | Verify request status updates automatically after completion/cancellation. | Functional    | Status updates dynamically after change.                            |  | |   |          |  | 2025-11-13 |
---

---

# 📞 Support & Maintenance

*(Add your support test cases here if needed — structure provided)*

| TC No. | Feature     | Objective          | Expected Result           | Actual Result | Status | Risk Link |
|--------|-------------|--------------------|---------------------------|---------------|--------|-----------|
| TBD    | Support     | Example objective  | Example expectation       | TBD           | TBD    | TBD       |

## **📊 Non-Functional Testing**
### Table 4: Executed Test Cases, their results and key observations
---
#### Table 4.1: Responsive Design (📱 User Interface Requirements )
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC0  | Verify responsiveness when resizing the browser window dynamically | Non-Functional | Layout adapts in real-time without breaking or losing functionality |Menu bar expands excessively when resizing window, hiding all other content | Fail ❌ | [D-008](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) | Major | Keamogetswe| 2025-11-14 |
| TC0  | Verify the system displays correctly on desktop screens (1920×1080 and above) | Non-Functional | All UI elements render properly and no horizontal scrolling occurs| All UI elements rendered properly and no horizontal scrolling occurs| Pass ✅ | — | —  | Keamogetswe| 2025-11-14 |
| TC0  | Verify the system displays correctly on tablet screens (768px to 1024px) | Non-Functional | ayout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur  | |  | — | —  | |  |
| TC0  | Verify the system displays correctly on mobile phones (320px to 767px) | Non-Functional | Layout adjusts appropriately, Content fits the screen, navigation is usable and no overlapping elements occur | |  | — | —  | |  |


#### Table 4.2: Accessibility (📱 User Interface Requirements ) - (Manual testing )
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC0  | Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | Non-Functional (Manually) | All text and UI elements meet required contrast ratios | Text readable; no low contrast detected | Pass ✅  | — | — | Sally Trizer  | 2025-11-12 |
| TC0  | Verify zooming to 200% does not break layout | Non-Functional | Page remains usable and responsive at 200% zoom | When zoomed to 200%, the menu enlarges excessively, pushing or hiding other content. Only the menu is visible at this zoom level | Fail ❌ | [D-010](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59)  | Medium  | Keamogetswe | 2025-11-14 |
| TC0  | Verift that the system support keyboard navigation | Non-Functional | All fields accessible and focusable using Tab and Enter | Tabbing works smoothly and Enter button functions correctly |  Pass ✅ | — | —  | Sally Trizer | 2025-11-12 |
| TC0  | Verify all meaningful images have descriptive alt text | Non-Functional | Images have descriptive alt text | alt attribute missing for awareness page images | Fail ❌ | [D-011](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59)  | Medium | Sally Trizer | 2025-11-12 |
| TC0  | Verify screen reader announces Form Field Labels correctly | Non-Functional | Screen reader announce each field correctly | |  | — | —  |  Sally Trizer |  |

#### Table 4.2: Accessibility (📱 User Interface Requirements ) - (Lighthouse - Dev Tools )
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC0  | Verify contrast ratio meets WCAG 2.1 AA (minimum 4.5:1 for text) | Non-Functional | All text and UI elements meet required contrast ratios | Low Contrast Text Fails WCAG 2.1 AA | Fail ❌ | [D-009](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) | Major | Keamogetswe | 2025-11-14 |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |

#### Table 4.2: Accessibility (📱 User Interface Requirements ) - (SonarQube )
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC0  | Verify that form fields include labels or ARIA-labels | Non-Functional |  | |  | — | —  | |  |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |

----

#### Table 4. Response Time Test cases for Navigation
#### Table 4. Response Time Test Cases for Navigation

| Test Case ID | Objective                                                   | Test Type       | Expected Result                                                                 | Actual Result                                                                 | Status | Defect ID | Severity | Tester       | Date       |
|--------------|-------------------------------------------------------------|------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------|-----------|----------|--------------|------------|
| TC-| Verify navigation menu is easy to understand                 | Non-Functional   | Navigation menu is clearly visible with descriptive labels                      | Navigation menu displays correctly and is easy to understand                 | Pass ✅   | —         | —        | Keamogetswe | 2025-11-16 |
| TC-  | Verify navigation menu links work correctly                  | Non-Functional   | Each navigation link should redirect to the correct page                         | All navigation redirects function as expected                                | Pass ✅    | —         | —        |Keamogetswe | 2025-11-16 |
| TC- | Verify system shows correct breadcrumbs on complex pages     | Non-Functional   | Breadcrumbs should display full, accurate page hierarchy                         | Breadcrumb shows only **"Profile"** when editing; hierarchy missing          | Fail ❌   | | Minor   | Keamogetswe | 2025-11-16 |
| TC-   | Verify search bar visibility and relevant results functionality | Non-Functional | Search results and filters should update based on input                          | Search & filter **do nothing**; article list remains unchanged               | Fail ❌  | | Medium    | Keamogetswe | 2025-11-16 |





| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |


#### Table 4. Response Time (🚀 Performance Requirements)
| Test Case ID | Objective                                                   | Test Type | Expected Result                                               | Actual Result                                       | Status     | Defect ID | Severity | Tester | Date |
| ---------------- | -------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | --------------- | ------------- | ------------ | ----------- | ---------- |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |

| TC0  |  | Non-Functional |  | |  | — | —  | |  |
| TC0  |  | Non-Functional |  | |  | — | —  | |  |




# 🌐 Cross-Browser Compatibility Testing

# Browser Compatibility Test Report

| Test Case ID | Objective | Test Type | Expected Result | Actual Result | Status | Defect ID | Severity | Tester | Date |
|--------------|-----------|-----------|-----------------|---------------|--------|-----------|----------|--------|------|
| TC- | Verify system works on Google Chrome (latest 2 versions) | Non-Functional | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | — | Sally Trizer  | 2025-11-11 |
| TC- | Verify system works on Mozilla Firefox (latest 2 versions) | Non-Functional | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | Sally Trizer | 2025-11-12  |
| TC- | Verify system works on Microsoft Edge (latest 2 versions) | Non-Functional | Application functions correctly without layout issues, errors, or crashes | Application works as expected | Pass ✅ | — | — | Sally Trizer | 2025-11-12 |



