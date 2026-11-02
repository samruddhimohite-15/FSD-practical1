from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    students = ["Ishwari","Samruddhi","Siddhi","Purva","Bhagyashri"]
    return "<h2>Students</h2><ul>" + "".join(f"<li>{x}</li>" for x in students) + "</ul>"

app.run(debug=True)