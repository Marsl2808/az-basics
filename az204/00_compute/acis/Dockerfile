FROM python:3.11.1

ADD requirements.txt /app/requirements.txt
ADD app.py /app/app.py

RUN ["pip", "install", "-r", "/app/requirements.txt"]

EXPOSE 5000

ENTRYPOINT [ "python", "/app/app.py"]
