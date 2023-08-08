# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory to /stack
WORKDIR /stack

# Copy the current directory contents into the container at /stack
COPY . /stack

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run your service (replace "app.py" with your service entry point)
CMD ["python", "app.py"]