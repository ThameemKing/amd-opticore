import torch
import torch.nn as nn
import time
import psutil
import argparse
from torchinfo import summary

# -----------------------------
# Models
# -----------------------------

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.conv2 = nn.Conv2d(16, 32, 3)
        self.fc1 = nn.Linear(32 * 6 * 6, 128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x


class MiniTransformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Linear(32, 64)
        encoder_layer = nn.TransformerEncoderLayer(d_model=64, nhead=4)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=2)
        self.fc = nn.Linear(64, 10)

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = self.fc(x.mean(dim=1))
        return x


# -----------------------------
# Benchmarking
# -----------------------------

def benchmark(model, input_tensor, runs=200):
    model.eval()
    start = time.time()
    cpu_start = psutil.cpu_percent(interval=None)

    with torch.no_grad():
        for _ in range(runs):
            _ = model(input_tensor)

    cpu_end = psutil.cpu_percent(interval=None)
    end = time.time()

    latency = end - start
    cpu_usage = (cpu_start + cpu_end) / 2
    return latency, cpu_usage


# -----------------------------
# Efficiency Score
# -----------------------------

def calculate_efficiency(latency, cpu_usage, params):
    score = (1 / latency) * (100 - cpu_usage) / (params / 1e5)
    return score


def grade_efficiency(score):
    if score > 50:
        return "A (Highly Efficient)"
    elif score > 20:
        return "B (Moderately Efficient)"
    else:
        return "C (Needs Optimization)"


# -----------------------------
# Suggestions
# -----------------------------

def generate_suggestions(improvement, cpu_usage, grade):
    suggestions = []

    if improvement < 0:
        suggestions.append("Dynamic quantization not effective → Consider FP16 mixed precision for AMD GPUs.")

    if cpu_usage > 70:
        suggestions.append("High CPU usage → Optimize thread distribution for AMD Ryzen architecture.")

    if grade.startswith("C"):
        suggestions.append("Low efficiency grade → Apply pruning or architecture simplification.")

    suggestions.append("Enable ROCm stack for AMD GPU acceleration.")
    suggestions.append("Tune batch size for Infinity Fabric bandwidth efficiency.")

    return suggestions


# -----------------------------
# Main
# -----------------------------

def main():

    parser = argparse.ArgumentParser(description="AMD AI Compiler Co-Pilot")
    parser.add_argument("--model", type=str, default="cnn", help="cnn or transformer")
    args = parser.parse_args()

    print("\n🚀 AMD AI Compiler Co-Pilot\n")

    if args.model == "cnn":
        model = SimpleCNN()
        input_tensor = torch.randn(1, 3, 32, 32)
    else:
        model = MiniTransformer()
        input_tensor = torch.randn(10, 5, 32)

    total_params = sum(p.numel() for p in model.parameters())

    print("🔍 Model Summary:")
    summary(model)

    original_latency, cpu_usage = benchmark(model, input_tensor)
    original_score = calculate_efficiency(original_latency, cpu_usage, total_params)
    original_grade = grade_efficiency(original_score)

    print(f"\nOriginal Latency: {original_latency:.4f}s")
    print(f"CPU Usage: {cpu_usage:.2f}%")
    print(f"Efficiency Score: {original_score:.2f}")
    print(f"Efficiency Grade: {original_grade}")

    quantized_model = torch.quantization.quantize_dynamic(
        model, {nn.Linear}, dtype=torch.qint8
    )

    quant_latency, _ = benchmark(quantized_model, input_tensor)
    improvement = ((original_latency - quant_latency) / original_latency) * 100

    print(f"\nAfter Quantization Latency: {quant_latency:.4f}s")
    print(f"Performance Change: {improvement:.2f}%")

    suggestions = generate_suggestions(improvement, cpu_usage, original_grade)

    print("\n🧠 AMD Optimization Suggestions:")
    for s in suggestions:
        print("-", s)

    with open("optimization_report.txt", "w", encoding="utf-8") as f:
        f.write(f"Model: {args.model}\n")
        f.write(f"Latency: {original_latency:.4f}\n")
        f.write(f"CPU Usage: {cpu_usage:.2f}\n")
        f.write(f"Efficiency Grade: {original_grade}\n")
        f.write(f"Performance Change: {improvement:.2f}%\n\n")
        f.write("Suggestions:\n")
        for s in suggestions:
            f.write(f"- {s}\n")

    print("\n📄 Report generated: optimization_report.txt")


if __name__ == "__main__":
    main()