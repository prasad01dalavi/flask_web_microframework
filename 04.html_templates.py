from flask import Flask, render_template
# Import render_template to render html templates


app = Flask(__name__)


# decorator- way to wrap a function and modify its way of behaviour
@app.route('/')   # http://127.0.0.1:5000/
def index():
    return '<h2>Home Page !</h2>'


@app.route('/profile/<name>')  # http://127.0.0.1:5000/profile/prasad
def profile(name):
    return render_template('profile.html', context=name)
    # Renders template with context


if __name__ == '__main__':
    app.run(debug=True)
