# CleanCity Application - Risk Analysis

📋 **Document Information**  
**Document Version:** 1.1  
**Date:** 18 November 2025  
**Project:** CleanCity - Waste Pickup Scheduler  
**Prepared For:** QA Testing Teams  

---

## ⚠️ Risks Table

| ID | Feature | Risk Description | Likelihood | Impact | Priority | Mitigation Strategy |
|:--:|:--|:--|:--:|:--:|:--:|:--|
| R001 | Registration & Login | Authentication errors, weak password validation, and incorrect credential handling | Medium | High | High | Add strong validation, implement secure API calls, and perform boundary testing |
| R002 | Pickup Scheduling | Form crashes on invalid date/time; incorrect pickup slot allocation | High | High | High | Enforce date/time validation, run functional and integration tests early |
| R003 | localStorage Data | Data loss or corruption during page reloads or session timeout | Medium | High | High | Regularly test localStorage persistence and implement backup saving logic |
| R004 | Admin Panel | Restricted access failure or role mismanagement | Medium | Medium | Medium | Implement role-based access control and validate admin endpoints |
| R005 | Blog & Community Features | Comment section or post creation may fail due to API errors | High | Medium | High | Conduct API testing and input sanitization; add retry logic |
| R006 | Form Validation | Missing field-level validation causing data entry errors | Medium | Medium | Medium | Add both client- and server-side validation with clear error prompts |
| R007 | Security | Unsecured API calls, lack of HTTPS, or potential XSS vulnerabilities | High | High | High | Apply HTTPS, sanitize inputs, and perform penetration testing |
| R008 | Performance & Load | Slow response or timeout during high user traffic | Medium | High | High | Conduct load and stress testing; optimize API responses |
| R009 | Mobile & Cross-browser | UI misalignment or functionality issues on smaller screens | Medium | Medium | Medium | Perform cross-device compatibility testing |
| R010 | Notifications & Alerts | Delayed or missing notifications for pickup confirmation | Medium | Medium | Medium | Test notification logic and set fallback messages |
| R011 | Offline & Network Issues | App fails to handle poor connectivity or offline mode | Low | Medium | Medium | Implement offline caching and retry mechanisms |
| R012 | Data Integrity & Backup | Missing database constraints or failed data backup | Medium | Medium | Medium | Enforce data integrity rules and schedule auto-backups |

---

## 📊 Risk Matrix

**Legend:**  
- **Likelihood:** High / Medium / Low  
- **Impact:** High / Medium / Low  

| Impact \ Likelihood | Low | Medium | High |
|:--|:--|:--|:--|
| **High** | R011 | R001, R003 | R002, R007, R008 |
| **Medium** | – | R004, R006, R009, R010, R012 | R005 |
| **Low** | – | – | – |

---

## ✅ Risk Coverage

| Metric | Percentage |
|:--|:--:|
| **Tested Risks** | 70% |
| **Untested Risks** | 30% |

**Notes:**  
- **Tested Risks:** Form validation, date/time boundaries, UI responsiveness, localStorage persistence, accessibility checks, and security payload validation.  
- **Untested Risks:** Performance under extreme load, notification delivery reliability, and offline caching scenarios.
