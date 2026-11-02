from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    result = ""
    if request.method == "POST":
        name = request.form["name"]
        m = [int(request.form["m1"]), int(request.form["m2"]), int(request.form["m3"])]
        result = f"Name: {name}<br>Total: {sum(m)}<br>Average: {sum(m)/3}"

    return f"""
    <h2>Student Details</h2>
    <form method="post">
    Name: <input name="name"><br><br>
    Marks 1: <input name="m1"><br><br>
    Marks 2: <input name="m2"><br><br>
    Marks 3: <input name="m3"><br><br>
    <input type="submit" value="Calculate">
    </form><h3>{result}</h3>
    """

app.run(debug=True)