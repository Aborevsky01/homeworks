FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY join_script.py .
RUN chmod +x join_script.py && mkdir -p /data/input /data/output

ENTRYPOINT ["python", "join_script.py"]
