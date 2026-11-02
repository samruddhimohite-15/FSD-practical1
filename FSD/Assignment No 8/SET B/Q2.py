from flask import Flask
import psycopg2

app = Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname = 'Books',
        user = 'postgres',
        password = 'root',
        host = 'localhost',
        port = '5432'
    )

@app.route('/create_table')
def create_table():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Books(
                bid SERIAL PRIMARY KEY,
                title VARCHAR(100),
                author VARCHAR(100),
                price INT
            );
        """)

        conn.commit()
        cur.close()
        conn.close()
        return "Books Table Created Successfully!"

    except Exception as e:
        return f"Error : {e}"

@app.route('/insert_records')
def insert_books():
    try:
        conn = db_connect()
        cur = conn.cursor()

        books = [
            ("Python", "samruddhi", 340),
            ("FSD", "samruddhi", 450),
            ("cloud", "siddhi", 230),
            ("OOAD", "KUNAL", 200),
            ("Data Science", "ISHWARI", 600)
        ]

        cur.executemany("INSERT INTO Books (title, author, price) VALUES(%s,%s,%s);", books)
        conn.commit()
        cur.close()
        conn.close()
        return "Records inserted successfully in Books table!"

    except Exception as e:
        return f"Error : {e}"

@app.route('/display_books')
def display_books():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("SELECT title, author, price FROM Books;")
        books = cur.fetchall()
        cur.close()
        conn.close()

        books_list = ""
        for book in books:
            books_list += f"Title: {book[0]}, Author: {book[1]}, Price: {book[2]}<br>"

        return books_list
    except Exception as e:
        return f"Error : {e}"

if __name__ == '__main__':
    app.run(debug=True)