from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    emp = [
        ["Ishwari",101,"IT",30000],
        ["Anisha",102,"HR",35000],
        ["Tanvi",103,"Sales",28000],
        ["Akashada",104,"Finance",40000],
        ["kiran",105,"IT",32000]
    ]

    return "<h2>Employees</h2>" + "".join(
        f"Name: {e[0]}, ID: {e[1]}, Dept: {e[2]}, Salary: ₹{e[3]}<br>"
        for e in emp
    )

app.run(debug=True)