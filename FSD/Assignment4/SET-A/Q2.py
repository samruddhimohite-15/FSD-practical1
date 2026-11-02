from flask import Flask
app = Flask(__name__)

@app.route('/contact')
def contact():
    return "Welcome to the Contact Page"

@app.route('/services')
def services():
    return "Welcome to the Services Page"

if __name__ == '__main__':
    app.run(debug=True)