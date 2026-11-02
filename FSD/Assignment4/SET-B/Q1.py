from flask import Flask
app = Flask(__name__)

@app.route('/student/<student_name>')
def student(student_name):
    return f"Welcome, {student_name}! This is the Student Page."

if __name__ == '__main__':
    app.run(debug=True)