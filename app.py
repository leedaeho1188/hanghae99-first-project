<<<<<<< HEAD
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



# @app.route('/artshow', methods=['GET'])
# def listingArtShow():
#     blogs = list(db.artShow.find({}, {'_id': False}))
#     return jsonify({'all_blogs': blogs})



## API 역할을 하는 부분

def savingArtShow():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(https://www.culture.go.kr/perform/performList.do?cPage=1&genre=6&searchKeywordType=t, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    shows = soup.select('#contents > div.list_type1 > ul > li')

    for show in shows:
      title = show.select_one('dl > dt > a > span').text
      url = show.select_one('dl > dt > a')['href']
      image = show.select_one('a.hoverDot > div > img').get("src")
      date = show.select_one('dl > dd.date').text
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text



  
    # desc = soup.select_one('meta[property="og:description"]')['content']

    # doc = {
    #     'title':title,
    #     'image':image,
    #     'comment':comment_receive,
    #     'url': url_receive,
    #     'name': name_receive,
    #     'like': 0
    # }
    # db.artShow.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})




if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
=======






>>>>>>> df0d407f7132f9a39487d3cd585d487ca4fa4663
