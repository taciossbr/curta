import os
import random
import string
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class URL(db.Model):

    short_url = db.Column(db.String(8), primary_key=True)
    original_url = db.Column(db.String(256))
    def __repr__(self):
        return '<URL short_url=%r, original_url%r>' % (short_url, original_url)
db.create_all()
def generate_code_link():
    conj = string.ascii_letters + string.digits
    s = ''
    for i in range(8):
        s+= random.choice(conj)
    return s

@app.route('/new/<path:url>', methods=['GET'])
def new(url):
    if url.startswith("https://") or url.startswith("http://"):
        rand = generate_code_link()
        new = URL(short_url=rand, original_url=url)
        db.session.add(new)
        db.session.commit()
        r = {
            'original_url': new.original_url,
            'short_url': new.short_url
        }
        return str(r)
    return str({
        'error': "Wrong url format, make sure you have a valid protocol and real site."
    })