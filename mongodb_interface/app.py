from flask import Flask, request, jsonify

from pymongo import MongoClient

import database

app = Flask(__name__)

app.config.from_object('config')

# specify the location of database
uri = app.config['URI']

# Create client to connect to db
client = MongoClient(uri)

# Create database instance
db = client['student_db']


@app.route('/create', methods=['POST'])
def create():
    response = database.create(db, request.json)
    return response


@app.route('/read', methods=['GET'])
def read():
    response = database.read(db)
    return jsonify(response)


@app.route('/update', methods=['POST'])
def update():
    response = database.update(db, request.json)
    return response


@app.route('/delete', methods=['POST'])
def delete():
    response = database.delete(db, request.json)
    return response


if __name__ == '__main__':
    app.run(debug=True)
