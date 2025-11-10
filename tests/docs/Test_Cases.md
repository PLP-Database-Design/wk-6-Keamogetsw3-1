# CleanCity Application – QA Test Cases
## 📋 Document Information
**Document Version:** 1.1  
**Date:** [Current Date]  
**Project:** CleanCity - Waste Pickup Scheduler  
**Prepared For:** QA Testing Teams 

## Manual Testing

### **1. Functional Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| TC001 | Registration           | Register new user with valid data                | Account created successfully                             | TBD           | TBD     | R002      |
| F002 | Registration           | Register user with invalid email                 | Validation error displayed                                | TBD           | TBD     | R002      |
| F003 | Login                  | Login with correct credentials                   | Access granted                                          | TBD           | TBD     | R003      |
| F004 | Login                  | Login with wrong credentials                     | Error message displayed                                  | TBD           | TBD     | R003      |
| F005 | Pickup Scheduling      | Schedule new pickup                              | Request created successfully                             | TBD           | TBD     | R006      |
| F006 | Pickup Scheduling      | Cancel pickup request                            | Request status updated to "Cancelled"                   | TBD           | TBD     | R006      |
| F007 | Blog Module            | Publish a new blog post                          | Post appears in blog list                                 | TBD           | TBD     | R007      |
| F008 | Community Module       | Add a new post                                  | Post appears in community feed                            | TBD           | TBD     | R011      |
| F009 | Profile Management     | Update profile information                       | Changes reflected in user profile                        | TBD           | TBD     | R002      |
| F010 | Admin Panel            | Mark pickup as scheduled                          | Status updated, UI refreshed                              | TBD           | TBD     | R008      |

---

## **2. Non-Functional Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| NF001| Performance            | Load 5000+ pickup requests                       | UI should remain responsive                             | TBD           | TBD     | R016      |
| NF002| Performance            | Load 1000+ user accounts                          | Application remains stable                               | TBD           | TBD     | R016      |
| NF003| Security               | Test XSS payloads in inputs                       | Scripts should not execute                                | TBD           | TBD     | R012      |
| NF004| Security               | Test SQL injection payloads                        | Should be rejected / sanitized                           | TBD           | TBD     | R012      |
| NF005| Usability              | Validate responsive navigation                     | Works correctly on mobile and tablet                     | TBD           | TBD     | R009      |
| NF006| Data Persistence       | Validate localStorage storage                      | Data persists across page reloads                        | TBD           | TBD     | R013      |

---

## **3. Accessibility Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| A001 | Awareness Page         | Screen reader reads images                        | Images have descriptive alt text                        | TBD           | TBD     | R010      |
| A002 | Forms                  | Keyboard navigation on registration form          | All fields accessible and focusable                     | TBD           | TBD     | R010      |
| A003 | Forms                  | Color contrast check                               | Meets WCAG 2.1 AA standards                             | TBD           | TBD     | R010      |
| A004 | Buttons                | Minimum touch target size                          | Buttons are ≥44x44px on mobile                          | TBD           | TBD     | R010      |

---

## **4. Cross-Browser Compatibility Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| CB001| Registration           | Test in Chrome, Firefox, Safari, Edge            | Form works consistently in all browsers                | TBD           | TBD     | R017      |
| CB002| Pickup Scheduling      | Test in Chrome, Firefox, Safari, Edge            | Requests can be created and viewed in all browsers     | TBD           | TBD     | R017      |
| CB003| Blog Module            | Test in Chrome, Firefox, Safari, Edge            | Blog posts render correctly in all browsers            | TBD           | TBD     | R017      |
| CB004| Community Module       | Test in Chrome, Firefox, Safari, Edge            | Posts, comments, and likes function in all browsers    | TBD           | TBD     | R017      |

---

## **5. Boundary and Edge Case Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| B001 | Registration           | Enter name with minimum characters (2)           | Accepted and account created                             | TBD           | TBD     | R002      |
| B002 | Registration           | Enter name with maximum characters (50)          | Accepted and account created                             | TBD           | TBD     | R002      |
| B003 | Registration           | Enter email with special characters               | Accepted if valid format                                  | TBD           | TBD     | R002      |
| B004 | Registration           | Enter password less than 8 characters            | Validation error displayed                                | TBD           | TBD     | R014      |
| B005 | Pickup Scheduling      | Schedule pickup on minimum allowed date (tomorrow)| Accepted, request created                                | TBD           | TBD     | R006      |
| B006 | Pickup Scheduling      | Schedule pickup on maximum allowed date (30 days)| Accepted, request created                                | TBD           | TBD     | R006      |
| B007 | Pickup Scheduling      | Enter very long instructions (>200 chars)       | Validation error displayed                                | TBD           | TBD     | R015      |
| B008 | Community Module       | Input Unicode characters in post/comment        | Displayed correctly without errors                       | TBD           | TBD     | R011      |
| B009 | Community Module       | Input HTML or JS scripts                          | Sanitized, no script executed                             | TBD           | TBD     | R012      |
| B010 | Profile Update         | Empty or whitespace-only inputs                  | Validation error displayed                                | TBD           | TBD     | R002      |


## Automated Testing

### **1. Functional Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| F001 | Registration           | Register new user with valid data                | Account created successfully                             | TBD           | TBD     | R002      |
| F002 | Registration           | Register user with invalid email                 | Validation error displayed                                | TBD           | TBD     | R002      |
| F003 | Login                  | Login with correct credentials                   | Access granted                                          | TBD           | TBD     | R003      |
| F004 | Login                  | Login with wrong credentials                     | Error message displayed                                  | TBD           | TBD     | R003      |
| F005 | Pickup Scheduling      | Schedule new pickup                              | Request created successfully                             | TBD           | TBD     | R006      |
| F006 | Pickup Scheduling      | Cancel pickup request                            | Request status updated to "Cancelled"                   | TBD           | TBD     | R006      |
| F007 | Blog Module            | Publish a new blog post                          | Post appears in blog list                                 | TBD           | TBD     | R007      |
| F008 | Community Module       | Add a new post                                  | Post appears in community feed                            | TBD           | TBD     | R011      |
| F009 | Profile Management     | Update profile information                       | Changes reflected in user profile                        | TBD           | TBD     | R002      |
| F010 | Admin Panel            | Mark pickup as scheduled                          | Status updated, UI refreshed                              | TBD           | TBD     | R008      |

---

## **2. Non-Functional Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| NF001| Performance            | Load 5000+ pickup requests                       | UI should remain responsive                             | TBD           | TBD     | R016      |
| NF002| Performance            | Load 1000+ user accounts                          | Application remains stable                               | TBD           | TBD     | R016      |
| NF003| Security               | Test XSS payloads in inputs                       | Scripts should not execute                                | TBD           | TBD     | R012      |
| NF004| Security               | Test SQL injection payloads                        | Should be rejected / sanitized                           | TBD           | TBD     | R012      |
| NF005| Usability              | Validate responsive navigation                     | Works correctly on mobile and tablet                     | TBD           | TBD     | R009      |
| NF006| Data Persistence       | Validate localStorage storage                      | Data persists across page reloads                        | TBD           | TBD     | R013      |

---

## **3. Accessibility Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| A001 | Awareness Page         | Screen reader reads images                        | Images have descriptive alt text                        | TBD           | TBD     | R010      |
| A002 | Forms                  | Keyboard navigation on registration form          | All fields accessible and focusable                     | TBD           | TBD     | R010      |
| A003 | Forms                  | Color contrast check                               | Meets WCAG 2.1 AA standards                             | TBD           | TBD     | R010      |
| A004 | Buttons                | Minimum touch target size                          | Buttons are ≥44x44px on mobile                          | TBD           | TBD     | R010      |

---

## **4. Cross-Browser Compatibility Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| CB001| Registration           | Test in Chrome, Firefox, Safari, Edge            | Form works consistently in all browsers                | TBD           | TBD     | R017      |
| CB002| Pickup Scheduling      | Test in Chrome, Firefox, Safari, Edge            | Requests can be created and viewed in all browsers     | TBD           | TBD     | R017      |
| CB003| Blog Module            | Test in Chrome, Firefox, Safari, Edge            | Blog posts render correctly in all browsers            | TBD           | TBD     | R017      |
| CB004| Community Module       | Test in Chrome, Firefox, Safari, Edge            | Posts, comments, and likes function in all browsers    | TBD           | TBD     | R017      |

---

## **5. Boundary and Edge Case Test Cases**

| ID   | Feature                | Objective                                         | Expected Result                                         | Actual Result | Status  | Risk Link |
|------|------------------------|--------------------------------------------------|--------------------------------------------------------|---------------|---------|-----------|
| B001 | Registration           | Enter name with minimum characters (2)           | Accepted and account created                             | TBD           | TBD     | R002      |
| B002 | Registration           | Enter name with maximum characters (50)          | Accepted and account created                             | TBD           | TBD     | R002      |
| B003 | Registration           | Enter email with special characters               | Accepted if valid format                                  | TBD           | TBD     | R002      |
| B004 | Registration           | Enter password less than 8 characters            | Validation error displayed                                | TBD           | TBD     | R014      |
| B005 | Pickup Scheduling      | Schedule pickup on minimum allowed date (tomorrow)| Accepted, request created                                | TBD           | TBD     | R006      |
| B006 | Pickup Scheduling      | Schedule pickup on maximum allowed date (30 days)| Accepted, request created                                | TBD           | TBD     | R006      |
| B007 | Pickup Scheduling      | Enter very long instructions (>200 chars)       | Validation error displayed                                | TBD           | TBD     | R015      |
| B008 | Community Module       | Input Unicode characters in post/comment        | Displayed correctly without errors                       | TBD           | TBD     | R011      |
| B009 | Community Module       | Input HTML or JS scripts                          | Sanitized, no script executed                             | TBD           | TBD     | R012      |
| B010 | Profile Update         | Empty or whitespace-only inputs                  | Validation error displayed                                | TBD           | TBD     | R002      |
