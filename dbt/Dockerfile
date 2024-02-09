# Dockerfile - DBT con Spark y Scala para Delta Files
FROM python:3.8-slim

# Instala Java y Scala (ajusta las versiones según sea necesario)
RUN apt-get update && \
    apt-get install -y default-jdk scala

# Instala DBT
RUN pip install dbt-spark[PyHive]