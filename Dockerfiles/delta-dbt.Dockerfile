# Dockerfile - DBT con Spark y Scala para Delta Files
FROM python:3.8-slim

# Instala Java y Scala (ajusta las versiones según sea necesario)
RUN apt-get update && \
    apt-get install -y default-jdk scala

# Instala DBT
RUN pip install dbt-spark[PyHive]

# Configura las variables de entorno para Java y Spark
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME /usr/local/spark

# Copia tu archivo de configuración DBT aquí si es necesario
# COPY ./dbt_project.yml /root/.dbt/

WORKDIR /dbt

CMD ["dbt", "run"]
