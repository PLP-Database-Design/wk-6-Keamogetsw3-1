# CleanCity: Waste Pickup Scheduler - Test Report
![Alt text](cleancity.png)

# 🟢 CleanCity Project – Software Testing Report

**Version:** 1.0  
**Test Date:** [Insert Date]  
**Test Manager:** Keamogetswe  
**Tester(s):** Keamogetswe, Sally  
**Risk Analyst:** Sally Trizer  

---

## 1. Objectives

As the KNS software testing team, our objectives are to ensure the CleanCity system meets all functional and non-functional requirements, functions reliably, and is secure. We aim to detect defects early, validate performance under different conditions, enhance user experience, reduce operational risks, confirm overall quality, and ensure the CleanCity application is fully ready for deployment.  

---

## 2. Overview of the CleanCity System

CleanCity is a web-based platform designed to streamline and modernize waste management operations for residents, waste collectors, and administrators. The system allows users to report waste issues, request collection services, track the status of their submissions, and communicate directly with the management team. Administrators can monitor reports, assign tasks, update progress, and analyze waste trends. The platform aims to improve city cleanliness, enhance reporting accuracy, reduce response time, and promote transparency and accountability in urban waste management.

---

## 3. Scope of Testing

**Included:**
- Test all core CleanCity features: registration, login, and waste collection requests.
- Validate admin dashboards and data management processes.
- Perform functional, non-functional, UI, usability, security, and compatibility testing.
- Test across multiple devices and browsers.
- Validate APIs, data accuracy, error handling, and system responses.
- Assess performance under normal, peak, and extreme conditions to ensure full reliability and requirement compliance.

**Excluded:**
- Load testing beyond a certain threshold.

---

## 4. Test Environment

- **Frontend:** CleanCity Web Application (HTML, CSS, JavaScript)
- **Backend:** Node.js / Express *(adjust based on actual backend used)*
- **Database:** MySQL / MongoDB *(adjust according to project)*
- **Browsers Tested:** Chrome, Firefox, Edge
- **Devices Tested:** Windows desktop and Android smartphone
- **Test Data:** Mix of dummy data and realistic simulated user inputs
- **Tools Used:** GitHub for defect tracking and test case management, Browser DevTools for debugging

---

## 5. Test Execution Summary

### Planned Test Cases

| Category | Manual | Automated | Total |
|----------|--------|-----------|-------|
| Registration | 5 | 5 | 10 |
| Login | 5 | 5 | 10 |
| Logout | 3 | 1 | 4 |
| Role-Based Access | 4 | – | 4 |
| Pickup Scheduling | 7 | 1 | 8 |
| Request Management | 8 | – | 8 |
| Tracking | 3 | – | 3 |
| Dashboard | 3 | – | 3 |
| Blog System | 7 | – | 7 |
| Awareness | 5 | – | 5 |
| Community Feed | 3 | – | 3 |
| Community Features | 4 | – | 4 |
| Admin Functions | 4 | – | 4 |
| Session Management | 5 | – | 5 |
| Non-Functional | 20+ | – | 20+ |
| Boundary / Edge Cases | 10+ | – | 10+ |

### Executed Test Cases – Pass / Fail

| Category | Total | Pass ✅ | Fail ❌ | Defects Linked |
|----------|-------|---------|---------|----------------|
| User Registration | 10 | 10 | 0 | — |
| User Login | 10 | 6 | 4 | D-002, D-003 |
| User Logout | 4 | 2 | 2 | D-004 |
| Role-Based Access | 4 | 4 | 0 | — |
| Pickup Scheduling | 8 | 3 | 5 | D-005, D-006, D-007 |
| Request Management | 8 | 0 | 8 | D-000 |
| Request Tracking | 3 | 1 | 2 | — |
| Dashboard & Analytics | 3 | 0 | 3 | D-000 |
| Blog System | 7 | 4 | 3 | D-000 |
| Awareness Section | 5 | 5 | 0 | — |
| Community Feed | 3 | 3 | 0 | — |
| Community Features | 3 | 1 | 2 | D-001, D-002 |
| Administrative Functions | 12 | 0 | 0 | Pending |
| Notification System | 4 | 0 | 0 | Pending |
| Data Management | 5 | 5 | 0 | — |
| Support & Maintenance | 3 | 0 | 0 | Pending |
| UI / Responsiveness | 4 | 1 | 1 | D-008, D-009, D-010, D-011 |
| Navigation | 4 | 2 | 2 | — |
| Performance | 4 | 0 | 0 | Pending |
| Cross-Browser | 8 | 8 | 0 | — |
| Error Handling | 10 | 0 | 0 | Pending |
| Form Validation | 3 | 0 | 0 | Pending |
| Boundary / Edge Cases | 2+ | 0 | 0 | Pending |

---

## 6. Defect Summary

### Functional Test Defects

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link | Test Case ID |
|----|------------|---------|---------|--------|------------|-------------|
| D-001 | Profile shows email instead of full name | Cosmetic | R00 | Open | [Issue #28](#) | TC-001 |
| D-002 | Existing user can login with a completely invalid password | Critical | R001 | Open | [Issue #31](#) | TC-005 |
| D-003 | System allows login with unregistered credentials | Critical | R001 | Open | [Issue #32](#) | TC-006 |
| D-004 | Pick-up request submitted without user registration | Major | R001 | Open | [Issue #33](#) | TC-010 |
| D-005 | The pickup is scheduled even with invalid date | Medium | R003 | Open | [Issue #34](#) | TC-025 |
| D-006 | Pickup request allows instructions exceeding 200 characters | Medium | R003 | Open | [Issue #41](#) | TC-028 |
| D-007 | Scheduling multiple pickups for the same date | Medium | R003 | Open | [Issue #42](#) | TC-029 |

### Non-Functional Test Defects

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|------------|---------|---------|--------|------------|
| D-008 | Menu bar expands excessively when resizing window | Medium | R008 | Open | [Issue #55](#) |
| D-009 | Low contrast text fails WCAG 2.1 AA | Major | R008 | Open | [Issue #56](#) |

### Accessibility Test Defects

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|------------|---------|---------|--------|------------|
| D-010 | [Add title] | Major | R006 | Open / In Progress / Resolved / Closed | [Link](#) |
| D-011 | [Add title] | Major | R007 | Open / In Progress / Resolved / Closed | [Link](#) |

### Cross-Browser Compatibility Test Defects

| ID | Issue Title | Severity | Risk ID | Status | GitHub Link |
|----|------------|---------|---------|--------|------------|
| D-012 | [Add title] | Minor | R008 | Open / In Progress / Resolved / Closed | [Link](#) |
| D-013 | [Add title] | Major | R009 | Open / In Progress / Resolved / Closed | [Link](#) |

---

## 7. Defect Summary by Category

Functional testing identified 7 defects, including 2 critical, 1 major, 3 medium, and 1 cosmetic. Non-functional testing revealed 2 defects, 1 major and 1 medium. Accessibility testing included 2 major defects, while cross-browser compatibility testing identified 2 defects (1 major, 1 minor). In total, 13 defects were reported. Most critical defects relate to login and authentication issues, while medium defects primarily involve scheduling and input validations. Non-functional and accessibility defects require UI and compliance fixes. Continuous monitoring is recommended for pending and in-progress defects to ensure timely resolution.
