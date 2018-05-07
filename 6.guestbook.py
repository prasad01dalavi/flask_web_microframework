from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')   # http://127.0.0.1:5000/
def index():
	return render_template('index.html')

@app.route('/sign')   # http://127.0.0.1:5000/sign 
def sign():           # This url will be redirected
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	return render_template('index.html', name=name, comment=comment)

@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)

if __name__ == '__main__':
	app.run(debug=True)
