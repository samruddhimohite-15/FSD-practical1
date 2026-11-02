from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    product = None

    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        product = num1 * num2

    return render_template("index.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
