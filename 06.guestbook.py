from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')   # http://127.0.0.1:5000/
def index():
    return render_template('index.html')


@app.route('/sign')   # http://127.0.0.1:5000/sign
def sign():           # This url will be redirected
    return render_template('sign.html')


@app.route('/process', methods=['POST'])  # http://127.0.0.1:5000/process
def process():
    # accessing posted data
    name = request.form['name']
    comment = request.form['comment']
    # request.data gives posted raw data as a string
    print 'request.method =', request.method   # POST
    print 'name:', name
    print 'comment:', comment
    return render_template('index.html', name=name, comment=comment)


if __name__ == '__main__':
    app.run(debug=True)
