# Telecom KPI Anomaly Detection Dashboard

Telecom network monitoring system that analyzes network KPIs, detects anomalies, forecasts performance trends and provides root cause analysis.

<img width="973" height="726" alt="image" src="https://github.com/user-attachments/assets/784c0735-0d43-4132-9871-be241f4178ff" />

<img width="988" height="637" alt="image" src="https://github.com/user-attachments/assets/5152a88f-c8c5-46a0-b095-0e522cf4d633" />


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

<img width="927" height="587" alt="image" src="https://github.com/user-attachments/assets/f51950d0-5aeb-4eab-8229-b828696d235e" />

<img width="961" height="542" alt="image" src="https://github.com/user-attachments/assets/bcc933a0-d3e5-488f-b61d-a5e343244576" />


### Forecasting
- ARIMA model for throughput forecasting

  <img width="976" height="701" alt="image" src="https://github.com/user-attachments/assets/fdca7572-f754-49f0-aca2-ff59650da2a0" />


### QoS Classification
- KNN classifier for network quality prediction

<img width="1047" height="723" alt="image" src="https://github.com/user-attachments/assets/8ba6bd9f-8c67-4021-90bb-c6d54b7bdbb2" />

## Dashboard

Run locally:

```bash
streamlit run app.py
