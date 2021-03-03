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

@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": username_receive,                           # 프로필 이름 기본값은 아이디
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
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.user_info.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)