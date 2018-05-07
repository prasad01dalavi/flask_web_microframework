from flask import Flask, render_template


app = Flask(__name__)


# For both the urls, same method (userLogin) will be called
@app.route('/')         # http://127.0.0.1:5000/
@app.route('/<name>')   # http://127.0.0.1:5000/prasad
def userLogin(name=None):
    return render_template('user.html', context=name)


if __name__ == '__main__':
    app.run(debug=True)
