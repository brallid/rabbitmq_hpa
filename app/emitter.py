import os
import time
import requests
from google.cloud import monitoring_v3

# Set up Google Cloud Monitoring client
client = monitoring_v3.MetricServiceClient()

# Google Cloud project name
project_name = "projects/brando-brando-sandbox"

# Prometheus URL
prometheus_url = 'http://10.136.0.11:9090/api/v1/query?query=rabbitmq_queue_messages'

def query_prometheus():
    response = requests.get(prometheus_url)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            # Extract the value (the second element of the "value" array)
            value = data["data"]["result"][0]["value"][1]
            return float(value)
    return None

def send_to_monitoring(value):
    # Create the time series data point
    timestamp = int(time.time())
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": timestamp}}
    )
    point = monitoring_v3.Point({"interval": interval, "value": {"double_value": value}})

    # Create the time series and send it to Google Cloud Monitoring
    series = monitoring_v3.TimeSeries()
    series.metric.type = "custom.googleapis.com/rabbitmq_queue_messages"
    series.resource.type = "gke_container"
    series.resource.labels["instance_id"] = ""
    series.resource.labels["zone"] = "europe-west4-c"
    series.resource.labels["cluster_name"] = "gke-whitson-test1"
    series.resource.labels["container_name"] = ""
    series.resource.labels["namespace_id"] = "monitoring"
    series.resource.labels["pod_id"] = ""
    series.points = [point]

    # Send the data point
    client.create_time_series(name=project_name, time_series=[series])

if __name__ == "__main__":
    while True:
        value = query_prometheus()
        if value is not None:
            send_to_monitoring(value)
        time.sleep(5)  # Run every 5 seconds