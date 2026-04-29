import requests
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import StandardScaler
import numpy as np

API_URL = "http://127.0.0.1:8000/export/logs"


class Autoencoder(nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 8),
            nn.ReLU(),
            nn.Linear(8, 3),
            nn.ReLU()
        )

        self.decoder = nn.Sequential(
            nn.Linear(3, 8),
            nn.ReLU(),
            nn.Linear(8, input_dim)
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded


def fetch_logs():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def prepare_data(logs):
    normal_logs = [log for log in logs if log["is_anomaly"] is False]

    features = [
        [
            log["latency_ms"],
            log["error_rate"],
            log["cpu_usage"],
            log["memory_usage"],
            log["request_count"],
        ]
        for log in normal_logs
    ]

    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    return torch.tensor(scaled, dtype=torch.float32), scaler


def train_model(data):
    model = Autoencoder(input_dim=5)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(100):
        output = model(data)
        loss = criterion(output, data)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

    return model


if __name__ == "__main__":
    logs = fetch_logs()

    if len(logs) < 50:
        print("Collect more logs first. Run generator for a few minutes.")
        exit()

    data, scaler = prepare_data(logs)
    model = train_model(data)

    torch.save(model.state_dict(), "ml/models/autoencoder.pth")
    print("Model saved to ml/models/autoencoder.pth")