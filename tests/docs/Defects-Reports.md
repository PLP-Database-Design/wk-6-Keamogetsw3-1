# 🐞 Defect Log – CleanCity Project

## **Functional Test Defects**

| ID    | Requirement | Issue Title                                                        | Severity        | Risk ID | Status | GitHub Link | Test Case ID |
|-------|-------------|--------------------------------------------------------------------|------------------|---------|--------|-------------|--------------|
| D001 |             | Profile shows email instead of full name                           | 🟢 Cosmetic      | R013     | Open   | [Issue #28](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/28) | |
| D002 |   🔐 Authentication System    | Existing user can login with a completely invalid password         | 🔴 Critical      | R001    | Open   | [Issue #31](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31) | TC012 / TC018  |
| D003 |             | System allows login with unregistered credentials                  | 🔴 Critical      | R001    | Open   | [Issue #32](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32) | TC015 / TC020 |
| D004 |             | Pick-up request submitted without user registration                | 🔴 Critical      | R002    | Open   | [Issue #33](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33) | TC023 |
| D-005 |             | Pickup is scheduled even with past/invalid date                    | 🟠 Major         | R003    | Open   | [Issue #34](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/34) | TC-025 |
| D-006 |             | Instructions exceeding 200 characters accepted without validation  | 🟡 Minor         | R003    | Open   | [Issue #41](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41) | TC-028 |
| D-007 |             | System allows scheduling multiple pickups for the same date        | 🟠 Major         | R003    | Open   | [Issue #42](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42) | TC-029 |
| D-012 |             | User cannot view past and current pickup request history           | 🟠 Major         | R003    | Open   | [Issue #61](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/61) | TC-030 |
| D-013 |             | Completed and cancelled pickup requests not shown in dashboard     | 🟠 Major         | R003    | Open   | [Issue #62](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/62) | TC-031 |
| D-014 |             | User cannot cancel a pending pickup request                        | 🟠 Major         | R003    | Open   | [Issue #63](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/63) | TC-032 |
| D-015 |             | Completed/cancelled requests can potentially be cancelled again    | 🟠 Major         | R003    | Open   | [Issue #64](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/64) | TC-033 |
| D-016 |             | User cannot modify pickup details 24 hours before scheduled time   | 🟠 Major         | R003    | Open   | [Issue #65](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/65) | TC-034 |
| D-017 |             | System allows modification within 24 hours of scheduled pickup     | 🟠 Major         | R003    | Open   | [Issue #66](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/66) | TC-035 |
| D-018 |             | Pickup status not displayed correctly                              | 🟠 Major         | R003    | Open   | [Issue #67](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/67) | TC-036 |
| D-019 |             | Pickup status does not update dynamically after completion/cancellation | 🟠 Major     | R003 | Open | [Issue #68](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/68) | TC-037 |
| D-020 |             | Pickup request status does not update in real-time                 | 🟠 Major         | R003    | Open   | [Issue #69](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/69) | TC-038 |
| D-021 |             | Users do not receive notifications for pickup request status changes | 🟠 Major     | R003 | Open | [Issue #70](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/70) | TC-039 |
| D-022 |             | Feedback not associated with completed pickup                      | 🟠 Major         | R003    | Open   | [Issue #71](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/71) | TC-040 |
| D-023 |             | Dashboard does not display personalized information for logged-in users | 🟠 Major   | R003 | Open | [Issue #72](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/72) | TC-041 |
| D-024 |             | Environmental impact metrics not displayed on dashboard            | 🟠 Major         | R003    | Open   | [Issue #73](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/73) | TC-042 |
| D-025 |             | Badges for achievements display incorrectly on dashboard           | 🟢 Cosmetic      | R003    | Open   | [Issue #74](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/74) | TC-043 |
| D-026 |             | Admins cannot create a blog post                                   | 🟠 Major         | R004    | Open   | [Issue #75](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/75) | TC-044 |
| D-027 |             | Admins cannot edit an existing blog post                           | 🟠 Major         | R004    | Open   | [Issue #76](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/76) | TC-045 |
| D-028 |             | Admins cannot delete a blog post                                   | 🟠 Major         | R004    | Open   | [Issue #77](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/77) | TC-046 |
| D-029 |             | Profile picture upload fails with server error                     | 🟢 Cosmetic      | R005    | Open   | [Issue #78](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/78) | TC-047 |
| D030  |             | Users cannot follow or unfollow other community members            | 🟡 Minor         |         | Open   | [D030](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/79) | |
| D031  |             | News feed does not display latest community activities             | 🟡 Minor         |         | Open   | [D031](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/80) | |
| D032  |             | Admins cannot approve, reject, or modify pickup requests           | 🟠 Major         |         | Open   | [D032](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/81) | |
| D033  |             | Admins cannot assign or update pickup dates and times              | 🟠 Major         |         | Open   | [D033](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/82) | |
| D034  |             | Admins cannot filter or search pickup requests correctly           | 🟡 Minor         |         | Open   | [D034](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/83) | |
| D035  |             | Admins cannot receive or reply to feedback                         | 🟠 Major         |         | Open   | [D035](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/84) | |
| D036  |             | Admins cannot view all registered users                             | 🟠 Major         |         | Open   | [D036](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/85) | |
| D037  |             | Admins cannot change user roles                                     | 🟠 Major         |         | Open   | [D037](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/86) | |
| D038  |             | Admins cannot suspend or delete user accounts                       | 🟠 Major         |         | Open   | [D038](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/87) | |
| D039  |             | Admins cannot moderate community posts and comments                | 🟠 Major         |         | Open   | [D039](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/88) | |
| D040  |             | Admins cannot delete inappropriate content                         | 🟠 Major         |         | Open   | [D040](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/89) | |
| D041  |             | User flags/reports do not appear in admin moderation queue         | 🟠 Major         |         | Open   | [D041](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/90) | |
| D042  |             | Admins cannot publish new blog posts                                | 🟠 Major         |         | Open   | [D042](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/91) | |
| D043  |             | Users cannot mark notifications as read                            | 🟡 Minor         |         | Open   | [D043](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/92) | |
| D044  |             | Contextual help and tooltips are missing                           | 🟡 Minor         |         | Open   | [D044](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/93) | |
| D045  |             | FAQ section is missing or inaccessible                             | 🟡 Minor         |         | Open   | [D045](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/94) | |
| D046  |             | Support contact information is not visible                          | 🟡 Minor         |         | Open   | [D046](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/95) | |
| D048  |             | Breadcrumbs do not display full page hierarchy                      | 🟡 Minor         |         | Open   | - | |
| D049  |             | Search bar does not return results or apply filters                 | 🟡 Minor         |         | Open   | - | |
| D050  |             | Date selection allows today and past dates                          | 🟠 Major         |         | Open   | [D050](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96) | |
| D051  |             | Date selection allows dates beyond 30 days                          | 🟠 Major         |         | Open   | [D051](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/97) | |
| D052  |             | Name field accepts invalid lengths (<2 or >50 characters)           | 🟠 Major         |         | Open   | [D052](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/98) | |
| D053  |             | Password field allows fewer than 8 characters                       | 🟠 Major         |         | Open   | [D053](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/99) | |
| D054  |             | Instructions field allows more than 200 characters                  | 🟡 Minor         |         | Open   | [D054](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/100) | |
| D055  |             | Unicode and international characters cause email send failure       | 🟡 Minor         |         | Open   | [D055](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/101) | |
| D056  |             | Very long inputs are accepted beyond maximum length                | 🟠 Major         |         | Open   | [D056](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/102) | |


---

## **Non-Functional Test Defects**
## **Non-Functional Test Defects**

| ID    | Requirement | Issue Title                                                               | Severity | Risk ID | Status | GitHub Link |
|--------|-------------|---------------------------------------------------------------------------|----------|---------|--------|-------------|
| D-008 |              | Menu bar expands excessively when resizing window, hiding content          | Major    | R008    | Open   | [Issue #55](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) |
| D-009 |              | Low-contrast text fails WCAG 2.1 AA                                        | Major    | R008    | Open   | [Issue #56](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/56) |
| D-010 |              | Layout breaks at 200% zoom (accessibility zoom & reflow failure)           | Medium   | R008    | Open   | [Issue #57](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/57) |
| D-011 |              | Missing alt text for meaningful images                                     | Medium   | R008    | Open   | D-011 |
| D057  |              | System responds slowly to user interactions, exceeding 1-second threshold  | Major    |         | Open   | [D057](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/103) |
| D058  |              | Map fails to load under slow internet connections                          | Major    |         | Open   | D0058 |
