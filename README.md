# AMD OptiCore  
AI Compiler Co-Pilot for Sustainable AI on AMD Hardware

---

## 🚀 Project Overview

**AMD OptiCore** is a prototype AI optimization assistant that analyzes PyTorch models and generates architecture-aware recommendations to improve performance-per-watt and promote Sustainable AI practices on AMD hardware.

The tool profiles model structure, benchmarks runtime performance, computes an efficiency score, evaluates optimization impact, and produces actionable tuning suggestions tailored for AMD architectures.

---

## 🧠 Problem Statement

Modern AI models are typically developed without hardware-aware optimization. This leads to:

- Increased energy consumption  
- Suboptimal inference performance  
- Inefficient CPU/GPU utilization  
- Higher operational and infrastructure costs  

There is currently no lightweight developer tool that assists in making AI workloads more efficient and AMD-ready through automated optimization insights.

---

## 💡 Solution Description

**AMD OptiCore** performs the following:

1. Loads and analyzes model architectures (CNN / Transformer)
2. Measures inference latency
3. Monitors CPU utilization
4. Computes an efficiency score
5. Assigns a sustainability grade (A / B / C)
6. Applies dynamic quantization
7. Benchmarks optimization impact
8. Generates AMD-specific optimization recommendations
9. Exports a structured optimization report

---

## 📊 Key Features

- Multi-model support (CNN + Mini Transformer)
- Inference benchmarking
- Efficiency scoring system
- Sustainability grading
- Dynamic quantization testing
- Intelligent AMD-aware tuning suggestions
- CLI-based execution
- Automatic report generation

---

## 🌱 Sustainable AI Impact

By profiling model runtime behavior and identifying inefficient configurations, AMD OptiCore:

- Encourages energy-efficient AI deployment  
- Improves performance-per-watt  
- Reduces compute waste  
- Promotes optimized execution on AMD architectures  

The system supports Sustainable AI practices by guiding developers toward more efficient model configurations.

---

## 🔧 How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run CNN Analysis

```bash
python main.py --model cnn
```

### 3️⃣ Run Transformer Analysis

```bash
python main.py --model transformer
```

After execution, an `optimization_report.txt` file will be generated containing performance metrics and AMD-specific recommendations.

---

## 📌 Future Enhancements

- ROCm GPU profiling integration  
- Large Language Model (LLM) optimization support  
- Automatic mixed-precision tuning  
- Reinforcement learning-based runtime optimization  
- Web dashboard for visualization  
- IDE / VS Code extension integration  

---

## 📍 Track

Sustainable AI / Efficient Computing

---

## 🧠 Tech Stack

- Python  
- PyTorch  
- psutil  
- torchinfo  

---

## 🎯 Vision

To build an intelligent AI optimization layer that enables developers to deploy energy-efficient, AMD-optimized AI workloads with minimal manual intervention — advancing the future of Sustainable AI infrastructure.

---

Built for AMD Sustainable AI Innovation.
