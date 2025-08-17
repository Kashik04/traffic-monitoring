# 🚦 Real-Time Traffic Monitoring System

A real-time traffic congestion and accident detection system built using **Apache Kafka, Python, and Streamlit**.  
This project simulates traffic data from multiple cities, streams it using Kafka, and visualizes live updates on a dashboard.

---

## ⚡ Features
- Real-time traffic data streaming using **Kafka Producer**
- Kafka Consumer integrated into a **Streamlit dashboard**
- Visualize traffic congestion, vehicle counts, and accident alerts
- Extensible for smart city & IoT use cases

---

## 🛠️ Tech Stack
- **Apache Kafka** (Data streaming)
- **Python** (Producer & Consumer logic)
- **Streamlit** (Dashboard visualization)

---

## 📂 Project Structure
```

project/
│-- producer.py        # Sends traffic data to Kafka
│-- dashboard.py       # Streamlit dashboard consuming Kafka data
│-- requirements.txt   # Python dependencies
│-- README.md          # Project documentation

````

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/Kashik04/traffic-monitoring.git
cd traffic-monitoring
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start Zookeeper & Kafka (in separate terminals)

```bash
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

### 4️⃣ Create Kafka topic

```bash
.\bin\windows\kafka-topics.bat --create --topic traffic-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 5️⃣ Run the Producer

```bash
python producer.py
```

### 6️⃣ Run the Dashboard

```bash
streamlit run dashboard.py
```

---

## 📸 Screenshots

(Add screenshots of your Streamlit dashboard here)

---

## 👨‍💻 Author

* **Kashik Kharwal**
  [GitHub](https://github.com/Kashik04) | [LinkedIn](#)

```

---

👉 Do you want me to also generate a **requirements.txt** file for you (so that anyone can install dependencies in one command)?
```
