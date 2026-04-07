FROM python:3.14
WORKDIR /app
COPY *.py ./
ENTRYPOINT ["python3", "./main.py"]