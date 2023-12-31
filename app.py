from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, send_file

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_pdf')
def download_pdf():
    return send_file('static/How_to_achieve_Peace.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run()


