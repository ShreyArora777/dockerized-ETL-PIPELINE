# dockerized-ETL-PIPELINE
dockerized ETL pipeline for student depression as per majors
# Student Mental Health ETL Pipeline

A Dockerized ETL pipeline that processes student mental health survey data and stores analytical results in SQLite. The pipeline extracts cleaned CSV data, aggregates depression responses by academic course, identifies the top 5 courses with the highest number of "Yes" responses, and loads results into a database.

Built with **Python 3.11, Pandas, SQLite, and Docker** to demonstrate production-grade data engineering practices including containerization, data transformation workflows, and database integration.

## Quick Start

```bash
docker build -t mental-health-etl .
docker run -v $(pwd)/data:/app/data mental-health-etl
```

## Project Structure

```
student-mental-health-etl-pipeline/
├── data/
│   ├── processed/          # Cleaned CSV input
│   └── db/                 # SQLite database output
├── etl_pipeline.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Output

Results stored in `data/db/mental_health.db` → Table: `depression_by_course`

```bash
sqlite3 data/db/mental_health.db
SELECT * FROM depression_by_course;
```

---

*Containerized for reproducibility across environments*
