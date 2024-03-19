FROM python:3.12-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080
EXPOSE 8443

CMD ["python", "app.py"]
