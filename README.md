# Delta / DBT / Elementary

--- 

![Status](https://img.shields.io/badge/%20Status-WIP-orange)

---

### Checkmarks

* [x] Base docker compose configuration
* [x] PostgreSQL with Hive metastore configuration 
* [x] Apache Hudi with Spark Thrift Server configuration 
* [x] DBT with connection to Spark Thrift Server and test model 
* [ ] Elementary integration 
* [ ] Run Book documentation

## Introduction
This document outlines the Proof of Concept (PoC) implemented to demonstrate the integration and functioning of Apache Hudi, DBT (Data Build Tool), and Elementary within a data processing environment. The aim is to assess the efficiency, scalability, and data quality management achievable by leveraging these technologies together.

## Technology Description
* **DBT (Data Build Tool)**: A data transformation tool that enables data teams to model and transform data in their data warehouse. It uses SQL for transformations and integrates with version control systems to maintain a change history and facilitate collaboration.

* **Apache Hudi**: A storage layer that brings ACID transactions, scalability, and reliability to data storage systems in a data lake format. It supports concurrent read and write operations, ensuring data integrity.

* **Spark Thrift Server**: Provides a JDBC/ODBC interface that allows external applications to connect to Spark SQL using standard protocols. It facilitates interoperability and access to data processed by Spark.

* **Hive Metastore in PostgreSQL**: The Hive Metastore stores table and partition metadata in a relational data store, in this case, PostgreSQL. This enables efficient and scalable management of metadata, crucial for complex data operations.

## How to replicate.

1. Clone this repo.
2. Build the images.

```bash
docker-compose build --no-cache
```

3. Run the containers.

```bash
docker-compose up
```
