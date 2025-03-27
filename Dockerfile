FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Change the exposed port from 5000 to 8080
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches with the new port
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]