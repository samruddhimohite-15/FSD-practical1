from flask import Flask,request,render_template
import psycopg2

app = Flask(__name__)

def get_connect():
    conn=psycopg2.connect(
        dbname="employee",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

def create_table():
    conn=get_connect()
    cur=conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXIST employee(
        Emp_ID SERIAL PRIMARY KEY,
        NAME VARCHAR(100),
        DEPARTMENT VARCHAR(100)
        )
""")
    conn.commit()
    cur.close()
    conn.close()


@app.route("/employee", methods=["GET", "POST"])

def employee():
    conn=get_connect()
    cur=get_cursor()

    if request.method=="POST":
        name=request.form.get("name")
        department=request.form.get("department")
        cur.execute(

                "INSERT INTO Employee(Name,Department) VALUES (%s, %s)", (name, department)
            )

            conn.commit()
        
        cur.execute("SELECT*FROM Employee ORDER BY Emp_ID")

if _name == 'main_':
    create_table()
    app.run(debug=True)