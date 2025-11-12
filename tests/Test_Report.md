# CleanCity: Waste Pickup Scheduler - Test Report
![Alt text](cleancity.png)

**Course:** Software Testing & Quality Assurance  
**Project Type:** Group Assessment
**Team Name:** KNS  
**Submission Date:** 2025-11-18

## Executive Summary
## Test Strategy and Approach
Manual and automated test cases were executed

## Manual Test Cases Summary

| Category | Range of Test Case IDs | Count |
|-----------|------------------------|--------|
| Functional | TC001 – TC010 | 10 |
| Non-Functional | TC011 – TC016 | 6 |
| UI (Accessibility + Cross-Browser) | TC017 – TC024 | 8 |
| Boundary & Edge Cases | TC025 – TC034 | 10 |
| **Total** |  | **34** |

---

## Automated Test Cases Summary

| Category | Range of Test Case IDs | Count |
|-----------|------------------------|--------|
| Functional | TC035 – TC044 | 10 |
| Non-Functional | TC045 – TC050 | 6 |
| UI (Accessibility + Cross-Browser) | TC051 – TC058 | 8 |
| Boundary & Edge Cases | TC059 – TC067 | 9 |
| ** Total** |  | **33** |

---

## Overall Test Summary

| Category | Manual | Automated | Total |
|-----------|---------|------------|--------|
| Functional | 10 | 10 | **20** |
| Non-Functional | 6 | 6 | **12** |
| UI (Accessibility + Cross-Browser) | 8 | 8 | **16** |
| Boundary & Edge Cases | 10 | 9 | **19** |
| ** Grand Total** | **34** | **33** | **67** |

---
## Test Case Execution Report
---
This section provides a detailed summary of the test cases executed during the Phase 3 (test execution) of this project.  
The purpose of this report is to validate that the application meets its functional requirements

### Table 4: Executed test cases, their results and key observations.

#### Table 4.1: Registration Test Cases
| Test Case ID | Test Description                           | Test Type  | Expected Result                        | Actual Result                  | Status | Defect ID | Severity | Tester        | Date       |
| ------------ | ------------------------------------------ | ---------- | -------------------------------------- | ------------------------------ | ------ | --------- | -------- | ------------- | ---------- |
| TC001        | Verify registration with valid credentials | Functional | User should be registered successfully | User successfully registered   | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC002        | Verify registration with invalid email     | Functional | System should ask for valid email      | System asked for correct email | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC003        | Verify registration with empty name field  | Functional | System should ask for Name             | System asked for full name     | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC004        | Verify registration with empty email       | Functional | System should ask for Email            | System asked for Email         | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |
| TC005        | Verify registration with empty password    | Functional | System should ask for Password         | System asked for Password      | Pass ✅ | —         | —        | Keamogetswe | 2025-11-10 |

#### Table 4.2: Login Test Cases

| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC-006      | Verify login with valid credentials       | Functional | User should be logged in successfully | User successfully logged in  | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC-007      | Verify login with invalid password        | Functional | System should display error  | User succefully logged in | Fail ❌ | [D-002](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31)       | Critical     | Keamogetswe | 2025-11-11 |
| TC-008      | Verify login without email       | Functional | System should display email required error | Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC-009      | Verify login without password    | Functional | System should display password required error| Error displayed: "Fill this field" | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-10 |
| TC-0010      | Verify login with non-existent user       | Functional | System should display error           | User logged in succefully   | Fail ❌ |[D-003](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32)        | Critical       | Keamogetswe | 2025-11-12 |

#### Table 4.3: Logout Test Cases

| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC-011      | Verify logout       | Functional | User should be logged out successfully | User successfully logged out  | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC-012      | Verify user cannot access dashboard after logout  | Functional | Attempting to access dashboard redirects to login page  | User redirected to login page | Pass ✅ | — | —  | Keamogetswe | 2025-11-12 |
| TC-013      | Verify scheduling a pickup without login  | Functional | System should restrict access and redirect to login page | Pick-up succefully submitted   | Fail ❌ |[D-004](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33)        | Major       | Keamogetswe | 2025-11-12 |

---
#### Table 4.4: User Session Management (localStorage) Test Cases
| Test Case ID | Test Description                          | Test Type   | Expected Result                       | Actual Result                | Status  | Defect ID | Severity | Tester          | Date       |
|--------------|-------------------------------------------|------------|---------------------------------------|------------------------------|---------|-----------|---------|----------------|-----------|
| TC-014      | Verify session data is stored in localStorage after login    | Functional | localStorage contains session key | localStorage contains a key  `User` | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC-015 | Verify user session persists after page refresh | Functional | User remains logged in; localStorage values persist  |User remains logged in; localStorage values persist | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC-016 | Verify that session persists after reopening browser tab | Functional | User remains logged in; localStorage still holds session data  |User remains logged in; localStorage values persist | Pass ✅  | —         | —       | Keamogetswe  | 2025-11-12 |
| TC-017 | Verify that session data is cleared after logout | Functional | localStorage entry `User` is removed| localStorage entry `User` is removed|Pass ✅ |  — | — | Keamogetswe | 2025-11-12 |


# 🧪 Test Case Table

| Test Case ID | Test Description                            | Test Type   | Expected Result                                | Actual Result                                  | Status  | Defect ID | Severity | Tester        | Date       | 
|---------------|---------------------------------------------|--------------|------------------------------------------------|------------------------------------------------|----------|------------|-----------|----------------|------------|
| TC001         | Verify registration with valid credentials  | Functional   | User should be registered successfully          | User successfully registered                   | Passed   | —          | —         | Keamogetswe | 2025-11-10 |
| TC002         | Verify registration with invalid email      | Functional   | System should ask for valid email             | System asking for correct email | Passed   | —          | —         | Keamogetswe| 2025-11-10 |
| TC003         | Verify registration with empty namefield     | Functional   | System should ask for Name             | System asked for Full name | Passed   | —          | —         | Keamogetswe| 2025-11-10 |
| TC003         | Verify login with valid password            | Functional   | User should be logged in successfully           | User successfully logged in                    | Passed   | —          | —         | Keamogetswe M | 2025-11-10 |
| TC004         | Verify registration with valid credentials  | Functional   | User should be registered successfully          | User successfully registered                   | Passed   | —          | —         | Keamogetswe M | 2025-11-10 |
| TC005         | Verify login with valid password            | Functional   | User should be logged in successfully           | User successfully logged in                    | Passed   | —          | —         | Keamogetswe M | 2025-11-10 |



## Test Case Execution Report 

| Test Case ID | Test Description | Test Type | Status | Defect ID | Severity | Tester | Date | Remarks |
|---------------|----------------|------------------|------------|----------|------------|-----------|---------|--------|
| TC001 | Verify registration with valid credentials | Functional | Passed | — | — | Keamogetswe M | 2025-11-10 | Succefully registered |
| TC003 |  Verify login with valid password | Functional | Passed | — | — | Keamogetswe M | 2025-11-10 | Successfully logged in |
