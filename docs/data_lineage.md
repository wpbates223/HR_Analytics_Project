# Data Lineage: HR Workforce Analytics Platform

## Overview

This document outlines the flow of data through the HR Workforce Analytics Platform, from raw ingestion to final business insights.

---

## Data Flow

### 1. Raw Data Source

* Source: IBM HR Analytics Dataset (CSV)
* Location: `data/raw_hr_data.csv`

This dataset contains employee-level information including demographics, compensation, tenure, and attrition.

---

### 2. Data Ingestion & Transformation (Python Pipeline)

File: `src/data_pipeline.py`

Key transformations:

* Standardized column names
* Created `attrition_flag` (binary indicator)
* Created `tenure_group` buckets
* Cleaned and structured dataset for analysis

Output:

* `data/clean_hr_data.csv`

---

### 3. Data Quality Validation

File: `src/data_quality_checks.py`

Validation checks include:

* No missing employee IDs
* Valid salary ranges
* Correct attrition flag values (0 or 1)

Purpose:
Ensure accuracy, consistency, and reliability of HR data.

---

### 4. Cloud Storage (AWS S3)

* Raw data uploaded to AWS S3
* Enables scalable storage and future pipeline integration

Example:

* `s3://hr-analytics-project-bucket/raw/raw_hr_data.csv`

---

### 5. Analytical Layer (SQL)

Files:

* `sql/create_tables.sql`
* `sql/analysis_queries.sql`

Used to:

* Aggregate attrition metrics
* Analyze trends across departments and tenure groups

---

### 6. Data Visualization (Dashboard)

Tool: Power BI

Input:

* Cleaned dataset (`clean_hr_data.csv`)

Output:

* Interactive dashboard with:

  * Attrition trends
  * Department-level analysis
  * Workforce insights

---

### 7. Business Consumption

Outputs consumed by:

* HR Leadership
* Business stakeholders

Used for:

* Workforce planning
* Retention strategy
* Organizational decision-making

---

## Summary

This data pipeline ensures:

* Clear traceability from raw data to insights
* Data quality and validation at each stage
* Scalable architecture for future enhancements
* Alignment with enterprise data governance practices
