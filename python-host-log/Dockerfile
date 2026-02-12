# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (optional, if you need to expose a service or app)
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]



# docker run -v /app/hostlogs:/app/logs pyhost

#docker run -v /home/user/logs:/app/logs my-python-app

