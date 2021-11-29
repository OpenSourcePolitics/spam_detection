FROM python:3.8

ENV PYTHONUNBUFFERED=1\
PORT=5000\
FLASK_ENV=production

EXPOSE $PORT

WORKDIR /spam_detection

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT --access-logfile - --error-logfile - --log-level debug wsgi:app