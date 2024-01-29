# Dockerfile - Elementary Data Observability
FROM ghcr.io/elementary-data/elementary:latest

# Instala Elementary
RUN pip install elementary-data[databricks]
RUN pip install dbt-spark[session]

# Copia los archivos de configuración de Elementary si es necesario
# COPY ./elementary_config.yml /root/.elementary/

WORKDIR /elementary