from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="SentinelX API")

logs_db = []
anomalies_db = []


class LogEvent(BaseModel):
    timestamp: str
    service_name: str
    endpoint: str
    latency_ms: int
    error_rate: float
    cpu_usage: float
    memory_usage: float
    request_count: int
    anomaly_type: str
    is_anomaly: bool


def detect_anomaly(log: LogEvent) -> bool:
    return (
        log.latency_ms > 1000
        or log.error_rate > 0.10
        or log.cpu_usage > 85
        or log.memory_usage > 85
        or log.request_count > 1000
    )

@app.get("/export/logs")
def export_logs():
    return logs_db

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/logs")
def create_log(log: LogEvent):
    detected = detect_anomaly(log)

    log_record = log.model_dump()
    log_record["detected_anomaly"] = detected
    log_record["received_at"] = datetime.utcnow().isoformat()

    logs_db.append(log_record)

    if detected:
        anomalies_db.append(log_record)

    return {
        "message": "log received",
        "detected_anomaly": detected,
        "total_logs": len(logs_db),
        "total_anomalies": len(anomalies_db),
    }


@app.get("/logs")
def get_logs():
    return logs_db[-20:]


@app.get("/anomalies")
def get_anomalies():
    return anomalies_db[-20:]