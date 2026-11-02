from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def emp():
    if request.method == 'POST':
        eid = request.form['id']
        name = request.form['name']
        dept = request.form['dept']
        return f"<h2>ID:{eid}<br>Name:{name}<br>Dept:{dept}</h2>"
    return '''
        <form method="POST">
            ID: <input name="id"><br>
            Name: <input name="name"><br>
            Dept: <input name="dept"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)