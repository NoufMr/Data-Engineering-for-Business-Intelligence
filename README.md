# Data-Engineering-for-Business-Intelligence
## About Capstone Project from Data Engineering Bootcamp
This project entails typical Analytical Data Engineering, involving the ingestion of data from various sources and its loading into the Snowflake data warehouse. Within the warehouse, after undergoing a series of data transformation processes, we prepare the data for Business Intelligence (BI) usage. The BI tool Metabase connects to the data warehouse to generate diverse dashboards and reports.
## Part One: Data Ingestion
The first part of the project involves Data Ingestion. It entails connecting to two data sources: the Postgres database and the AWS S3 bucket. Utilizing Airbyte, establish a connection to the raw_st schema of the Postgres database on AWS RDS, and transfer all tables to the Snowflake data warehouse. In addition, leverage AWS Lambda to connect to the AWS S3 bucket and transfer the file named inventory.csv from the S3 bucket to the Snowflake data warehouse.

