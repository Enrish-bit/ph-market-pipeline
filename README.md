Philippine Market Data & Cloud Pipeline

An automated data engineering pipeline that extracts live currency exchange rates for the Philippine Peso (PHP), transforms the data for consistency, and loads it into a managed cloud database.

#Tech Stack
Language:Python 3
Database: PostgreSQL (Supabase)
Infrastructure: Terraform (Infrastructure as Code)
Libraries: Psycopg2, Requests, Python-Dotenv

#System Architecture
1. Extract: Python pulls live USD/PHP market rates from a public API.
2. Transform: Raw timestamps are converted to ISO standard formats and floats are rounded.
3. Load: Python securely connects to a remote cloud database via environment variables and executes SQL optimization blocks to insert data.
4. Infrastructure: Managed using Terraform to showcase automated deployment capabilities.

#How to Run Locally
1. Clone this repository.
2. Set up a python virtual environment: `python -m venv venv` and activate it.
3. Install dependencies: `pip install -r requirements.txt` 
4. Configure your `.env` file with your `DATABASE_URL`.
5. Run the pipeline: `python db_load.py`
