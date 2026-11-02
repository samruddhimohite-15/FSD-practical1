from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        if user == "admin":
            return "<h1>Login Successful!</h1>"
        else:
            return "<h1>Invalid Username!</h1>"
    return '''
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)