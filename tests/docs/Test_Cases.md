# CleanCity Application – QA Test Cases

## 📋 Document Information
**Document Version:** 1.1  
**Date:** 18 Novemeber 2025  
**Project:** CleanCity - Waste Pickup Scheduler  
**Prepared For:** QA Testing Teams 

---

## Manual Testing

### **1. Functional Test Cases**

#### 1.1 Registration Test Cases

| Test Case ID | Objective                         | Expected Result              | Risk Link |
| ----- | --------------------------------- | ---------------------------- | --------- |
| TC-001 | Register new user with valid data | Account created successfully | R002      |
| TC-002 | Register user with invalid email  | Validation error displayed   | R002      |
| TC-003 | Register user with empty name     | Validation error displayed   | R002      |
| TC-004 | Register user with empty email    | Validation error displayed   | R002      |
| TC-005 | Register user with empty password | Validation error displayed   | R002      |

#### 1.2 Login Test Cases

| Test Case ID | Objective                                | Expected Result                       | Risk Link |
|--------------|-----------------------------------------|---------------------------------------|-----------|
| TC-006      | Login with valid credentials             | Login successful                      | R003      |
| TC-007      | Login with invalid password              | Error: "Invalid email or password"    | R003      |
| TC-008      | Login with non-existent user             | Error: "Invalid email or password"    | R003      |






| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC001 | Registration | Register new user with valid data | Account created successfully | Account successfully created | Pass ✅ | R002 |
| TC002 | Registration | Register user with invalid email | Validation error displayed | Error was shown | Pass ✅| R002 |
| TC003 | Registration | Register user with empty name | Validation error displayed | Error was shown | Pass ✅| R002 |
| TC003 | Login | Login with correct credentials | Access granted | Logged in successfully | Pass ✅ | R003 |
| TC004 | Login | Login with wrong credentials | Error message displayed | TBD | TBD | R003 |
| TC005 | Pickup Scheduling | Schedule new pickup | Request created successfully | TBD | TBD | R006 |
| TC006 | Pickup Scheduling | Cancel pickup request | Request status updated to "Cancelled" | TBD | TBD | R006 |
| TC007 | Blog Module | Publish a new blog post | Post appears in blog list | TBD | TBD | R007 |
| TC008 | Community Module | Add a new post | Post appears in community feed | TBD | TBD | R011 |
| TC009 | Profile Management | Update profile information | Changes reflected in user profile | TBD | TBD | R002 |
| TC010 | Admin Panel | Mark pickup as scheduled | Status updated, UI refreshed | TBD | TBD | R008 |

---

### **2. Non-Functional Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC011 | Performance | Load 5000+ pickup requests | UI should remain responsive | TBD | TBD | R016 |
| TC012 | Performance | Load 1000+ user accounts | Application remains stable | TBD | TBD | R016 |
| TC013 | Security | Test XSS payloads in inputs | Scripts should not execute | TBD | TBD | R012 |
| TC014 | Security | Test SQL injection payloads | Should be rejected / sanitized | TBD | TBD | R012 |
| TC015 | Usability | Validate responsive navigation | Works correctly on mobile and tablet | TBD | TBD | R009 |
| TC016 | Data Persistence | Validate localStorage storage | Data persists across page reloads | TBD | TBD | R013 |

---

### **3. Accessibility Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC017 | Awareness Page | Screen reader reads images | Images have descriptive alt text | TBD | TBD | R010 |
| TC018 | Forms | Keyboard navigation on registration form | All fields accessible and focusable | TBD | TBD | R010 |
| TC019 | Forms | Color contrast check | Meets WCAG 2.1 AA standards | TBD | TBD | R010 |
| TC020 | Buttons | Minimum touch target size | Buttons are ≥44x44px on mobile | TBD | TBD | R010 |

---

### **4. Cross-Browser Compatibility Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC021 | Registration | Test in Chrome, Firefox, Safari, Edge | Form works consistently in all browsers | TBD | TBD | R017 |
| TC022 | Pickup Scheduling | Test in Chrome, Firefox, Safari, Edge | Requests can be created and viewed in all browsers | TBD | TBD | R017 |
| TC023 | Blog Module | Test in Chrome, Firefox, Safari, Edge | Blog posts render correctly in all browsers | TBD | TBD | R017 |
| TC024 | Community Module | Test in Chrome, Firefox, Safari, Edge | Posts, comments, and likes function in all browsers | TBD | TBD | R017 |

---

### **5. Boundary and Edge Case Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC025 | Registration | Enter name with minimum characters (2) | Accepted and account created | TBD | TBD | R002 |
| TC026 | Registration | Enter name with maximum characters (50) | Accepted and account created | TBD | TBD | R002 |
| TC027 | Registration | Enter email with special characters | Accepted if valid format | TBD | TBD | R002 |
| TC028 | Registration | Enter password less than 8 characters | Validation error displayed | TBD | TBD | R014 |
| TC029 | Pickup Scheduling | Schedule pickup on minimum allowed date (tomorrow) | Accepted, request created | TBD | TBD | R006 |
| TC030 | Pickup Scheduling | Schedule pickup on maximum allowed date (30 days) | Accepted, request created | TBD | TBD | R006 |
| TC031 | Pickup Scheduling | Enter very long instructions (>200 chars) | Validation error displayed | TBD | TBD | R015 |
| TC032 | Community Module | Input Unicode characters in post/comment | Displayed correctly without errors | TBD | TBD | R011 |
| TC033 | Community Module | Input HTML or JS scripts | Sanitized, no script executed | TBD | TBD | R012 |
| TC034 | Profile Update | Empty or whitespace-only inputs | Validation error displayed | TBD | TBD | R002 |

---

## Automated Testing

### **1. Functional Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC035 | Registration | Register new user with valid data | Account created successfully | TBD | TBD | R002 |
| TC036 | Registration | Register user with invalid email | Validation error displayed | TBD | TBD | R002 |
| TC037 | Login | Login with correct credentials | Access granted | TBD | TBD | R003 |
| TC038 | Login | Login with wrong credentials | Error message displayed | TBD | TBD | R003 |
| TC039 | Pickup Scheduling | Schedule new pickup | Request created successfully | TBD | TBD | R006 |
| TC040 | Pickup Scheduling | Cancel pickup request | Request status updated to "Cancelled" | TBD | TBD | R006 |
| TC041 | Blog Module | Publish a new blog post | Post appears in blog list | TBD | TBD | R007 |
| TC042 | Community Module | Add a new post | Post appears in community feed | TBD | TBD | R011 |
| TC043 | Profile Management | Update profile information | Changes reflected in user profile | TBD | TBD | R002 |
| TC044 | Admin Panel | Mark pickup as scheduled | Status updated, UI refreshed | TBD | TBD | R008 |

---

### **2. Non-Functional Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC045 | Performance | Load 5000+ pickup requests | UI should remain responsive | TBD | TBD | R016 |
| TC046 | Performance | Load 1000+ user accounts | Application remains stable | TBD | TBD | R016 |
| TC047 | Security | Test XSS payloads in inputs | Scripts should not execute | TBD | TBD | R012 |
| TC048 | Security | Test SQL injection payloads | Should be rejected / sanitized | TBD | TBD | R012 |
| TC049 | Usability | Validate responsive navigation | Works correctly on mobile and tablet | TBD | TBD | R009 |
| TC050 | Data Persistence | Validate localStorage storage | Data persists across page reloads | TBD | TBD | R013 |

---

### **3. Accessibility Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC051 | Awareness Page | Screen reader reads images | Images have descriptive alt text | TBD | TBD | R010 |
| TC052 | Forms | Keyboard navigation on registration form | All fields accessible and focusable | TBD | TBD | R010 |
| TC053 | Forms | Color contrast check | Meets WCAG 2.1 AA standards | TBD | TBD | R010 |
| TC054 | Buttons | Minimum touch target size | Buttons are ≥44x44px on mobile | TBD | TBD | R010 |

---

### **4. Cross-Browser Compatibility Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC055 | Registration | Test in Chrome, Firefox, Safari, Edge | Form works consistently in all browsers | TBD | TBD | R017 |
| TC056 | Pickup Scheduling | Test in Chrome, Firefox, Safari, Edge | Requests can be created and viewed in all browsers | TBD | TBD | R017 |
| TC057 | Blog Module | Test in Chrome, Firefox, Safari, Edge | Blog posts render correctly in all browsers | TBD | TBD | R017 |
| TC058 | Community Module | Test in Chrome, Firefox, Safari, Edge | Posts, comments, and likes function in all browsers | TBD | TBD | R017 |

---

### **5. Boundary and Edge Case Test Cases**

| TC (number) | Feature | Objective | Expected Result | Actual Result | Status | Risk Link |
|--------------|----------|------------|----------------|----------------|---------|-----------|
| TC059 | Registration | Enter name with minimum characters (2) | Accepted and account created | TBD | TBD | R002 |
| TC060 | Registration | Enter name with maximum characters (50) | Accepted and account created | TBD | TBD | R002 |
| TC061 | Registration | Enter email with special characters | Accepted if valid format | TBD | TBD | R002 |
| TC062 | Registration | Enter password less than 8 characters | Validation error displayed | TBD | TBD | R014 |
| TC063 | Pickup Scheduling | Schedule pickup on minimum allowed date (tomorrow) | Accepted, request created | TBD | TBD | R006 |
| TC064 | Pickup Scheduling | Schedule pickup on maximum allowed date (30 days) | Accepted, request created | TBD | TBD | R006 |
| TC065 | Pickup Scheduling | Enter very long instructions (>200 chars) | Validation error displayed | TBD | TBD | R015 |
| TC066 | Community Module | Input Unicode characters in post/comment | Displayed correctly without errors | TBD | TBD | R011 |
| TC067 | Community Module | Input HTML or JS scripts | Sanitized, no script executed | TBD | TBD | R012 |
| TC068 | Profile Update | Empty or whitespace-only inputs | Validation error displayed | TBD | TBD | R002 |
