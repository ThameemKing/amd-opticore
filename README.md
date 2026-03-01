# AMD OptiCore  
AI Compiler Co-Pilot for Sustainable AI on AMD Hardware

---

## 🚀 Project Overview

**AMD OptiCore** is a prototype tool that analyzes AI models and generates architecture-aware optimization suggestions designed to improve energy efficiency and performance on AMD hardware platforms.

The tool profiles PyTorch models, measures performance, computes a sustainability score, evaluates optimization impact, and provides actionable recommendations for developers.

---

## 🧠 Problem Statement

Modern AI models are often developed without hardware-aware optimization, leading to:

- Increased energy consumption  
- Suboptimal performance  
- Inefficient use of available compute  
- Higher operational costs

There is a need for a lightweight tool to assist developers in making AI workloads more efficient, especially for AMD CPUs and GPUs.

---

## 💡 Solution Description

**AMD OptiCore** performs the following:

1. Loads and analyzes model architecture (CNN / Transformer)
2. Measures inference latency and CPU utilization
3. Computes an efficiency score and sustainability grade
4. Applies dynamic quantization
5. Benchmarks results
6. Generates AMD-specific optimization suggestions
7. Outputs a structured optimization report

---

## 📊 Features

- Support for multiple model types (CNN, Mini Transformer)  
- Inference benchmarking  
- Efficiency scoring and grading  
- Dynamic quantization testing  
- Intelligent AMD-aware recommendations  
- Automatic report generation  
- CLI-based interface

---

## 🌱 Sustainable AI Impact

By profiling model performance and optimization effectiveness, **AMD OptiCore**:

- Encourages energy-efficient AI deployment  
- Improves performance-per-watt  
- Reduces compute waste  
- Promotes optimized execution on AMD architecture

Ideal for developers building AI systems with sustainability in mind.

---
## 🔧 How to Run

### Install dependencies
pip install -r requirements.txt
### Run CNN model
python main.py --model cnn
### Run Mini Transformer model
python main.py --model transformer
---

## 📌 Future Enhancements

- ROCm GPU profiling integration  
- LLM optimization and mixed-precision tuning  
- Automated accuracy-aware pruning  
- UI dashboard for visualization  
- Integration as VS Code / IDE plugin

---

## 📍 Track

**Sustainable AI / Efficient Computing**

---

## 🧠 Tech Stack

- Python  
- PyTorch  
- psutil  
- torchinfo

---

## 🎯 Vision

To build an intelligent optimization layer that enables developers to deploy energy-efficient, AMD-optimized AI workloads with minimal manual effort.

## 🔧 How to Run

### Install dependencies
