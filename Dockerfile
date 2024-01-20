# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy requirements.txt file into the container
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Expose port 8000 in the container
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]