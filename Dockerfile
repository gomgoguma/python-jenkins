# Use the official Python image as a base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Check if venv directory exists, if not, create it
RUN test -d venv || python -m venv venv

# Activate the virtual environment and install dependencies
RUN . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .


# Command to run the application
CMD ["python", "main.py"]