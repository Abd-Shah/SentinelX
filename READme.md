# 🛡️ SentinelX

**SentinelX** is a real-time anomaly detection system designed to monitor backend infrastructure logs and system performance metrics. The project uses machine learning to identify abnormal system behavior and simulate observability workflows commonly used in distributed systems.

---

## Features

- **Real-Time Log Ingestion**
  - Continuously generates and processes simulated backend system logs
  - Tracks service-level metrics including latency, CPU usage, memory usage, request counts, and error rates

- **ML-Based Anomaly Detection**
  - PyTorch autoencoder trained on normal system behavior
  - Reconstruction-error-based anomaly detection pipeline
  - Dynamically calculated anomaly threshold using training statistics

- **REST API Backend**
  - Built with FastAPI for real-time inference and log ingestion
  - Exposes endpoints for:
    - log ingestion
    - anomaly retrieval
    - health monitoring
    - training data export

- **Data Preprocessing Pipeline**
  - StandardScaler preprocessing for feature normalization
  - Consistent training and inference pipelines

- **Modular Architecture**
  - Structured for future integration with:
    - Kafka / Redis Streams
    - PostgreSQL
    - Docker & Kubernetes
    - Monitoring dashboards

---

## ML Pipeline

```text
Log Input
   ↓
Feature Extraction
   ↓
Feature Scaling (StandardScaler)
   ↓
PyTorch Autoencoder
   ↓
Reconstruction Error Calculation
   ↓
Threshold Comparison
   ↓
Anomaly Classification
```

---

## System Architecture

```text
Log Generator
      ↓
FastAPI Backend
      ↓
Preprocessing Pipeline
      ↓
PyTorch Inference
      ↓
Anomaly Detection
      ↓
REST API Response
```

---

## Current Status

SentinelX is currently under active development. The current implementation focuses on:
- real-time log ingestion
- ML inference pipelines
- anomaly scoring
- backend API integration

Future phases include distributed streaming, persistent storage, monitoring dashboards, container orchestration, and auto-healing workflows.
