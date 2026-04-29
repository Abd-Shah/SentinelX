import requests
import random
import time
from datetime import datetime, timezone

SERVICES = [
    "auth-service",
    "payment-service",
    "search-service",
    "user-service",
    "notification-service",
]

ENDPOINTS = {
    "auth-service": ["/api/login", "/api/logout", "/api/register"],
    "payment-service": ["/api/payments", "/api/refunds", "/api/invoices"],
    "search-service": ["/api/search", "/api/recommendations"],
    "user-service": ["/api/users", "/api/profile"],
    "notification-service": ["/api/email", "/api/sms"],
}


def generate_normal_log():
    service = random.choice(SERVICES)
    endpoint = random.choice(ENDPOINTS[service])

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service_name": service,
        "endpoint": endpoint,
        "latency_ms": random.randint(80, 350),
        "error_rate": round(random.uniform(0.0, 0.04), 4),
        "cpu_usage": round(random.uniform(20, 70), 2),
        "memory_usage": round(random.uniform(30, 75), 2),
        "request_count": random.randint(50, 400),
        "anomaly_type": "none",
        "is_anomaly": False,
    }


def inject_anomaly(log):
    anomaly_type = random.choice([
        "latency_spike",
        "high_error_rate",
        "cpu_overload",
        "memory_leak",
        "traffic_spike",
    ])

    log["anomaly_type"] = anomaly_type
    log["is_anomaly"] = True

    if anomaly_type == "latency_spike":
        log["latency_ms"] = random.randint(1200, 5000)

    elif anomaly_type == "high_error_rate":
        log["error_rate"] = round(random.uniform(0.15, 0.60), 4)

    elif anomaly_type == "cpu_overload":
        log["cpu_usage"] = round(random.uniform(85, 99), 2)

    elif anomaly_type == "memory_leak":
        log["memory_usage"] = round(random.uniform(85, 99), 2)

    elif anomaly_type == "traffic_spike":
        log["request_count"] = random.randint(1500, 7000)
        log["latency_ms"] = random.randint(600, 2500)

    return log


def generate_log(anomaly_probability=0.08):
    log = generate_normal_log()

    if random.random() < anomaly_probability:
        log = inject_anomaly(log)

    return log


if __name__ == "__main__":
    API_URL = "http://127.0.0.1:8000/logs"

    if __name__ == "__main__":
        while True:
            log = generate_log()

            try:
                response = requests.post(API_URL, json=log)
                print("Sent:", log)
                print("Response:", response.json())
            except Exception as e:
                print("Error sending log:", e)

            time.sleep(1)