from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        comment = request.form['comment']
        return f"<h1>Thanks {name}</h1><p>Rating:{rating}<br>Comment:{comment}</p>"
    return '''
        <form method="POST">
            Name: <input name="name"><br>
            Rating: <input type="number" name="rating" min="1" max="5"><br>
            Comments: <textarea name="comment"></textarea><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)