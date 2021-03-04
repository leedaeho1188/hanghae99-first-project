from flask import Flask, render_template, jsonify, request, redirect, url_for
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbhh99_1

SECRET_KEY = 'SPARTA'

import jwt

import datetime

import hashlib

from werkzeug.utils import secure_filename

from datetime import datetime, timedelta

@app.route('/')
def Home():
   return render_template('index.html')

@app.route('/artShow', methods=['GET'])
def artShow():
   data = list(db.Share_artShow.find({}, {'_id': False}))
   return render_template('artShow.html', blogs = data)

@app.route('/Performance', methods=['GET'])
def performance():
   data = list(db.Share_Performance.find({}, {'_id': False}))
   return render_template('performance.html', blogs = data)

# @app.route('/artshow', methods=['GET'])
# def listingArtShow():
#    blogs = list(db.Share_artShow.find({}, {'_id': False}))
#    return jsonify({'all_blogs': blogs})

# @app.route('/performance', methods=['GET'])
# def listingPerformance():
#    blogs = list(db.Share_Performance.find({}, {'_id': False}))
#    return jsonify({'all_blogs': blogs})

@app.route('/sign_up/save', methods=['POST'])
def sign_up():
   username_receive = request.form['username_give']
   password_receive = request.form['password_give']
   password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
   doc = {
      "username": username_receive,                              
      "password": password_hash,                                  
      "profile_name": username_receive,                           
   }
   db.user_info.insert_one(doc)
   return jsonify({'result': 'success'})

@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
   username_receive = request.form['username_give']
   exists = bool(db.user_info.find_one({"username": username_receive}))
   return jsonify({'result': 'success', 'exists': exists})

@app.route('/sign_in', methods=['POST'])
def sign_in():

   username_receive = request.form['username_give']
   password_receive = request.form['password_give']

   pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
   result = db.user_info.find_one({'username': username_receive, 'password': pw_hash})

   if result is not None:
      payload = {
      'id': username_receive,
      'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24) 
      }
      token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

      return jsonify({'result': 'success', 'token': token})

   else:
      return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
      
@app.route('/review/artshow', methods=['POST'])
def submit_artShow_review():
   token_receive = request.cookies.get('mytoken')
   payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
   title_receive = request.form['title_give']
   review_receive = request.form['review_give']
   doc = {
      "username" : payload["id"],
      "title" : title_receive,
      "review" : review_receive
   }
   db.artshow_review.insert_one(doc)
   return jsonify({'msg':'저장완료!'})

@app.route('/review/performance', methods=['POST'])
def submit_performance_review():
   token_receive = request.cookies.get('mytoken')
   payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
   title_receive = request.form['title_give']
   review_receive = request.form['review_give']
   doc = {
      "username" : payload["id"],
      "title" : title_receive,
      "review" : review_receive
   }
   db.performance_review.insert_one(doc)
   return jsonify({'msg':'저장완료!'})

@app.route('/review/artshow/reviews', methods=['GET'])
def show_artShow_review():
   data_reviews = list(db.artshow_review.find({}, {'_id': False}))
   return jsonify({'reviews': data_reviews})
   

@app.route('/review/performance/reviews', methods=['GET'])
def show_performance_review():
   data_reviews = list(db.performance_review.find({}, {'_id': False}))
   return jsonify({'reviews': data_reviews})


   
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
