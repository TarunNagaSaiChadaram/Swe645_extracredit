# Samanvitha Matta (G01252738)
# Akshaya Reddy Dundigalla (G01482843)
# Tarun Naga Sai Chadaram (G01445928)
# Dockerfile to containerize the Flask-based Student Survey API application
# This builds a lightweight Python container and runs the app on port 5001
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "/app/app.py"]
