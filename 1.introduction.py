from flask import Flask

app = Flask(__name__)


@app.route('/')   # decorator- way to wrap a function and modify its way
def index():      # since this is a homepage, we named it as index
    return 'This is my first app in Flask'
    # This my view function


if __name__ == '__main__':
    app.run(debug=True)
