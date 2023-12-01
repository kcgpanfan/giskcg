from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_data():
    if request.method == 'POST':
        cs_no = request.form['cs_no']
    else:
        cs_no = ''
    
    url = 'http://61.218.242.179/GISMap/JMap/mapPages/ThemePages/Themes/clicked_NFA119case.jsp'

    data = {
        'cs_no': cs_no
    }

    response = requests.get(url, params=data)

    # 使用 BeautifulSoup 解析 HTML 回應
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取目標表格的內容
    table = soup.find('table', style='font-size:16px;width:100%')
    rows = table.find_all('tr')

    # 建立包含提取資料的列表
    data_list = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            label = cells[0].get_text(strip=True)
            value = cells[1].get_text(strip=True)
            data_list.append((label, value))

    # 將回應內容傳遞給模板
    return render_template('01.html', data_list=data_list)

if __name__ == '__main__':
    app.run()

    # 打開瀏覽器
    webbrowser.open('http://localhost:5000/')