import os
import random
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/new/<url>')
def hello_world(url):

    if url.startswith("https://") or url.startswith("http://"):
        new = {
            'original_url': url,
            'short_url': int(random.random()*100000000)
        }
        print(new)
        mongo.db.urls.insert(new)
        return "Hello, world"
    
    return str({
        'error': "Wrong url format, make sure you have a valid protocol and real site."
    })