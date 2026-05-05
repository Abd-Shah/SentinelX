# 🛡️ SentinelX

**SentinelX** is a real-time anomaly detection system designed to monitor system logs and performance metrics across distributed services. It leverages machine learning to detect unusual patterns and potential system failures before they escalate.

---

## Features

- **Real-Time Monitoring**
  - Processes high-volume system logs and metrics
  - Handles 10K+ events per minute (simulated)

- **ML-Based Anomaly Detection**
  - Autoencoder (PyTorch) for reconstruction-based detection
  - Isolation Forest for statistical anomaly detection
  - Hybrid detection pipeline for improved accuracy

- **Streaming Pipeline**
  - Log → Scaler → Model → Reconstruction Error → Anomaly Decision
  - Designed for scalable, distributed environments

- **System Metrics Tracking**
  - Latency, error rate, CPU usage, memory usage
  - Request volume and service-level monitoring

-  **Scalable Architecture**
  - Backend built with FastAPI
  - Designed for containerized deployment (Docker, Kubernetes ready)

---

## Tech Stack

- **Backend:** FastAPI (Python)  
- **Machine Learning:** PyTorch, Scikit-learn  
- **Data Processing:** NumPy, Pandas  
- **Model Storage:** joblib  
- **API Testing:** Postman  
- **Dev Environment:** Python 3.12, Anaconda  

---

## System Architecture

```text
Log Input → Preprocessing → Feature Scaling → ML Model → Reconstruction Error → Anomaly Classification
