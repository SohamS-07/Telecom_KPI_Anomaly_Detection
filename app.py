import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Telecom KPI Monitoring Dashboard")
df=pd.read_csv("final_kpi_dataset.csv")
df['Timestamp']=pd.to_datetime(df['Timestamp'])


# ---------------- KPI PLOT FUNCTIONS ----------------

def daily_plot(kpi):
    df['date']=df['Timestamp'].dt.date
    rsrp_daily=df.groupby(['date','Site_ID'])[kpi].mean().reset_index()
    fig,ax=plt.subplots(figsize=(10,5))

    for site in rsrp_daily['Site_ID'].unique():
        site_data=rsrp_daily[rsrp_daily['Site_ID']==site]
        ax.plot(site_data['date'],site_data[kpi],label=site)

    ax.set_title(f"Daily {kpi} for every site")
    ax.set_xlabel("Date")
    ax.set_ylabel(kpi)
    plt.xticks(rotation=45)
    ax.legend()
    st.pyplot(fig)


def weekly_plot(kpi):
    df['week']=df['Timestamp'].dt.isocalendar().week
    rsrp_daily=df.groupby(['week','Site_ID'])[kpi].mean().reset_index()
    fig,ax=plt.subplots(figsize=(10,5))

    for site in rsrp_daily['Site_ID'].unique():
        site_data=rsrp_daily[rsrp_daily['Site_ID']==site]
        ax.plot(site_data['week'],site_data[kpi],label=site)

    ax.set_title(f"Weekly {kpi} for every site")
    ax.set_xlabel("Week")
    ax.set_ylabel(kpi)
    ax.legend()
    st.pyplot(fig)


# ---------------- KPI DASHBOARD ----------------


st.header("Daily KPI Trends")

for kpi in [
    'RSRP',
    'SINR',
    'Latency',
    'Throughput',
    'Packet_Loss',
    'Connected_Users'
]:
    daily_plot(kpi)


st.header("Weekly KPI Trends")

for kpi in [
    'RSRP',
    'SINR',
    'Latency',
    'Throughput',
    'Packet_Loss',
    'Connected_Users'
]:
    weekly_plot(kpi)


# ---------------- ANOMALIES ----------------


st.header("Detected Anomalies")


anomalies=df[
    df['anomaly']==-1
]


st.dataframe(
    anomalies[
        [
        'Timestamp',
        'Site_ID',
        'RSRP',
        'SINR',
        'Latency',
        'Root_Cause',
        'Solution'
        ]
    ]
)



# ---------------- RCA SUMMARY ----------------


st.header("Root Cause Analysis")

st.bar_chart(anomalies['Root_Cause'].value_counts())


# ---------------- QoS ----------------


st.header("Network Quality Status")

st.write(df['Network_Quality'].value_counts())
st.bar_chart(df['Network_Quality'].value_counts())


# ---------------- ALERTS ----------------


st.header("Alerts")

critical=df[df['Root_Cause']!='Nil']

if len(critical)>0:
    st.warning(f"{len(critical)} network issues detected")
else:
    st.success("All sites healthy")


# ---------------- FORECAST ----------------


st.header("Throughput Forecast")

forecast=pd.read_csv("forecast.csv")

st.line_chart(forecast['predicted_mean'])