# 🐞 Defect Log – CleanCity Project

## **Functional Test Defects**

| ID    | Requirement | Issue Title                                                        | Severity        | Risk ID | Status | GitHub Link | Test Case ID |
|-------|-------------|--------------------------------------------------------------------|------------------|---------|--------|-------------|--------------|
| D001 |             | Profile shows email instead of full name                           | 🟢 Cosmetic      | R013     | Open   | [Issue #28](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/28) | |
| D002 |   🔐 Authentication System    | Existing user can login with a completely invalid password         | 🔴 Critical      | R001    | Open   | [Issue #31](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/31) | TC012 / TC018  |
| D003 |             | System allows login with unregistered credentials                  | 🔴 Critical      | R001    | Open   | [Issue #32](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/32) | TC015 / TC020 |
| D004 |             | Pick-up request submitted without user registration                | 🔴 Critical      | R002    | Open   | [Issue #33](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/33) | TC023 |
| D-005 | Waste Management | Pickup is scheduled even with past/invalid date                    | 🟠 Major         | R002    | Open   | [Issue #34](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/34) | TC031 |
| D-006 |             | Instructions exceeding 200 characters accepted without validation  | 🟡 Minor         | R006    | Open   | [Issue #41](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/41) | TC034 |
| D-007 |             | System allows scheduling multiple pickups for the same date        | 🟠 Major         | R002    | Open   | [Issue #42](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/42) | TC035 |
| D-012 |             | User cannot view past and current pickup request history           | 🟠 Major         | R002    | Open   | [Issue #61](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/61) | TC037 |
| D-013 |             | Completed and cancelled pickup requests not shown in dashboard     | 🟠 Major         | R002    | Open   | [Issue #62](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/62) | TC038 |
| D-014 |             | User cannot cancel a pending pickup request                        | 🟠 Major         | R002    | Open   | [Issue #63](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/63) | TC039|
| D-015 |             | Completed/cancelled requests can potentially be cancelled again    | 🟠 Major         | R002    | Open   | [Issue #64](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/64) | TC040 |
| D-016 |             | User cannot modify pickup details 24 hours before scheduled time   | 🟠 Major         | R002    | Open   | [Issue #65](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/65) | TC041|
| D-017 |             | System allows modification within 24 hours of scheduled pickup     | 🟠 Major         | R002    | Open   | [Issue #66](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/66) | TC042  |
| D-018 |             | Pickup status not displayed correctly                              | 🟠 Major         | R002    | Open   | [Issue #67](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/67) | TC043 |
| D-019 |             | Pickup status does not update dynamically after completion/cancellation | 🟠 Major     | R002 | Open | [Issue #68](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/68) | TC044 |
| D-020 |             | Pickup request status does not update in real-time                 | 🟠 Major         | R002    | Open   | [Issue #69](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/69) | TC045 |
| D-021 |             | Users do not receive notifications for pickup request status changes | 🟠 Major     | R010 | Open | [Issue #70](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/70) | TC046 |
| D-022 |             | Feedback not associated with completed pickup                      | 🟠 Major         | R002    | Open   | [Issue #71](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/71) | TC047 |
| D-023 | 📊 Dashboard & Analytics | Dashboard does not display personalized information for logged-in users | 🟠 Major   | R013 | Open | [Issue #72](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/72) | TC048 |
| D-024 |             | Environmental impact metrics not displayed on dashboard            | 🟡 Minor         | R013    | Open   | [Issue #73](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/73) | TC049 |
| D-025 |             | Badges for achievements display incorrectly on dashboard           | 🟢 Cosmetic      | R013    | Open   | [Issue #74](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/74) | TTC050 |
| D-026 | 📝 Content Management  | Admins cannot create a blog post                                   | 🟡 Minor        | R005    | Open   | [Issue #75](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/75) | TC054 |
| D-027 |             | Admins cannot edit an existing blog post                           | 🟠 Major         | R005    | Open   | [Issue #76](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/76) | TC055 |
| D-028 |             | Admins cannot delete a blog post                                   | 🟠 Major         | R005    | Open   | [Issue #77](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/77) | TC056 |
| D-029 |  Community Features  | Profile picture upload fails with server error                     | 🟢 Cosmetic      | R013    | Open   | [Issue #78](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/78) | TC067 |
| D030  |             | Users cannot follow or unfollow other community members            | 🟡 Minor         |    R005     | Open   | [D030](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/79) | TC068  |
| D031  |             | News feed does not display latest community activities             | 🟡 Minor         |   R005      | Open   | [D031](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/80) | TC069 |
| D032  | ⚙️ Administrative Functions  | Admins cannot approve, reject, or modify pickup requests           | 🟠 Major |  R004  | Open   | [D032](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/81) | TC071 |
| D033  |             | Admins cannot assign or update pickup dates and times              | 🟠 Major         |  R004  | Open   | [D033](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/82) | TC072 |
| D034  |             | Admins cannot filter or search pickup requests correctly           | 🟡 Minor         | R004 | Open   | [D034](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/83) | TC073  |
| D035  |             | Admins cannot receive or reply to feedback                         | 🟠 Major         | R004 | Open   | [D035](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/84) | TC074 |
| D036  |             | Admins cannot view all registered users                             | 🟠 Major         | R004| Open   | [D036](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/85) |TC075 |
| D037  |             | Admins cannot change user roles                                     | 🟠 Major         | R004 | Open   | [D037](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/86) | TC076  |
| D038  |             | Admins cannot suspend or delete user accounts                       | 🟠 Major         |  R004 | Open   | [D038](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/87) | TC077 |
| D039  |             | Admins cannot moderate community posts and comments                | 🟠 Major         |  R004  | Open   | [D039](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/88) | TC079 |
| D040  |             | Admins cannot delete inappropriate content                         | 🟠 Major         |  R004 | Open   | [D040](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/89) | TC080 |
| D041  |             | User flags/reports do not appear in admin moderation queue         | 🟠 Major         | R004 | Open   | [D041](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/90) | TC081 |
| D042  |             | Admins cannot publish new blog posts                                | 🟠 Major         | R004 | Open   | [D042](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/91) | TC083 |
| D043  | 🔔 Notification System  | Users cannot mark notifications as read                            | 🟡 Minor         | R010 | Open   | [D043](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/92) | TC086 |
| D044  | 📞 Support & Maintenance | Contextual help and tooltips are missing                           | 🟡 Minor         |   R010      | Open   | [D044](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/93) | TC093 |
| D045  |             | FAQ section is missing or inaccessible                             | 🟡 Minor         |    R010     | Open   | [D045](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/94) | TC094 |
| D046  |             | Support contact information is not visible                          | 🟡 Minor         |  R010   | Open   | [D046](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/95) | TC095  |

---
## **Non-Functional Test Defects**

| ID    | Requirement | Issue Title                                                               | Severity | Risk ID | Status | GitHub Link | TC |
|--------|-------------|---------------------------------------------------------------------------|----------|---------|--------|-------------|-----|
| D008 | 📱User Interface  | Menu bar expands excessively when resizing window, hiding content    | 🟠 Major | R008    | Open   | [Issue #55](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55) | TC098 |
| D047  |             | Menu bar expands excessively when resizing window  | 🔴 Critical  | R008   | Open   | [Issue #55](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/55)  | TC101  |
| D009 |              | Low-contrast text fails WCAG 2.1 AA                                        | 🟠 Major | R008    | Open   | [Issue #56](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/56) |  TC107   |
| D-010 |              | Layout breaks at 200% zoom (accessibility zoom & reflow failure)           | 🟠 Major | R008    | Open   | [Issue #57](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/57) | TC103 |
| D-011 |              | Missing alt text for meaningful images                                     | 🟠 Major | R008    | Open   | [D-011](httpsgithub.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/59) | TC105 |
| D048  |             | Breadcrumbs do not display full page hierarchy                      | 🟡 Minor         | R008 | Open   | [D048](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96) | TC110 |
| D049  |             | Search bar does not return results or apply filters                 | 🟡 Minor         |  R008  | Open   |  [D049](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96) | TC111  |
| D057  |  🚀 Performance   | System responds slowly to user interactions, exceeding 1-second threshold  | 🟠 Major  |  R008  | Open   | [D057](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/103) | TC117 |
| D058  |  📋 Error Handling  | Map fails to load under slow internet connections | 🟠 Major   | R011| Open   | [D050](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96) | TC122 |

---
## Boundary Testing and Edge Case Test
| D050  |             | Date selection allows today and past dates                          | 🟠 Major         | R006 | Open   | [D050](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/96) | TC129  |
| D051  |             | Date selection allows dates beyond 30 days                          | 🟠 Major         | R006  | Open   | [D051](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/97) | TC130 |
| D052  |             | Name field accepts invalid lengths (<2 or >50 characters)           | 🟠 Major         | R006 | Open   | [D052](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/98) | TC131|
| D053  |             | Password field allows fewer than 8 characters                       | 🔴 Critical       | R006 | Open   | [D053](httpsgithub.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/99) | TC133  |
| D054  |             | Instructions field allows more than 200 characters                  | 🟡 Minor         | R006 | Open   | [D054](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/100) | TC134 |
| D055  |             | Unicode and international characters cause email send failure       | 🟠 Major         | R006 | Open   | [D055](httpsgithub.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/101) | TC136  |
| D056  |             | Very long inputs are accepted beyond maximum length                | 🟠 Major         | R006 | Open   | [D056](https://github.com/Keamogetsw3/CleanCity-Waste_Pickup_Scheduler-QATesting/issues/102) | TC137 |


