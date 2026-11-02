from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        n1 = int(request.form.get('num1'))
        n2 = int(request.form.get('num2'))
        return f"<h1>Addition is: {n1+n2}</h1>"
    return '''
        <form method="POST">
            Num1: <input type="number" name="num1"><br>
            Num2: <input type="number" name="num2"><br>
            <input type="submit" value="Add">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)