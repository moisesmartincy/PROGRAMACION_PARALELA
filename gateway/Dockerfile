FROM python:3.11-slim
WORKDIR /app
RUN pip install flask requests flask-cors
COPY app.py .
CMD ["python", "app.py"]
