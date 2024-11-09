# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /Origin

# Copy the 'app.py' file into the container
COPY Origin.py .

# Install the required dependencies (Flask in this case)
RUN pip install flask

# Set the command to be run when the container starts
CMD ["python", "Origin.py"]
