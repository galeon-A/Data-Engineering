# Pharma Commercial Patient Journey Lakehouse

## Overview

An enterprise-scale healthcare and pharmaceutical data engineering platform built using PySpark, Delta Lake, and Databricks architecture principles.

This project simulates a real-world pharmaceutical patient journey ecosystem involving:

* Patient HUB programs
* Claims processing
* Specialty pharmacy shipments
* Provider master data
* Commercial analytics pipelines

The architecture follows a Medallion Lakehouse design:

* Bronze Layer → Raw ingestion
* Silver Layer → Cleansed and standardized data
* Gold Layer → Business-ready analytics (extendable)

The project demonstrates:

* Enterprise ETL engineering
* Healthcare domain modeling
* PHI masking & governance
* Delta Lake ingestion pipelines
* Data quality handling
* Scalable PySpark transformations

---

# Architecture

Raw CSV Sources
↓
Bronze Layer (Raw Delta Tables)
↓
Silver Layer (Validated & Cleaned Delta Tables)
↓
Gold Layer (Commercial Analytics & KPIs)

---

# Key Features

## Synthetic Healthcare Data Generation

Generates realistic datasets for:

* Patients
* Claims
* Providers
* Specialty pharmacy shipments

Includes:

* Missing values
* Duplicate claims
* Data inconsistencies
* Multi-domain healthcare entities

---

## Bronze Layer Ingestion

Implements:

* Schema enforcement
* Delta Lake raw ingestion
* Metadata enrichment
* Source tracking
* Audit timestamps

---

## Silver Layer Processing

Implements:

* Deduplication
* Null filtering
* Data standardization
* Date normalization
* Business rule validation
* PHI masking using SHA-256 hashing

---

## Healthcare Governance Concepts

Includes:

* Consent flag handling
* Provider master history
* Current provider identification
* Patient data masking
* Commercial lineage tracking

---

# Tech Stack

* Python
* PySpark
* Databricks
* Delta Lake
* Faker
* Pandas
* Spark SQL

---

# Dataset Domains

## Patient HUB

Contains:

* Enrollment data
* Therapy start tracking
* Support programs
* Consent flags

## Claims

Contains:

* Prescription claims
* Payer data
* Claim status
* Rejection reasons

## Provider Master

Contains:

* Provider identifiers
* Specialties
* Territory assignments

## Specialty Pharmacy

Contains:

* Shipments
* Refill tracking
* Delivery delays

---

# Data Quality Handling

Implemented validations:

* Null checks
* Duplicate detection
* Date formatting
* Standardized categorical values
* Business rule filtering

---

# PHI & Governance

The project simulates enterprise healthcare governance:

* Case manager masking
* Consent validation
* Lineage tracking
* Bronze/Silver separation

---

# Project Structure

```bash
pharma-commercial-patient-journey-lakehouse/
│
├── data_generation/
│   └── generate_pharma_data.py
│
├── bronze_layer/
│   └── bronze_ingestion.py
│
├── silver_layer/
│   └── silver_transformation.py
│
├── notebooks/
│   └── databricks_pipeline_notebook.ipynb
│
├── data/
│   ├── raw_claims.csv
│   ├── raw_patient_hub.csv
│   ├── raw_provider_master.csv
│   └── raw_specialty_pharmacy.csv
│
├── screenshots/
│   ├── bronze_tables.png
│   ├── silver_tables.png
│   └── dq_checks.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Generate Data

```bash
python generate_pharma_data.py
```

## Run Bronze Layer

```bash
python bronze_ingestion.py
```

## Run Silver Layer

```bash
python silver_transformation.py
```

---

# Enterprise Concepts Demonstrated

* Medallion Architecture
* Healthcare Data Engineering
* Delta Lake Pipelines
* Commercial Analytics Engineering
* Data Governance
* Data Quality Frameworks
* PHI Compliance Concepts
* Distributed Processing

---

# Future Enhancements

* Gold commercial KPI layer
* Power BI dashboards
* Great Expectations integration
* Unity Catalog governance
* Real-time ingestion with Kafka
* Azure Data Factory orchestration
* ML patient adherence scoring

---

