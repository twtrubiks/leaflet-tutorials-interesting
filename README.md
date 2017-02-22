# leaflet-tutorials-interesting
[leaflet](http://leafletjs.com/) tutorials interesting use Python Flask 📝

* [Youtube Demo](https://youtu.be/JVljuudfamM)



## Leaflet 與  Google Map 比較

* [leaflet](http://leafletjs.com/) 在手機上表現的效能以及速度勝過 Google Map
* Google Map 精準度比 [leaflet](http://leafletjs.com/) 高
* [leaflet](http://leafletjs.com/) 有很多額外的 [plugins](http://leafletjs.com/plugins.html)

## 安裝套件
確定電腦有安裝 [Python](https://www.python.org/) 之後

clone 我的簡單範例

```
git clone https://github.com/twtrubiks/leaflet-tutorials-interesting
```

接著請在  cmd (命令提示字元) 輸入以下指令
```
pip install -r requirements.txt
```

## 使用方法 以及 執行畫面

先產生模擬資料
```
python generator_data.py
```
執行完畢後， app.db 裡會多出 200 筆資料，可以使用 [SQLiteBrowser](http://sqlitebrowser.org/) 觀看

![alt tag](http://i.imgur.com/QSFJANB.jpg)

接著我們設計簡單的 api ， 其實就是去讀 app.db 的資料，接著在吐給前端而已。

```
@app.route("/api", methods=['POST'])
def api():
    db_data = MapPets.query.all()
    infornation_dic = {}
    infornation_list = []
    for data in db_data:
        infornation_dic['data'] = []
        infornation_dic['Name'] = data.Name
        infornation_dic['Picture'] = data.Picture
        infornation_dic['Color'] = data.Color
        infornation_dic['Longitude'] = data.Longitude
        infornation_dic['Latitude'] = data.Latitude
        infornation_list.append(infornation_dic)
        infornation_dic = {}

    return json.dumps(infornation_list)
```


## 執行畫面

```
python app.py
```

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
* Python 3.4.3

## Reference
* [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster)
* [leaflet-locatecontrol](https://github.com/domoritz/leaflet-locatecontrol)
* [leaflet.fullscreen](https://github.com/brunob/leaflet.fullscreen)
* [leaflet-search](https://github.com/stefanocudini/leaflet-search)
* [Leaflet.SmoothMarkerBouncing](https://github.com/hosuaby/Leaflet.SmoothMarkerBouncing)


## License
MIT license
