from flask import Flask, request, make_response
from functools import wraps


app = Flask(__name__)


# Creating decorator for authorized sites	
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'prasad' and auth.password == 'prasad':
            return f(*args, **kwargs)
        return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required!"'})
    return decorated

@app.route('/')
def index():
    auth = request.authorization 

    if auth and auth.username == 'abc'  and auth.password == 'abc':
        return '<h1>You are logged in</h1>'

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required!"'})


@app.route('/page')
@auth_required
def page():
    return "<h1>You are on the Page</h1>"


if  __name__ == '__main__':
    app.run(debug=True)
