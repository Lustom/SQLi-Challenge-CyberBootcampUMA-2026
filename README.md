# CTF Challenge: The Intruder (SQL Injection)

This repository contains "The Intruder", a Web vulnerability challenge designed for the **Cyber Bootcamp Málaga**. 

As a mentor and challenge creator, I built this lab to teach students how to identify and exploit UNION-based SQL Injections in a SQLite environment, moving away from automated tools to focus on manual database schema reconnaissance.

## Technical Details

The core of the challenge is a Python/Flask web application querying a local SQLite database. The vulnerability exists in `src/app.py`, where user input is directly concatenated into the SQL query without proper parameterization.

To aid the learning process, the application includes a custom debug interface that renders raw `sqlite3.OperationalError` exceptions. This design choice helps students understand query arity (column matching) and internal structures (`sqlite_master`) without having to rely on tedious Blind SQLi techniques.

For the production deployment during the CTF event, the application is served via Gunicorn and containerized using Docker, with strict CPU and memory limits defined in the `docker-compose.yaml` to prevent resource exhaustion or DoS attacks from participants.

## Repository Structure

* **`challenge.md`:** The original challenge description, metadata, and hints provided to the students.
* **`solution.md`:** The step-by-step write-up containing the exploitation logic and payloads.
* **`src/`**: Contains the challenge source code:
  * `app.py`: The vulnerable Flask application.
  * `init_db.py`: Setup script that creates the schema, populates dummy data, and inserts the hidden flag.
* **`Dockerfile` & `docker-compose.yaml`**: Container deployment configurations.
* **`requirements.txt`**: Python dependencies.

## Local Deployment

You can deploy this challenge locally to test the vulnerability.

### Option 1: Using Docker (Recommended)
This is the exact environment used during the Bootcamp. Make sure you have Docker and Docker Compose installed.

```bash
docker-compose up --build -d
```
The application will be accessible at `http://localhost:8000`.

### Option 2: Manual Python Setup
If you prefer to run it without Docker, you can set it up directly using Python 3.11+.

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the SQLite database (this creates `reto.db`):
```bash
python src/init_db.py
```

3. Start the Flask server:
```bash
python src/app.py
```
