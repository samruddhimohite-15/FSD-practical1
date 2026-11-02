from flask import Flask, request, render_template, redirect
import psycopg2
app = Flask(__name__)
# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname="college_db",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
# Create Student table
def create_table():
    con = db_connect()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Student "
                "(Student_ID SERIAL PRIMARY KEY, Name VARCHAR(100), Course VARCHAR(100))")
    con.commit()
    cur.close()
    con.close()
# Add Student
@app.route("/", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["Name"].strip()
        course = request.form["Course"].strip()
        if name and course:
            con = db_connect()
            cur = con.cursor()
            cur.execute("INSERT INTO Student (Name, Course) VALUES (%s, %s)", (name, course))
            con.commit()
            cur.close()
            con.close()
            return redirect("/display")
    return render_template("add.html")
# Display Students
@app.route("/display")
def display_students():
    con = db_connect()
    cur = con.cursor()
    cur.execute('SELECT * FROM "student" ORDER BY "student_id"')
    students = cur.fetchall()
    cur.close()
    con.close()
    return render_template("display.html", students=students)
# Update Student
@app.route("/update", methods=["GET", "POST"])
def update_student():
    if request.method == "POST":
        sid = request.form["Student_ID"]
        name = request.form["Name"].strip()
        course = request.form["Course"].strip()

        if name and course:
            con = db_connect()
            cur = con.cursor()
            cur.execute('UPDATE "student" SET "name"=%s, "course"=%s WHERE "student_id"=%s',
                         (name, course, sid))
            con.commit()
            cur.close()
            con.close()
            return redirect("/display")
    return render_template("update.html")
# Delete Student
@app.route("/delete", methods=["GET", "POST"])
def delete_student():
    if request.method == "POST":
        sid = request.form["Student_ID"]
        con = db_connect()
        cur = con.cursor()
        cur.execute('DELETE FROM "student" WHERE "student_id"=%s', (sid,))
        con.commit()
        cur.close()
        con.close()
        return redirect("/display")
    return render_template("delete.html")
if __name__ == "__main__":
    create_table()
    app.run(debug=True)
