# Dockerfile - Elementary Data Observability
FROM ghcr.io/elementary-data/elementary:latest

# Instala Elementary
RUN pip install elementary-data[databricks]
RUN pip install dbt-spark[PyHive]

WORKDIR /elementary