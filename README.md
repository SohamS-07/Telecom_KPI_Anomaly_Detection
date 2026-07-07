# Telecom KPI Anomaly Detection Dashboard

AI-powered telecom network monitoring system that analyzes network KPIs, detects anomalies, forecasts performance trends and provides root cause analysis.

## Features

- Multi-site KPI trend visualization
- Isolation Forest anomaly detection
- LSTM Autoencoder anomaly detection
- Throughput forecasting using ARIMA
- QoS/QoE prediction
- Root Cause Analysis (RCA)
- Automated network optimization suggestions
- Interactive Streamlit dashboard

## Tech Stack

- Python
- PyTorch
- Scikit-learn
- Pandas
- NumPy
- Statsmodels
- Streamlit
- Matplotlib / Seaborn

## Machine Learning Models

### Anomaly Detection
- Isolation Forest for KPI anomaly detection
- LSTM AutoEncoder for time-series anomaly detection using reconstruction error

### Forecasting
- ARIMA model for throughput forecasting

### QoS Classification
- KNN classifier for network quality prediction

## Dashboard

Run locally:

```bash
streamlit run app.py
