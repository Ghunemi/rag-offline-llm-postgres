import psycopg2
from faker import Faker
import random

fake = Faker()

# PostgreSQL connection details
DB_NAME = "rag_test"
DB_USER = ""
DB_PASS = ""
DB_HOST = "localhost"
DB_PORT = "5432"

tables = {
    "departments": """
        CREATE TABLE IF NOT EXISTS departments (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            location VARCHAR(100)
        );
    """,
    "employees": """
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            department_id INTEGER REFERENCES departments(id),
            job_title VARCHAR(100),
            hired_at DATE
        );
    """,
    "projects": """
        CREATE TABLE IF NOT EXISTS projects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            description TEXT,
            department_id INTEGER REFERENCES departments(id),
            start_date DATE,
            end_date DATE
        );
    """,
    "clients": """
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            industry VARCHAR(50),
            contact_email VARCHAR(100)
        );
    """,
    "timesheets": """
        CREATE TABLE IF NOT EXISTS timesheets (
            id SERIAL PRIMARY KEY,
            employee_id INTEGER REFERENCES employees(id),
            project_id INTEGER REFERENCES projects(id),
            hours_worked DECIMAL(5,2),
            work_date DATE
        );
    """,
    "salaries": """
        CREATE TABLE IF NOT EXISTS salaries (
            employee_id INTEGER PRIMARY KEY REFERENCES employees(id),
            monthly_salary DECIMAL(10, 2),
            currency VARCHAR(10)
        );
    """
}

def connect_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

def create_tables(conn):
    cur = conn.cursor()
    for table, ddl in tables.items():
        cur.execute(ddl)
    conn.commit()
    cur.close()

def populate_departments(conn):
    cur = conn.cursor()
    for _ in range(10):
        cur.execute(
            "INSERT INTO departments (name, location) VALUES (%s, %s);",
            (fake.company(), fake.city())
        )
    conn.commit()
    cur.close()

def populate_clients(conn):
    cur = conn.cursor()
    for _ in range(50):
        cur.execute(
            "INSERT INTO clients (name, industry, contact_email) VALUES (%s, %s, %s);",
            (fake.company(), fake.job(), fake.email())
        )
    conn.commit()
    cur.close()

def populate_employees(conn):
    cur = conn.cursor()
    for _ in range(200):
        cur.execute(
            "INSERT INTO employees (name, email, department_id, job_title, hired_at) VALUES (%s, %s, %s, %s, %s);",
            (fake.name(), fake.email(), random.randint(1, 10), fake.job(), fake.date_this_decade())
        )
    conn.commit()
    cur.close()

def populate_projects(conn):
    cur = conn.cursor()
    for _ in range(50):
        cur.execute(
            "INSERT INTO projects (name, description, department_id, start_date, end_date) VALUES (%s, %s, %s, %s, %s);",
            (fake.bs(), fake.text(), random.randint(1, 10), fake.date_this_decade(), fake.future_date())
        )
    conn.commit()
    cur.close()

def populate_timesheets(conn):
    cur = conn.cursor()
    for _ in range(1000):
        cur.execute(
            "INSERT INTO timesheets (employee_id, project_id, hours_worked, work_date) VALUES (%s, %s, %s, %s);",
            (random.randint(1, 200), random.randint(1, 50), round(random.uniform(1, 8), 2), fake.date_this_year())
        )
    conn.commit()
    cur.close()

def populate_salaries(conn):
    cur = conn.cursor()
    for eid in range(1, 201):
        cur.execute(
            "INSERT INTO salaries (employee_id, monthly_salary, currency) VALUES (%s, %s, %s);",
            (eid, round(random.uniform(3000, 10000), 2), "USD")
        )
    conn.commit()
    cur.close()

if __name__ == "__main__":
    conn = connect_db()
    create_tables(conn)
    populate_departments(conn)
    populate_clients(conn)
    populate_employees(conn)
    populate_projects(conn)
    populate_timesheets(conn)
    populate_salaries(conn)
    conn.close()
    print("Database setup and sample data generation complete.")
