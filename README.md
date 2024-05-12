# Data-Engineering-for-Business-Intelligence
## About Capstone Project from Data Engineering Bootcamp
This project entails typical Analytical Data Engineering, involving the ingestion of data from various sources and its loading into the Snowflake data warehouse. Within the warehouse, after undergoing a series of data transformation processes, we prepare the data for Business Intelligence (BI) usage. The BI tool Metabase connects to the data warehouse to generate diverse dashboards and reports.
## Part One: Data Ingestion
The first part of the project involves Data Ingestion. It entails connecting to two data sources: the Postgres database and the AWS S3 bucket. Utilizing Airbyte, establish a connection to the raw_st schema of the Postgres database on AWS RDS, and transfer all tables to the Snowflake data warehouse. In addition, leverage AWS Lambda to connect to the AWS S3 bucket and transfer the file named inventory.csv from the S3 bucket to the Snowflake data warehouse.
<p align="center">
<img src="https://github.com/NoufMr/Data-Engineering-for-Business-Intelligence/blob/main/Project%20Overview/partOne.png" width="500" height="300" />
</p>

## Part Two: Data Transformation
The next stage of the project focuses on data transformation within the Snowflake data warehouse. This involves reshaping tables from their original structure to the desired format. Throughout this phase, tasks include creating a data model, developing ETL scripts, and establishing a schedule for the data loading process.
<p align="center">
<img src="https://github.com/NoufMr/Data-Engineering-for-Business-Intelligence/blob/main/Project%20Overview/partTwo.png" width="500" height="300" />
</p>

## Part Three: Data Analysis
In the last part of this project, establish a connection between the Snowflake data warehouse and the BI tool (Metabase). This connection allows for the creation and display of dashboards and reports in Metabase, utilizing the data stored in Snowflake.

<p align="center">
<img src="https://github.com/NoufMr/Data-Engineering-for-Business-Intelligence/blob/main/Project%20Overview/partThree.png" width="500" height="300" />
</p>
