# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY emitter.py .

# Copy the service account key file into the container
COPY brando-brando-sandbox-4b309e0edfdd.json /app/brando-brando-sandbox-4b309e0edfdd.json

# Set the environment variable for Google Cloud authentication
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/brando-brando-sandbox-4b309e0edfdd.json

# Install required packages
RUN pip install requests google-cloud-monitoring

# Command to run the application
CMD ["python", "emitter.py"]