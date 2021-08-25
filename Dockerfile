# Не уверен в работосопособности
FROM python:3.8 as builder
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install -r requirements.txt

CMD ["python", "main.py", "examples.py"]
