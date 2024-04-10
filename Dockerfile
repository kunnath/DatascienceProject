# Use Python base image for ARM architecture (compatible with Mac M1)
FROM python:3.9.6-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
COPY house_data.csv /app/
RUN pip install --no-cache-dir -r requirements.txt


# Copy the Python script and HTML file into the container
#COPY predictionhome.py /app/
#COPY map.py /app/
COPY Jinja2.py /app/
COPY index.html /app/
COPY house_data.csv /app/

# Expose port 8009 (or any other port you want to use for the web server)
EXPOSE 8009

# Command to run the Python script (starts a simple web server)
CMD ["python", "-m", "http.server", "8009"]
