from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def insert_students():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="college_db",
            user="postgres",
            password="root",
            port="5432"
        )

        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                id INT PRIMARY KEY,
                name VARCHAR(50),
                age INT,
                course VARCHAR(50)
            )
        """)

        students = [                    
            (1, "Kunal", 20, "BSC.IT"),
            (2, "Vedant", 21, "BSC"),
            (3, "Datta", 22, "BCA"),
            (4, "Omkar", 20, "BCom"),
            (5, "Siddesh", 21, "BSC")
        ]

        cur.executemany("""
            INSERT INTO Student (id, name, age, course)
            VALUES (%s, %s,%s, %s)
            ON CONFLICT (id) DO NOTHING
        """, students)

        conn.commit()
        cur.close()
        conn.close()

        return "5 Student Records Inserted Successfully"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)