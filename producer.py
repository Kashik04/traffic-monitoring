from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

locations = ["Delhi", "Mumbai", "Bangalore", "Pune", "Hyderabad", "Chennai"]

while True:
    data = {
        "location": random.choice(locations),
        "vehicle_count": random.randint(10, 200),
        "status": random.choice(["Normal", "Congested", "Accident"])
    }
    
    producer.send("traffic-data", value=data)
    print(f"Sent: {data}")
    
    time.sleep(2)  # send data every 2 seconds
