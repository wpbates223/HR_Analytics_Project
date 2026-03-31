# HR Workforce Analytics Platform

End-to-end HR analytics system designed to simulate how enterprise organizations like Capital One leverage data to drive workforce strategy, retention, and operational efficiency.

---

## Business Problem

HR leaders need to answer critical questions:

* Why are employees leaving?
* Which departments are at highest risk of attrition?
* What factors drive retention vs turnover?

This project builds a scalable analytics solution to support data-driven HR decision making.

---

## Executive Summary

See business insights and recommendations:
[Executive Summary](notebooks/executive_summary.md)

---

## Architecture

Raw HR Data → Python Data Pipeline → Data Quality Checks → AWS S3 → SQL Analytics → Power BI Dashboard

---

## Data Lineage

View full data flow documentation:
[Data Lineage](docs/data_lineage.md)

---

## Data Dictionary

View field definitions and business metrics:
[Data Dictionary](docs/data_dictionary.md)

---

## Attrition Risk Model

A machine learning model predicts employee attrition risk using:

- Salary
- Tenure
- Work-life balance
- Performance rating

Outputs:
- Risk score (0–1)
- Risk category (Low / Medium / High)

This enables proactive workforce retention strategies.

---

## Tech Stack

* Python (Pandas, Boto3)
* SQL
* AWS S3
* Power BI
* Git

---

## Features

### 1. Data Pipeline (Innovation)

* Cleans and transforms raw HR data
* Creates derived features (attrition flag, tenure groups)
* Outputs analytics-ready dataset

### 2. Data Quality & Governance (Data Management)

* Validates key fields (employee IDs, salary, attrition)
* Ensures data consistency and integrity
* Simulates enterprise data governance practices

### 3. SQL Analytics Layer (Business Intelligence)

* Attrition by department
* Attrition by tenure
* Workforce composition metrics

### 4. Dashboard (Business Intelligence)

Interactive dashboard providing:

* Attrition trends
* Department-level risk analysis
* Workforce insights

### 5. Cloud Integration (AWS)

* Stores raw data in AWS S3
* Demonstrates cloud-based data pipeline architecture

---

## Key Insights

* Employees with <2 years tenure show the highest attrition rates
* Work-life balance strongly correlates with retention
* Certain departments exhibit significantly higher turnover risk

---

## Project Structure

HR_Analytics_Project/<br>
│<br>
├── dashboards/<br>
├── data/<br>
├── docs/<br>
├── notebooks/<br>
├── sql/<br>
├── src/<br>
└── README.md

---

## Project Highlights

* End-to-end data pipeline development
* SQL and Python analytics 
* Data quality and governance implementation
* Business-focused analytics and storytelling
* Cloud data integration using AWS

---

## Future Improvements

* Automate pipeline using Airflow
* Expand data quality framework with Great Expectations
* Deploy dashboard to cloud

---
