"""
https://gionkunz.github.io/chartist-js/
"""

from flask import Flask, render_template, jsonify
from random import sample

app = Flask(__name__)


@app.route('/')
def index():
    data = jsonify({'my_data': sample(range(1, 10), 5)})
    return render_template('chart.html')


@app.route('/data')
def data():
    print sample(range(1, 10), 5)
    my_list = []
    my_list.append(sample(range(1, 10), 5))
    return jsonify({'my_data': sample(range(1, 10), 5)})


if __name__ == '__main__':
    app.run(debug=True)
