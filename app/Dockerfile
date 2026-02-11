# Use the official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --upgrade pip

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]