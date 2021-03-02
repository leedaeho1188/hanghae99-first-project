from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbhh99_1

@app.route('/')
def Home():
   return render_template('index.html')

@app.route('/artShow')
def artShow():
   return render_template('artShow.html')

@app.route('/Performance')
def performance():
   return render_template('performance.html')

@app.route('/artshow', methods=['GET'])
def listingArtShow():
   blogs = list(db.Share_artShow.find({}, {'_id': False}))
   
   return jsonify({'all_blogs': blogs})

@app.route('/performance', methods=['GET'])
def listingPerformance():
   blogs = list(db.Share_Performance.find({}, {'_id': False}))
   return jsonify({'all_blogs': blogs})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)