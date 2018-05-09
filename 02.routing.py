from flask import Flask

app = Flask(__name__)


# decorator- way to wrap a function and modify its way of behaviour
@app.route('/')   # Decorator maps the url to the return value
def index():
    return 'This is my Flask root !'


@app.route('/home')     # http://127.0.0.1:5000/home
def home():
    return '<h1>HOME PAGE!</h1>'


@app.route('/profile/<username>')   # http://127.0.0.1:5000/profile/prasad
def profile(username):              # username will be a variable
    print 'Type of variable:', type(username), username
    # ! I tried to check whether the method is run when we hit the url
    # ! but It didn't actually
    return "<h2>Hey there, %s !<h2>" % username


# specify the data type of argument e.g. int, string, float etc.
@app.route('/post/<int:post_id>')   # http://127.0.0.1:5000/post/13
def show_int(post_id):        # method name doesn't need to be same as url
    print 'Type of variable:', type(post_id), post_id
    # ! I tried to check whether the method is run when we hit the url
    # ! but It didn't actuallyss
    return "<h2>Post ID: %d <h2>" % post_id


if __name__ == '__main__':
    app.run(debug=True)
