import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd

st.set_page_config(page_title="Traffic Monitoring Dashboard", layout="wide")

st.title("🚦 Real-Time Traffic Congestion & Accident Detection")

# Kafka Consumer
consumer = KafkaConsumer(
    'traffic-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id="dashboard-group"
)

st.subheader("📊 Live Traffic Data")

placeholder = st.empty()

data = []

# Continuous stream
for message in consumer:
    record = message.value
    data.append(record)

    # Keep only last 20 records for display
    df = pd.DataFrame(data[-20:])

    with placeholder.container():
        st.dataframe(df, use_container_width=True)

        # Simple stats
        accidents = df[df['status'] == 'Accident'].shape[0]
        congested = df[df['status'] == 'Congested'].shape[0]
        st.metric("🚨 Accidents", accidents)
        st.metric("🚗 Congested Areas", congested)
