# Dockerfile - Extractor de Twitter con Python
FROM python:3.10-slim

# Instala las librerías necesarias para interactuar con Twitter
RUN pip install tweepy pandas

# Copia tus scripts de Python aquí
COPY ./twitter_extractor.py /app/

WORKDIR /app

CMD ["python", "./twitter_extractor.py"]
