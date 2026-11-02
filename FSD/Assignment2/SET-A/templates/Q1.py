from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# GET request endpoint
@app.route("/api/user", methods=["GET"])
def get_user():
    user = {
        "id": 100,
        "name": "Samruddhi",
        "email": "sam@example.com",
        "course": "Python"
    }
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)