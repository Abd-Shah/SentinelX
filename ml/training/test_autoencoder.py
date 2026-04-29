import torch
import torch.nn as nn
import numpy as np


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


def predict_anomaly(model, log_features, threshold=1.5):
    x = torch.tensor(log_features, dtype=torch.float32)

    with torch.no_grad():
        reconstructed = model(x)
        error = torch.mean((x - reconstructed) ** 2).item()

    return error, error > threshold


if __name__ == "__main__":
    model = Autoencoder(input_dim=5)
    model.load_state_dict(torch.load("ml/models/autoencoder.pth"))
    model.eval()

    normal_log = [120, 0.01, 45, 60, 200]
    anomaly_log = [3500, 0.45, 95, 92, 5000]

    normal_error, normal_is_anomaly = predict_anomaly(model, normal_log)
    anomaly_error, anomaly_is_anomaly = predict_anomaly(model, anomaly_log)

    print("Normal Log:")
    print("Error:", normal_error)
    print("Anomaly:", normal_is_anomaly)

    print("\nAnomaly Log:")
    print("Error:", anomaly_error)
    print("Anomaly:", anomaly_is_anomaly)