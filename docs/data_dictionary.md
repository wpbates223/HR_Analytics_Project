# Data Dictionary: HR Workforce Analytics Platform

## Overview

This document defines the key data fields used in the HR Workforce Analytics Platform. It ensures consistent understanding of metrics across business and technical stakeholders.

---

## Employee Data Fields

| Column Name       | Description                                    | Data Type | Example |
| ----------------- | ---------------------------------------------- | --------- | ------- |
| employeenumber    | Unique identifier for each employee            | Integer   | 1001    |
| department        | Employee’s department within the organization  | String    | Sales   |
| jobrole           | Specific role or job title                     | String    | Manager |
| monthlyincome     | Employee’s monthly salary                      | Integer   | 5000    |
| yearsatcompany    | Total years employee has been with the company | Integer   | 5       |
| worklifebalance   | Work-life balance score (1 = low, 4 = high)    | Integer   | 3       |
| performancerating | Employee performance rating (1–4 scale)        | Integer   | 3       |

---

## Derived Fields

| Column Name    | Description                                      | Data Type | Example |
| -------------- | ------------------------------------------------ | --------- | ------- |
| attrition_flag | Binary indicator (1 = employee left, 0 = stayed) | Integer   | 1       |
| tenure_group   | Categorized tenure bucket                        | String    | 3-5     |

---

## Business Metrics

| Metric Name     | Definition                                          |
| --------------- | --------------------------------------------------- |
| Attrition Rate  | Percentage of employees who have left the company   |
| High-Risk Group | Segment of employees with elevated attrition rates  |
| Retention Rate  | Percentage of employees who remain with the company |

---

## Notes

* Attrition is derived from the original dataset field (“Yes”/“No”)
* Tenure groups are defined as:

  * 0–2 years
  * 3–5 years
  * 6–10 years
  * 10+ years

---

## Purpose

This data dictionary supports:

* Data consistency across teams
* Clear business definitions
* Alignment between technical and non-technical stakeholders
* Improved data governance practices
