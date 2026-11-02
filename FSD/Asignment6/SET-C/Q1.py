from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    emp = [
        ["Ishwari",1,"IT"],
        ["Samruddhi",2,"HR"],
        ["siddhi",3,"Sales"],
        ["Anisha",4,"Finance"]
    ]

    return "<h2>Employee Details</h2>" + "".join(
        f"Name: {e[0]}, ID: {e[1]}, Department: {e[2]}<br>"
        for e in emp
    )

app.run(debug=True)