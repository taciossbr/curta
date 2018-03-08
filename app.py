import os
import random
from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
app['MONGO_URI'] = os.environ['MONGODB_URI']

@app.route('/new/<path:url>', methods=['GET'])
def hello_world(url):

    if url.startswith("https://") or url.startswith("http://"):
        new = {
            'original_url': url,
            'short_url': int(random.random()*100000000)
        }
        mongo.db.urls.insert(new)
        r = {
            'original_url': new['original_url'],
            'short_url': request.url.split('new/')[0] + str(new['short_url'])
        }
        return str(r)
    
    return str({
        'error': "Wrong url format, make sure you have a valid protocol and real site."
    })