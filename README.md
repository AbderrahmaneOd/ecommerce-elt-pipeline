# E-Commerce ELT Pipeline

## 📄 Description
This project implements an ELT (Extract, Load, Transform) data pipeline for analyzing e-commerce transaction data from a UK-based online retailer. It uses a modern, containerized tech stack to enable efficient data ingestion, transformation, warehousing, and visualization. The pipeline facilitates actionable business insights through streamlined processes.

---

## 🚀 Features
- **Data Extraction**: Ingest raw e-commerce transaction data from CSV files.
- **Data Transformation**: Clean, aggregate, and enrich data using Apache Spark.
- **Data Warehousing**: Store processed data in Hive tables for querying.
- **Workflow Orchestration**: Manage pipeline tasks using Apache Airflow.
- **Scalability**: Leverage Hadoop for distributed data storage and processing.
- **Containerized Deployment**: Use Docker to run the entire stack seamlessly.

---

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|--- |--- | --- |
| Hadoop | Distributed storage (HDFS) | 3.2.1 |
| Python | Programming and scripting  | 3.9 |
| Spark | Distributed data processing | 3.2.2
| Airflow | Workflow orchestration | 2.3.3 |
| Zeppelin | Web-based notebook for exploration | 0.10.1 |
| Hive | Data warehousing solution | 2.3.2 |
| Postgres | Hive metastore backend | 15.1 |

---

## 📂 Project Structure

```
.
├── dags/                        # Airflow DAGs for pipeline orchestration
├── configs/                     # Configuration files for Spark, Hive, and Hadoop
├── spark-scripts/               # Scripts for data ingestion and transformation
├── data/                        # Folder to store raw data
├── streamlit/                   # Streamlit app for data visualization
└── docker-compose.yml           # Docker Compose file to orchestrate services

```

---

## ⚙️ Setup and Usage

### Prerequisites
- Docker and Docker Compose installed
- Basic understanding of ELT pipelines and the tech stack

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/AbderrahmaneOd/spark-hive-airflow-ecommerce-pipeline.git
   cd spark-hive-airflow-ecommerce-pipeline
   ```

2. **Launch Services**
   ```bash
   docker compose up -d
   ```


3. **Access Services**
  
| Service             | URL                        |
|---------------------|----------------------------|
| HDFS Namenode       | http://localhost:9870      |
| YARN ResourceManager| http://localhost:8088      |
| Spark Master        | http://localhost:8080      |
| Spark Worker        | http://localhost:8081      |
| Zeppelin            | http://localhost:8082      |
| Airflow             | http://localhost:3000      |

##### Airflow creds
 - username  : admin
 - password  : admin
 - firstname : admin
 - lastname  : admin
 - role      : Admin
 - email     : admin@gmail.com

4. **Run the Pipeline**

You can monitor progress in the Airflow UI.

---

## 📈 Data Visualization
The project includes a Streamlit app for intuitive visualization of business metrics, such as total revenue, top-selling products, and customer trends.
