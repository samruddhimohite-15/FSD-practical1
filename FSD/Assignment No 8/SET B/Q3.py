from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def insert_patients():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="college",
            user="postgres",
            password="your_password",
            port="5432"
        )

        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Patient (
                id INT PRIMARY KEY,
                name VARCHAR(50),
                age INT
            )
        """)

        patients = [
            (101, "Amit", 35),
            (102, "Priya", 28),
            (103, "Rahul", 42),
            (104, "Sneha", 30),
            (105, "Neha", 25)
        ]

        cur.executemany("""
            INSERT INTO Patient (id, name, age)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, patients)

        conn.commit()
        cur.close()
        conn.close()

        return "5 Patient Records Inserted Successfully"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)