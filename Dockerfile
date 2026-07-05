# TARGET TRIVY: Image versi tua ini memiliki banyak celah keamanan bawaan
FROM python:3.8-slim

WORKDIR /app
COPY src/ /app/

RUN pip install flask

EXPOSE 5000
CMD ["python", "app.py"]
