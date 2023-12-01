from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://gis.fdkc.gov.tw/rescue/getnowcase/json?getalls=1"
    headers = {
        'Referer': 'https://gis.fdkc.gov.tw/rescue/'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return '請求資料失敗'
    json_data = response.json()
    return render_template("t1.html", data=json_data)

if __name__ == "__main__":
    app.run(port=5200)