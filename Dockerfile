FROM python:3.11-alpine

WORKDIR /app
COPY src/ /app/
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
