# Utilizamos Python 3.10 como imagen base
FROM python:3.10

WORKDIR /app

# Copiamos el archivo requirements.txt primero para aprovechar la cache de Docker
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos los archivos locales necesarios
COPY main.py ./
