from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    s = {"Name":"Ishwari","Roll":36,"Course":"Bsc.IT","Marks":70}
    return f"""
    <h2>Student Information</h2>
    Name: {s['Name']}<br>
    Roll No: {s['Roll']}<br>
    Course: {s['Course']}<br>
    Marks: {s['Marks']}
    """

app.run(debug=True)