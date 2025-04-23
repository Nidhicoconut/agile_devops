# Dockerfile

FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .
# Dockerfile

# 👇 Make src/ visible as a module
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Run unit tests
CMD ["python", "-m", "unittest", "discover", "tests"]

COPY . /app
WORKDIR /app

RUN pip install flask

CMD ["python", "app.py"]
