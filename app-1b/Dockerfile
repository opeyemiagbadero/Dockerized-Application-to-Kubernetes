# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Set the ENV environment variable to 'dev' by default
ENV ENV dev

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
