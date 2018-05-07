from flask import Flask, request   # import requests


app = Flask(__name__)


@app.route('/')      # http://127.0.0.1:5000/
def index():
    return '<h2>Requested Method: %s </h2>' % request.method


# capable of handling both requests
@app.route('/method', methods=['GET', 'POST'])   # http://127.0.0.1:5000/method
def request_check():
    if request.method == 'POST':
        print 'Post request data:', request.data
        # I can get the posted data using request.data
        return 'You are using Post Method'
    else:
        return 'You probably using Get Method'


if __name__ == '__main__':
    app.run(debug=True)
