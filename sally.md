# CleanCity Application – QA Test Cases

📋 **Document Information**  
**Document Version:** 1.2  
**Date:** 18 November 2025  
**Project:** CleanCity - Waste Pickup Scheduler  
**Prepared For:** QA Testing Teams  

---

## 🧪 Manual Testing

### 1. Functional Test Cases

| TC | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|:--:|:--|:--|:--|:--|:--|:--:|
| TC001 | Registration | Register new user with valid data | Account created successfully | Account successfully created | Pass ✅ | R001 |
| TC002 | Registration | Register user with invalid email | Validation error displayed | Error was shown | Pass ✅ | R001 |
| TC003 | Registration | Register user with empty name | Validation error displayed | Error was shown | Pass ✅ | R001 |
| TC004 | Login | Login with correct credentials | Access granted | Logged in successfully | Pass ✅ | R001 |
| TC005 | Login | Login with wrong credentials | Error message displayed | TBD | TBD | R001 |
| TC006 | Pickup Scheduling | Schedule new pickup with valid date/time | Request created successfully | TBD | TBD | R002 |
| TC007 | Pickup Scheduling | Schedule pickup with invalid date/time | Validation error displayed | TBD | TBD | R002 |
| TC008 | Pickup Scheduling | Cancel pickup request | Request status updated to "Cancelled" | TBD | TBD | R002 |
| TC009 | localStorage | Verify persistence after page reload | Data remains saved | TBD | TBD | R003 |
| TC010 | Admin Panel | Mark pickup as scheduled | Status updated, UI refreshed | TBD | TBD | R004 |
| TC011 | Blog Module | Publish a new blog post | Post appears in blog list | TBD | TBD | R005 |
| TC012 | Community Module | Add a new community post | Post appears in feed | TBD | TBD | R005 |
| TC013 | Profile Management | Update profile information | Changes reflected in profile | TBD | TBD | R001 |

---

### 2. Non-Functional Test Cases

| TC | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|:--:|:--|:--|:--|:--|:--|:--:|
| TC014 | Performance | Load 5000+ pickup requests | UI remains responsive | TBD | TBD | R008 |
| TC015 | Performance | Load 1000+ user accounts | Application remains stable | TBD | TBD | R008 |
| TC016 | Security | Test XSS payloads in inputs | Scripts should not execute | TBD | TBD | R007 |
| TC017 | Security | Test SQL injection payloads | Inputs sanitized; no DB exposure | TBD | TBD | R007 |
| TC018 | Usability | Validate responsive navigation | Works correctly on mobile/tablet | TBD | TBD | R009 |
| TC019 | Data Persistence | Validate localStorage storage | Data persists across reloads | TBD | TBD | R003 |

---

### 3. Accessibility Test Cases

| TC | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|:--:|:--|:--|:--|:--|:--|:--:|
| TC020 | Awareness Page | Screen reader reads images | Images have descriptive alt text | TBD | TBD | R009 |
| TC021 | Forms | Keyboard navigation on registration form | All fields accessible and focusable | TBD | TBD | R009 |
| TC022 | Forms | Color contrast check | Meets WCAG 2.1 AA standards | TBD | TBD | R009 |
| TC023 | Buttons | Minimum touch target size | Buttons ≥44x44px on mobile | TBD | TBD | R009 |

---

| TC No. | Feature              | Objective                                           | Expected Result                                 | Actual Result                                      | Status     | Risk Link |
|--------:|----------------------|----------------------------------------------------|--------------------------------------------------|----------------------------------------------------|-------------|------------|
| TC024  | Registration         | Register new user with valid data                   | Account created successfully                     | Successfully registered new user in Chrome         | ✅ Pass     | R002       |
| TC025  | Login                | Login with correct credentials                      | Access granted                                   | Successfully logged in with correct password       | ✅ Pass     | R003       |
| TC026  | Login                | Login with wrong credentials                        | Error message displayed                          | Error “Wrong password” displayed as expected       | ✅ Pass     | R003       |
| TC027  | Login                | Login with the same credentials across all browsers | Invalid email or wrong password message          | Failed to login — “Invalid email or wrong password”| ❌ Fail     | R003       |
| TC028  | Dashboard Filters    | Filter by Status                                    | Only requests with selected status display       | Requests filtered correctly by status              | ✅ Pass     | R002       |
| TC029  | Dashboard Filters    | Filter by Location                                  | Only requests in selected location display       | Requests filtered correctly by location            | ✅ Pass     | R002       |
| TC030  | Pickup & Rescheduling| Verify pickup and rescheduling functions properly   | Request should be successfully rescheduled/picked| Function failed to reschedule/pickup request       | ❌ Fail     | R004       |
| TC031  | Awareness Page       | Verify awareness page loads and displays content    | Awareness page loads successfully                | Awareness page displayed correctly with all content| ✅ Pass     | R005       |

---

### 5. Boundary and Edge Case Test Cases

| TC | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|:--:|:--|:--|:--|:--|:--|:--:|
| TC028 | Registration | Enter name with minimum characters (2) | Accepted, account created | TBD | TBD | R001 |
| TC029 | Registration | Enter name with maximum characters (50) | Accepted, account created | TBD | TBD | R001 |
| TC030 | Registration | Enter password less than 8 characters | Validation error displayed | TBD | TBD | R001 |
| TC031 | Pickup Scheduling | Schedule pickup on earliest allowed date | Request created successfully | TBD | TBD | R002 |
| TC032 | Pickup Scheduling | Schedule pickup on latest allowed date (30 days) | Request created successfully | TBD | TBD | R002 |
| TC033 | Pickup Scheduling | Enter very long pickup instructions (>200 chars) | Validation error displayed | TBD | TBD | R002 |
| TC034 | Community Module | Input Unicode characters in post/comment | Displayed correctly | TBD | TBD | R005 |
| TC035 | Community Module | Input HTML/JS scripts | Sanitized; no script execution | TBD | TBD | R007 |
| TC036 | Offline Functionality | Disconnect internet during pickup scheduling | Show offline error and retry | TBD | TBD | R011 |
| TC037 | Data Backup | Simulate DB failure | Backup/restore works correctly | TBD | TBD | R012 |

---

## 🤖 Automated Testing (High-Risk Priority Focus)

| TC | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|:--:|:--|:--|:--|:--|:--|:--:|
| TC038 | Registration | Register new user with valid data | Account created successfully | TBD | TBD | R001 |
| TC039 | Login | Login with correct credentials | Access granted | TBD | TBD | R001 |
| TC040 | Pickup Scheduling | Create new pickup (valid inputs) | Request created successfully | TBD | TBD | R002 |
| TC041 | Security | Run automated XSS/SQL tests | No vulnerabilities found | TBD | TBD | R007 |
| TC042 | Performance | Simulate 100 concurrent requests | Response time < 3s | TBD | TBD | R008 |
| TC043 | localStorage | Verify session persistence via script | Data retained post-refresh | TBD | TBD | R003 |
| TC044 | Admin Panel | Mark pickup as scheduled (automated) | Status updated successfully | TBD | TBD | R004 |
| TC045 | Blog Module | Publish post via API | Post saved and retrieved successfully | TBD | TBD | R005 |
| TC046 | Mobile Responsiveness | Auto UI snapshot validation | All layouts render correctly | TBD | TBD | R009 |

---

### 🧭 Summary of Adjustments
- ✅ **Updated Risk Links** to match your official risk register (R001–R012).  
- 🔺 **Added new tests** for **offline handling (R011)** and **data integrity (R012)**.  
- ⚙️ **Merged and refined performance/security cases** based on high-priority risks (R007, R008).  
- 📱 **Cross-browser & accessibility** tests now linked correctly to **R009 (Mobile & Cross-browser)**.  

---



