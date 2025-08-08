# Use official Python image as base
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "src/server.py"]
