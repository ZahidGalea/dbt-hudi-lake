# Dockerfile - Elementary Data Observability
FROM python:3.10-slim

# Instala Elementary
RUN pip install elementary-data

# Copia los archivos de configuración de Elementary si es necesario
COPY ./elementary_config.yml /root/.elementary/

WORKDIR /elementary

CMD ["elementary", "check"]
