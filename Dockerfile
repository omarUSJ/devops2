# Start with the official Python image
FROM python:3.9-slim-buster

# Set environment variables for the PostgreSQL driver
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN pip install django
RUN pip install djangorestframework

# Install required packages, including Django and the PostgreSQL driver
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application files to the image
COPY . /app

# Install application dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Django application runs on
EXPOSE 8080

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
