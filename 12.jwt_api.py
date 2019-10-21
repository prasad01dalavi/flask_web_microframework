from flask import Flask, request, make_response, jsonify
from functools import wraps
import jwt
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "thisismysecretkey"

# Creating decorator for authorized sites


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
     
        if not(token):
            return jsonify({'message': 'Token is missing!'})
         
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            print(f'[INFO] Data: {data}')
        except Exception as e:
            return jsonify({'message': f'Token in invalid {e}'})

        return f(*args, **kwargs)
    return decorated


@app.route('/unprotected')
def unprotected():
    return 'This has been accessed without token'


@app.route('/protected')
@token_required
def protected():
    return 'You are seeing Protected Site because Token is Correct!'


@app.route('/login')
def index():
    auth = request.authorization
    # Just login with username and password = abc to get token (to login without credentials but with token)
    if auth and auth.username == 'abc' and auth.password == 'abc':
        payload = {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15)}
        token = jwt.encode(payload, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')}) 

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required!"'})


if __name__ == '__main__':
    app.run(debug=True)
