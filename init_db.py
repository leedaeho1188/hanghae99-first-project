from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhh99_1

# @app.route('/artshow', methods=['GET'])
# def listingArtShow():
#     blogs = list(db.Share_artShow.find({}, {'_id': False})
#     return jsonify({'all_blogs': blogs})



## API 역할을 하는 부분
def savingArtShow1():
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://www.culture.go.kr/perform/performList.do?cPage=1&genre=6&searchKeywordType=t',
      verify=False)

   soup = BeautifulSoup(data.text, 'html.parser')

   shows = soup.select('#contents > div.list_type1 > ul > li')

   for show in shows:
      title = show.select_one('dl > dt > a > span').text
      url = "https://www.culture.go.kr" + show.select_one('a.hoverDot')['href']
      image = "https://www.culture.go.kr" + show.select_one('a.hoverDot > div > img')['src']
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text
      date = show.select_one('dl > dd.date').text

      doc = {
            'title': title,
            'image': image,
            'loc': loc,
            'url': url,
            'loc_detail': loc_detail,
            'date': date
         }

      db.Share_artShow.insert_one(doc)
   print('완료', title)

def savingArtShow2():
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://www.culture.go.kr/perform/performList.do?cPage=2&genre=6&searchKeywordType=t',
      verify=False)

   soup = BeautifulSoup(data.text, 'html.parser')

   shows = soup.select('#contents > div.list_type1 > ul > li')

   for show in shows:
      title = show.select_one('dl > dt > a > span').text.strip()
      url = "https://www.culture.go.kr" + show.select_one('a.hoverDot')['href']
      image = "https://www.culture.go.kr" + show.select_one('a.hoverDot > div > img')['src']
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text
      date = show.select_one('dl > dd.date').text

      doc = {
         'title': title,
         'image': image,
         'loc': loc,
         'url': url,
         'loc_detail': loc_detail,
         'date': date
      }

      db.Share_artShow.insert_one(doc)
      print('완료', title)



   #  return jsonify({'msg':'저장이 완료되었습니다.'})
def savingPerformance1():
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://www.culture.go.kr/perform/performList.do?cPage=1&genre=8&searchKeywordType=t',
      verify=False)

   soup = BeautifulSoup(data.text, 'html.parser')

   shows = soup.select('#contents > div.list_type1 > ul > li')

   for show in shows:
      title = show.select_one('dl > dt > a > span').text.strip()
      url = "https://www.culture.go.kr" + show.select_one('a.hoverDot')['href']
      image = "https://www.culture.go.kr" + show.select_one('a.hoverDot > div > img')['src']
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text
      date = show.select_one('dl > dd.date').text

      doc = {
         'title': title,
         'image': image,
         'loc': loc,
         'url': url,
         'loc_detail': loc_detail,
         'date': date
      }

      db.Share_Performance.insert_one(doc)
      print('완료', title)

def savingPerformance2():
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://www.culture.go.kr/perform/performList.do?cPage=2&genre=8&searchKeywordType=t',
      verify=False)

   soup = BeautifulSoup(data.text, 'html.parser')

   shows = soup.select('#contents > div.list_type1 > ul > li')

   for show in shows:
      title = show.select_one('dl > dt > a > span').text.strip()
      url = "https://www.culture.go.kr" + show.select_one('a.hoverDot')['href']
      image = "https://www.culture.go.kr" + show.select_one('a.hoverDot > div > img')['src']
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text
      date = show.select_one('dl > dd.date').text

      doc = {
         'title': title,
         'image': image,
         'loc': loc,
         'url': url,
         'loc_detail': loc_detail,
         'date': date
      }

      db.Share_Performance.insert_one(doc)
      print('완료', title)

def savingPerformance3():
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://www.culture.go.kr/perform/performList.do?cPage=3&genre=8&searchKeywordType=t',
      verify=False)

   soup = BeautifulSoup(data.text, 'html.parser')

   shows = soup.select('#contents > div.list_type1 > ul > li')

   for show in shows:
      title = show.select_one('dl > dt > a > span').text.strip()
      url = "https://www.culture.go.kr" + show.select_one('a.hoverDot')['href']
      image = "https://www.culture.go.kr" + show.select_one('a.hoverDot > div > img')['src']
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text
      date = show.select_one('dl > dd.date').text

      doc = {
         'title': title,
         'image': image,
         'loc': loc,
         'url': url,
         'loc_detail': loc_detail,
         'date': date
      }

      db.Share_Performance.insert_one(doc)
      print('완료', title)

def savingPerformance4():
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://www.culture.go.kr/perform/performList.do?cPage=4&genre=8&searchKeywordType=t',
      verify=False)

   soup = BeautifulSoup(data.text, 'html.parser')

   shows = soup.select('#contents > div.list_type1 > ul > li')

   for show in shows:
      title = show.select_one('dl > dt > a > span').text.strip()
      url = "https://www.culture.go.kr" + show.select_one('a.hoverDot')['href']
      image = "https://www.culture.go.kr" + show.select_one('a.hoverDot > div > img')['src']
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text
      date = show.select_one('dl > dd.date').text

      doc = {
         'title': title,
         'image': image,
         'loc': loc,
         'url': url,
         'loc_detail': loc_detail,
         'date': date
      }

      db.Share_Performance.insert_one(doc)
      print('완료', title)

def savingPerformance5():
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get('https://www.culture.go.kr/perform/performList.do?cPage=5&genre=8&searchKeywordType=t',
      verify=False)

   soup = BeautifulSoup(data.text, 'html.parser')

   shows = soup.select('#contents > div.list_type1 > ul > li')

   for show in shows:
      title = show.select_one('dl > dt > a > span').text.strip()
      url = "https://www.culture.go.kr" + show.select_one('a.hoverDot')['href']
      image = "https://www.culture.go.kr" + show.select_one('a.hoverDot > div > img')['src']
      loc = show.select_one('dl > dd:nth-child(3) > span.loc').text
      loc_detail = show.select_one('dl > dd:nth-child(3) > span.loc_detail').text
      date = show.select_one('dl > dd.date').text

      doc = {
         'title': title,
         'image': image,
         'loc': loc,
         'url': url,
         'loc_detail': loc_detail,
         'date': date
      }

      db.Share_Performance.insert_one(doc)
      print('완료', title)


def insert_allArtShow():
   db.Share_artShow.drop()
   savingArtShow1()
   savingArtShow2()

def insert_allPerformance():
   db.Share_Performance.drop()
   savingPerformance1()
   savingPerformance2()
   savingPerformance3()
   savingPerformance4()
   savingPerformance5()



insert_allArtShow()
insert_allPerformance()

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)