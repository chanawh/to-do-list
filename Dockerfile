# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install application dependencies
RUN pip install -r requirements.txt

# Set the default command to run the tests
CMD ["python", "-m", "unittest", "discover"]

