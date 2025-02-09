import os
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
import requests
from bs4 import BeautifulSoup

class Goods(Resource):
  def get(self, barcode):
      url = f'https://barcode-list.ru/barcode/RU/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA.htm?barcode={barcode}'
      response = requests.get(url)
      print(response)
      bs = BeautifulSoup(response.text, 'html.parser')
      temp = bs.find('h1', 'pageTitle')
      return jsonify({'ok': temp.text.split(' - ')[0]})

app = Flask(__name__)
api = Api(app)
api.add_resource(Goods, '/goods/<barcode>')


@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(host='127.0.0.1', port=port)
