# Test Case Execution Report
---
This section provides a detailed summary of the test cases executed during Phase 3 (test execution) of this project.  
The purpose of this report is to validate that the application meets its functional requirements.

## ** Functional Testing **
### Table 1: Manually Executed Test Cases, their results and key observations

#### Table 1.1: Registration Test Cases
| Test Case ID | Test Description                           | Test Type  | Expected Result                        | Actual Result                  | Status | Defect ID | Severity | Tester        | Date       |
| ------------ | ------------------------------------------ | ---------- | -------------------------------------- | ------------------------------ | ------ | --------- | -------- | ------------- | ---------- |
| TC001        | Verify registration with valid credentials | Functional | User should be registered successfully | User successfully registered   | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC002        | Verify registration with invalid email     | Functional | System should ask for valid email      | System asked for correct email | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC003        | Verify registration with empty name field  | Functional | System should ask for Name             | System asked for full name     | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC004        | Verify registration with empty email       | Functional | System should ask for Email            | System asked for Email         | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC005        | Verify registration with empty password    | Functional | System should ask for Password         | System asked for Password      | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |

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
| TC028  | Invalid pickup request (Very long text >200 chars)   | Functional | System truncates input or shows error for long text  | Confirmation message displayed   |  Fail ❌| — | — |  Keamogetswe  | 2025-11-14  |
| TC029  | The system shall prevent scheduling multiple pickups for the same date | Functional | System prevents creating duplicate pickups for the same date |   Confirmation message displayed   | Fail ❌ | — | — |  Keamogetswe  | 2025-11-14   |

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

## ** Functional Testing **
### Table 2: Boundary and Edge Case Test Cases, their results and key observations

## ** Functional Testing **
### Table 3: Automatically Executed Test Cases, their results and key observations

## **Non-Functional Testing**
### Table 4: Executed Test Cases, their results and key observations
