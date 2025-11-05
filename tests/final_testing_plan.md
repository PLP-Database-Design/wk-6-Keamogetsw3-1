# CleanCity: Waste Pickup Scheduler - Test Management Plan

**Course:** Software Testing & Quality Assurance  
**Module:** Week 6 Module 
**Project Type:** Group Assessment  
**Team Name:** KNS  
**Submission Date:** 2025-11-05

## Team Information

| Role | Name | Responsibilities |
|------|------|------------------|
| Test Manager | Keamogetswe M| Planning, scheduling, coordination, metric tracking |
| Risk Analyst | Martin Justin| Risk identification, prioritization, test design linkage |
| Test Executor | Sally Trizer | Execution, evidence capture, defect logging |

## 1. Project Overview

This Test Management Plan defines the strategy, objectives, scope, approach, resources(tools) and schedule for testing the Waste Management Application.

### Tech Stack
- Frontend: React 18.2.0
- Routing: React Router DOM 6.3.0
- Styling: CSS3 with responsive design
- Data Storage: localStorage (no backend required)
- Testing: React Testing Library (included)

## 2. Objectives

- Verify that all functional and non-functional requirements are met.

- Identify and document software defects with reproducible evidence.

- Ensure risk-based testing coverage of critical modules.

- Validate the system’s security, usability and compatibility across devices.

- Deliver a final QA report summarizing results, metrics, and recommendations.

## 3. Schedule & Milestones

| Phase                              | Objectives                                              | Key Activities                                    | Duration      | Start Date       | Due Date       |
|-----------------------------------|--------------------------------------------------------|--------------------------------------------------|---------------|----------------|---------------|
| Phase 1: Planning & Setup          | Prepare project foundation and define testing approach | Understand application & set up environment    | 2 days       | Thu, Oct 30, 2025 | Sat, Nov 1, 2025 |
|                                   |                                                        | Create test plan & identify risks               |          2 days     |                |               |
|                                   |                                                        | Set up project board & define approach          |             2 days  |                |               |
| Phase 2: Test Design & Early Execution | Develop detailed test cases and begin initial testing | Design detailed test cases & checklists        | 1 week        | Thu, Nov 6, 2025  | Tue, Nov 11, 2025 |
|                                   |                                                        | Create test data & start early execution       |               |                |               |
|                                   |                                                        | Begin defect logging & tracking                 |               |                |               |
| Phase 3: Full Execution & Reporting | Execute all tests, document results, and finalize report | Complete full test execution with evidence     | 1 week        | Wed, Nov 12, 2025 | Tue, Nov 18, 2025 |
|                                   |                                                        | Analyze defects and prepare final reports      |               |                |               |
|                                   |                                                        | Create video presentation & documentation      |               |                |               |

## 4. Resources and Tools
# Tools and Resources

| Category            | Purpose                                           | Tools / Platforms                                |
|--------------------|-------------------------------------------------|-------------------------------------------------|
| Test Management     | Plan, track, and manage test cases and tasks   | Jira, GitHub Projects                            |
| Documentation       | Document test plans      |            |
|       | Results and reports      |            |
| Testing Tools       |  |     |
| Collaboration       | Team communication, file sharing and discussions | WhatsApp Messenger        |


## 5. Test Envronment
| Component        | Details                                            |
| ---------------- | -------------------------------------------------- |
| **Platform**     | Web Application                                    |
| **Browsers**     | Chrome, Firefox, Safari, Edge                      |
| **Devices**      | Desktop, Mobile, Tablet                            |
| **Data Storage** | localStorage                          |
| **Test Data**    | Mock users, sample pickup requests, admin accounts,Sample Blog Posts|

## Scope
### In Scope:
We will cover both both functional and non-functionaltesting of the CleanCity application.
| Type                    | Area                  | Key Focus                                           | Risk Category |
| ----------------------- | -------------------- | -------------------------------------------------- | ------------- |
| Functional Testing      | User Authentication   | Registration, login, logout, password reset       | High          |
| Functional Testing      | Waste Management      | Schedule pickups, view history, cancel requests   | High          |
| Functional Testing      | Admin Functions       | Manage requests, users, content moderation       | High       |
| Functional Testing      | Content Features      | Blog posts, comments, community features         | Medium        |
| Functional Testing      | Data Persistence      | localStorage data integrity and reliability      | High          |
| Functional Testing      | Form Validation       | Input validation, error messages, required fields|High      |
| Non-Functional Testing  | Performance           | Page load times, responsiveness                  | High          |
| Non-Functional Testing  | Usability             | User-friendliness, intuitive navigation          | Medium        |
| Non-Functional Testing  | Accessibility         | WCAG 2.1 compliance, screen reader support      | Medium        |
| Non-Functional Testing  | Security              | Input sanitization, data protection              | High          |
| Non-Functional Testing  | Compatibility         | Cross-browser and responsive design              | Medium        |


### Out of Scope:
