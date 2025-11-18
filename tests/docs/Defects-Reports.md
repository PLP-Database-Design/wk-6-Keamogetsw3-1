# 🐞 Defect Log – CleanCity Project

## **Functional Test Defects**
| ID    | Issue Title                                                        | Severity | Risk ID | Status | GitHub Link | Test Case ID |
|-------|--------------------------------------------------------------------|----------|---------|--------|-------------|--------------|
| D-001 | Profile shows email instead of full name                           | Cosmetic | R00     | Open   | [Issue #28](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/28) | TC-001 |
| D-002 | Existing user can login with a completely invalid password         | Critical | R001    | Open   | [Issue #31](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31) | TC-002 |
| D-003 | System allows login with unregistered credentials                  | Critical | R001    | Open   | [Issue #32](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32) | TC-003 |
| D-004 | Pick-up request submitted without user registration                | Critical | R001    | Open   | [Issue #33](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33) | TC-020 |
| D-005 | Pickup is scheduled even with past/invalid date                    | Major    | R003    | Open   | [Issue #34](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/34) | TC-025 |
| D-006 | Instructions exceeding 200 characters accepted without validation  | Minor    | R003    | Open   | [Issue #41](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41) | TC-028 |
| D-007 | System allows scheduling multiple pickups for the same date        | Major    | R003    | Open   | [Issue #42](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42) | TC-029 |
| D-012 | User cannot view past and current pickup request history           | Major    | R003    | Open   | [Issue #61](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/61) | TC-030 |
| D-013 | Completed and cancelled pickup requests not shown in dashboard     | Major    | R003    | Open   | [Issue #62](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/62) | TC-031 |
| D-014 | User cannot cancel a pending pickup request                        | Major    | R003    | Open   | [Issue #63](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/63) | TC-032 |
| D-015 | Completed/cancelled requests can potentially be cancelled again    | Major    | R003    | Open   | [Issue #64](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/64) | TC-033 |
| D-016 | User cannot modify pickup details 24 hours before scheduled time   | Major    | R003    | Open   | [Issue #65](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/65) | TC-034 |
| D-017 | System allows modification within 24 hours of scheduled pickup     | Major    | R003    | Open   | [Issue #66](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/66) | TC-035 |
| D-018 | Pickup status not displayed correctly                               | Major    | R003    | Open   | [Issue #67](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/67) | TC-036 |
| D-019 | Pickup status does not update dynamically after completion/cancellation | Major | R003    | Open   | [Issue #68](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/68) | TC-037 |
| D-020 | Pickup request status does not update in real-time                  | Major    | R003    | Open   | [Issue #69](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/69) | TC-038 |
| D-021 | Users do not receive notifications for pickup request status changes | Major  | R003    | Open   | [Issue #70](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/70) | TC-039 |
| D-022 | Feedback not associated with completed pickup                        | Major    | R003    | Open   | [Issue #71](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/71) | TC-040 |
| D-023 | Dashboard does not display personalized information for logged-in users | Major | R003    | Open   | [Issue #72](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/72) | TC-041 |
| D-024 | Environmental impact metrics not displayed on dashboard             | Major    | R003    | Open   | [Issue #73](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/73) | TC-042 |
| D-025 | Badges for achievements display incorrectly on dashboard            | Cosmetic | R003    | Open   | [Issue #74](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/74) | TC-043 |
| D-026 | Admins cannot create a blog post                                     | Major    | R004    | Open   | [Issue #75](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/75) | TC-044 |
| D-027 | Admins cannot edit an existing blog post                              | Major    | R004    | Open   | [Issue #76](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/76) | TC-045 |
| D-028 | Admins cannot delete a blog post                                      | Major    | R004    | Open   | [Issue #77](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/77) | TC-046 |
| D-029 | Profile picture upload fails with server error                        | Cosmetic | R005    | Open   | [Issue #78](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/78) | TC-047 |

---

## **Non-Functional Test Defects**
| ID    | Issue Title                                                               | Severity | Risk ID | Status | GitHub Link |
|--------|---------------------------------------------------------------------------|----------|---------|--------|-------------|
| D-008 | Menu bar expands excessively when resizing window, hiding content          | Major    | R008    | Open   | [Issue #55](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) |
| D-009 | Low-contrast text fails WCAG 2.1 AA                                        | Major    | R008    | Open   | [Issue #56](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/56) |
| D-010 | Layout breaks at 200% zoom (accessibility zoom & reflow failure)           | Medium   | R008    | Open   | [Issue #57](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/57) |
| D-011 | Missing alt text for meaningful images                                     | Medium   | R008    | Open   | D-011 |
