

## 🎯 Purpose

The purpose of the **tests** folder is to:

- Maintain structured and traceable test documentation  
- Ensure coverage of functional, non-functional, boundary and risk-based testing  
- Provide clear test cases mapped to requirements and risk IDs  
- Track execution status and defect links  

---
## 📂 Folder Structure

```bash
/tests
│
├── data/                                   # Contains all test data files
│   └── test_data.md                        # Valid, invalid, boundary & edge case test data
│
├── docs/                                   # Full test documentation library
│   ├── Bug-Report-Summary.md               # Summary of all logged bugs grouped by severity & status
│   ├── Defects-Reports.md                  # Detailed defect reports with reproduction steps
│   ├── Risk_Analysis_Form.md               # Identified risks, impact levels, mitigation steps
│   ├── Test_Cases.md                       # Complete list of all test cases with expected results & risk IDs
│   ├── Test-Execution-Report.md            # Execution results showing pass/fail and defect links
│   ├── Test_Management_Plan.md             # Strategy, scope, objectives, roles, and timelines for testing
│   ├── defect-reporting-standards.md       # Standards & guidelines for writing and managing defect reports
│   └── Final-Test-Report.md                # Final summary report at test cycle completion
│
├── Scripts/                                # Automated scripts for testing or preparing test data
│   ├──                  
│   ├──                        
│   ├──                
│   └──                         
│
├── Final-Test-Report.pdf                   # Exported PDF version of the final full test report
└── README.md                               # Documentation file explaining the test folder structure

