# leaflet-tutorials-interesting
[leaflet](http://leafletjs.com/) tutorials interesting use Python Flask 📝

* [Youtube Demo](https://youtu.be/JVljuudfamM)

## Leaflet 與  Google Map 比較

* [leaflet](http://leafletjs.com/) 在手機上表現的效能以及速度勝過 Google Map
* Google Map 精準度比 [leaflet](http://leafletjs.com/) 高
* [leaflet](http://leafletjs.com/) 有很多額外的 [plugins](http://leafletjs.com/plugins.html)

## 安裝套件

clone 專案

```
git clone https://github.com/twtrubiks/leaflet-tutorials-interesting
cd leaflet-tutorials-interesting
```

建立虛擬環境並安裝相依套件

```
pip install -r requirements.txt
```

## 使用方法 以及 執行畫面

第一次使用先初始化資料庫 (Flask-Migrate 4.x 已內建 `flask db` CLI,不再需要 Flask-Script)

```
export FLASK_APP=app.py        # Windows PowerShell: $env:FLASK_APP="app.py"
flask db init
flask db migrate -m "init"
flask db upgrade
```

接著產生模擬資料

```
python generator_data.py
```
執行完畢後， app.db 裡會多出 200 筆資料，可以使用 [SQLiteBrowser](http://sqlitebrowser.org/) 觀看

![alt tag](http://i.imgur.com/QSFJANB.jpg)

接著我們設計簡單的 api ， 其實就是去讀 app.db 的資料，接著在吐給前端而已。

```python
@app.route("/api", methods=["POST"])
def api():
    pets = MapPets.query.all()
    return jsonify([
        {
            "Name": p.Name,
            "Picture": p.Picture,
            "Color": p.Color,
            "Longitude": p.Longitude,
            "Latitude": p.Latitude,
        }
        for p in pets
    ])
```


## 執行畫面

只在本機跑 (預設綁 `127.0.0.1:5000`,只有自己連得到):

```
python app.py
```

想讓區網 / 外網其他裝置也連得進來,改用 Flask CLI 並指定 `--host=0.0.0.0`:

```
export FLASK_APP=app.py        # Windows PowerShell: $env:FLASK_APP="app.py"
flask run --host=0.0.0.0 --port=5000 --debug
```

> 兩個都是 Werkzeug 開發 server,**不適合 production**。正式部署請改用 gunicorn / uWSGI 等 WSGI server (例如 `gunicorn -w 4 'app:app'`)。

首頁

左上角可以全螢幕

![alt tag](http://i.imgur.com/6GcySl1.jpg)

![alt tag](http://i.imgur.com/RQYBOpw.jpg)

點隨任一個動物，會跳出名稱和經緯度

![alt tag](http://i.imgur.com/vL7ai1n.jpg)

也有搜索功能

![alt tag](http://i.imgur.com/ihcEUrZ.jpg)

選定後，會移到該動物的位置

![alt tag](http://i.imgur.com/tiwg6s7.jpg)

## 執行環境

* Python 3.13
* Flask 3.1
* Flask-SQLAlchemy 3.1 / SQLAlchemy 2.0
* Flask-Migrate 4.1
* Leaflet 1.9.4 + 相關 plugin 全部走 jsDelivr CDN

## Reference
* [Leaflet](https://leafletjs.com/)
* [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster)
* [leaflet-locatecontrol](https://github.com/domoritz/leaflet-locatecontrol)
* [leaflet.fullscreen](https://github.com/brunob/leaflet.fullscreen)
* [leaflet-search](https://github.com/stefanocudini/leaflet-search)
* [Leaflet.SmoothMarkerBouncing](https://github.com/hosuaby/Leaflet.SmoothMarkerBouncing)

## License
MIT license
