FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT gunicorn -w 4 -b 0.0.0.0 app:app
