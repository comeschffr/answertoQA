from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/qaanswer'

db = SQLAlchemy(app)

@app.route('/set')
def set():
	"""Creates a row to the table of the form (key,value)"""
	for somekey, somevalue in request.args.items():
		thing = Something(key=somekey, value=somevalue)
		db.session.add(thing)
	db.session.commit()
	return f'SET: {somekey}={somevalue}'


@app.route('/get')
def get():
	"""Gets a row of the table from a key"""
	somekey = request.args.get('key')
	somevalue = Something.query.filter_by(key=somekey).first().value
	return f'GET: {somekey}={somevalue}'


# Schema of the table
# Each row is made of a key and a value
class Something(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	key = db.Column(db.String(200), unique=True, nullable=False)
	value = db.Column(db.String(200), unique=True, nullable=False)


if __name__ == '__main__':
	app.run(debug=True, port=4000)