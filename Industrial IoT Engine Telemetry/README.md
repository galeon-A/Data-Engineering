# Industrial IoT Engine Telemetry Data Quality Platform

## Overview

An enterprise-scale Industrial IoT telemetry and data quality platform built using PySpark, Delta Lake, and Databricks.

This project simulates real-world engine telemetry pipelines commonly used in:

* Manufacturing
* Heavy equipment monitoring
* Fleet management
* Industrial IoT analytics
* Predictive maintenance systems

The architecture implements a Medallion Lakehouse design with integrated data quality validation frameworks.

---

# Architecture

Telemetry Generators
↓
CSV + JSON Raw Sources
↓
Bronze Layer (Raw Delta)
↓
Silver Layer (Validated + Cleansed)
↓
Gold Layer (DQ Metrics & KPI Tables)
↓
Databricks SQL Dashboard

---

# Key Features

## Synthetic IoT Telemetry Generation

Generates:

* Engine RPM data
* Oil pressure telemetry
* Coolant temperature metrics
* Exhaust NOx emissions
* Fuel consumption metrics
* GPS coordinates

Includes intentionally injected:

* Missing values
* Duplicate records
* Outliers
* Multi-format ingestion issues

---

## Multi-Source Data Ingestion

Supports:

* CSV ingestion
* Nested JSON ingestion
* Schema standardization
* Source tracking
* Delta Lake storage

---

## Data Quality Framework

Implements enterprise-grade DQ validations:

* Null checks
* Duplicate detection
* Sensor threshold validation
* Outlier detection
* Pass/fail scoring

---

## Silver Layer Cleansing

Performs:

* Timestamp standardization
* Duplicate elimination
* Sensor validation
* Record quality tagging
* Data normalization

---

## Gold Layer Analytics

Produces:

* Pass/fail metrics
* Data quality percentages
* Sensor failure tracking
* Source-level DQ reporting

---

# Tech Stack

* Python
* PySpark
* Delta Lake
* Databricks
* Pandas
* Faker
* Kafka-ready architecture
* Azure integration libraries

---

# Data Quality Rules

## RPM Validation

Valid range:

* 500 to 3000 RPM

## Oil Pressure Validation

Valid range:

* 20 to 120 PSI

## Coolant Temperature Validation

Valid range:

* 70°C to 120°C

## NOx Validation

Valid range:

* Greater than 0
* Less than or equal to 500 PPM

---

# Project Structure

```bash
industrial-iot-engine-telemetry-platform/
│
├── data_generation/
│   └── generate_sensor_data.py
│
├── bronze_layer/
│   └── bronze_ingestion.py
│
├── silver_gold_layer/
│   └── silver_gold_dq_pipeline.py
│
├── raw_data/
│   ├── telemetry_csv/
│   └── telemetry_json/
│
├── dashboards/
│   └── databricks_sql_dashboard.png
│
├── screenshots/
│   ├── bronze_summary.png
│   ├── dq_metrics.png
│   └── telemetry_dashboard.png
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

## Generate Telemetry Data

```bash
python generate_sensor_data.py
```

## Run Bronze Layer

```bash
python bronze_ingestion.py
```

## Run Silver + Gold DQ Pipeline

```bash
python silver_gold_dq_pipeline.py
```

---

# Enterprise Concepts Demonstrated

* Industrial IoT Data Engineering
* Medallion Architecture
* Delta Lake Processing
* Enterprise Data Quality Frameworks
* Sensor Validation Systems
* Multi-format Ingestion
* Distributed Data Pipelines
* Real-time Architecture Foundations

---

# Future Enhancements

* Kafka real-time streaming
* Predictive maintenance ML models
* Azure Event Hub ingestion
* Power BI dashboards
* Great Expectations integration
* Unity Catalog governance
* IoT anomaly detection

---
