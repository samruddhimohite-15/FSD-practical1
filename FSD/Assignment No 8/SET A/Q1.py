from flask import Flask
import psycopg2
app = Flask(__name__)
def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="student1",
        user="postgres",
        password="root",
        port="5432")
@app.route('/')
def home():
    try:
        conn = connect_db()
        conn.close()
        return "Database Connected Successfully"
    except Exception as e:
        return f"Error: {e}"
@app.route('/create_table')
def table_create():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Student1 (
                student_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                course VARCHAR(100))""")
        conn.commit()
        cur.close()
        conn.close()
        return "Student2 Table Created Successfully!"
    except Exception as e:
        return f"Error: {e}"
@app.route('/insert_record')
def insert_record():
    try:
        conn = connect_db()
        cur = conn.cursor()
        students = [
            ('SAMRUDDHI', 20, 'CS'),
            ('ISHWARI', 21, ' IT'),
            ('SIDDHI', 23, 'BCS'),
            ('OMKAR', 23, 'BBA'),
            ('KUNAL', 22, 'BCS')]
        cur.executemany("""
            INSERT INTO Student1
            (name, age, course)
            VALUES (%s, %s, %s)
        """, students)
        conn.commit()
        cur.close()
        conn.close()
        return "5 Student Records Inserted Successfully!"
    except Exception as e:
        return f"Error: {e}"
if __name__ == '__main__':
    app.run(debug=True)