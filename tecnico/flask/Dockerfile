FROM python:3.8-buster

COPY requirements.txt /
RUN pip install -r /requirements.txt --no-cache-dir
ENV FLASK_APP=run.py
COPY . /app/
WORKDIR /app

CMD python test.py & flask run --host=0.0.0.0 --port=5000
