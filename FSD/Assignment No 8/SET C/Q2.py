from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def manage_vehicles():
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
            CREATE TABLE IF NOT EXISTS Vehicle (
                id INT PRIMARY KEY,
                name VARCHAR(50),
                brand VARCHAR(50),
                price NUMERIC(12, 2)
            )
        """)

        vehicles = [
            (1, "Swift", "Maruti", 600000),
            (2, "City", "Honda", 1200000),
            (3, "Nexon", "Tata", 900000),
            (4, "Creta", "Hyundai", 1100000),
            (5, "Thar", "Mahindra", 1500000)
        ]

        cur.executemany("""
            INSERT INTO Vehicle (id, name, brand, price)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, vehicles)

        # Update price of Vehicle ID 1
        cur.execute("""
            UPDATE Vehicle
            SET price = %s
            WHERE id = %s
        """, (650000, 1))

        # Delete Vehicle ID 5
        cur.execute(
            "DELETE FROM Vehicle WHERE id = %s",
            (5,)
        )

        conn.commit()

        cur.execute("""
            SELECT id, name, brand, price
            FROM Vehicle ORDER BY id
        """)

        rows = cur.fetchall()

        html = """
            <h2>Final Vehicle Records</h2>
            <table border="1" cellpadding="8">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Brand</th>
                <th>Price</th>
            </tr>
        """

        for vehicle in rows:
            html += f"""
                <tr>
                    <td>{vehicle[0]}</td>
                    <td>{vehicle[1]}</td>
                    <td>{vehicle[2]}</td>
                    <td>{vehicle[3]}</td>
                </tr>
            """

        html += "</table>"

        cur.close()
        conn.close()
        return html

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)