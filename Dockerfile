# Use a base Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies including curl
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    poppler-utils \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app ./app

# Set PYTHONPATH so Python knows to look in /app
ENV PYTHONPATH=/app

# Start the app
CMD ["python", "-m", "app.main"]
