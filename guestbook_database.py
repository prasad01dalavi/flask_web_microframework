from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lmtech123@localhost:3306/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# let me know the changes in the database but i don't want to know

# create database object
db = SQLAlchemy(app)


# class in python will be table in database
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(200))

    # time_created = Column(DateTime(timezone=True), server_default=func.now())
    # time_updated = Column(DateTime(timezone=True), onupdate=func.now())


@app.route('/')   # http://127.0.0.1:5000/
def index():
    all_data = Comments.query.all()  # Gives all data in Comments table
    return render_template('db_index.html', all_data=all_data)


@app.route('/sign')   # http://127.0.0.1:5000/sign
def sign():           # This url will be redirected
    return render_template('db_sign.html')


@app.route('/process', methods=['POST'])  # http://127.0.0.1:5000/process
def process():
    # accessing posted data
    name = request.form['name']
    comment = request.form['comment']

    # now save the data in database (pk will be auto incremented)
    database_query = Comments(name=name, comment=comment)
    db.session.add(database_query)  # adds the posted comment to database
    db.session.commit()             # save the data in database
    return redirect(url_for('index'))   # redirects to the view for /index


if __name__ == '__main__':
    app.run(debug=True)
