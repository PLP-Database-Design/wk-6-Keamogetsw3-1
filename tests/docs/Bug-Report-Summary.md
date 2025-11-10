# 🐞 CleanCity Bug Report Summary

**Project:** CleanCity – Waste Pickup Scheduler  
**Version:** 1.0  
**Prepared by:** QA Team  
**Date:** [Insert Date]  

---

## 🔍 Overview

This document provides a summary of all defects identified during manual and automated testing of the CleanCity application.  

## ✅ Expected Behaviors
List 3 things the CleanCity app should do correctly.

1. Allow users to schedule waste pickup requests with valid dates, waste types, and instructions.  
2. Enable admins to mark requests as “Scheduled” or “Completed” and have the UI update immediately.  
3. Ensure pages are accessible (with alt text, proper contrast, and keyboard navigation) and responsive across devices.

## 🐛 Reported Bugs

### 🐞 BUG-001
**Title:** Profile shows email username instead of Full Name after registration  
**GitHub Link:** #28  
**Requirement Affected:** User Registration – Profile Display  
**Severity:** Low  

---

#### 🧩 Summary
After registering a new user with a proper Full Name, the profile page displays the username portion of the email (e.g., `user1` from `newuser@test.com`) instead of the Full Name (`New Test User`) provided during registration. This may cause confusion for users, as the system does not reflect the actual name they entered.

---

#### 🔁 Steps to Reproduce
1. Register a new user with:
   - **Full Name:** `New Test User`
   - **Email:** `newuser@test.com`
   - **Password:** `NewPass123`
2. Log in with the newly registered account.  
3. Navigate to the **User Profile** page.  
4. Observe that the profile shows the email username instead of the Full Name.

---

#### ✅ Expected Result
The profile page should display the **Full Name** entered during registration.

---

#### ❌ Actual Result
The profile page displays the **username derived from the email** instead of the Full Name.

---
