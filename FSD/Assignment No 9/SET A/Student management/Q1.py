from flask import Flask, request
import psycopg2
app = Flask(__name__)
def connect():
    return psycopg2.connect(
        host="localhost",
        database="college_db",
        user="postgres",
        password="root",
        port="5432"
    )
con = connect()
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (id INT, name VARCHAR(50), course VARCHAR(50))")
con.commit()
cur.close()
con.close()
@app.route("/", methods=["GET", "POST"])
def home():
    msg = ""
    if request.method == "POST":
        sid = request.form["id"].strip()
        name = request.form["name"].strip()
        course = request.form["course"].strip()
        if not sid or not name or not course:
            msg = "All fields are compulsory!"
        else:
            con = connect()
            cur = con.cursor()
            cur.execute("INSERT INTO students VALUES (%s, %s, %s)", (sid, name, course))
            con.commit()
            cur.close()
            con.close()
            msg = "Student Registered Successfully!"
    return """
    <h2>Student Registration Form</h2>
    <form method="post">
    Student ID: <input name="id" required><br><br>
    Student Name: <input name="name" required><br><br>
    Course: <input name="course" required><br><br>
    <input type="submit" value="Register">
    </form>
    """ + msg
app.run(debug=True)
