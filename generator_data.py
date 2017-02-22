from dbModel import *
import random

name = ["派派", "阿肥", "咪咪", "妞妞", "胖胖"
    , "大頭", "阿寶", "皮皮", "嘟嘟", "妮妮"
    , "樂樂", "毛毛", "粉圓", "飯糰", "圓圓"
    , "肥肥", "布丁", "妹妹", "小黑", "旺財"]

picture = ["http://imgur.com/yI00Ehb.jpg",
           "http://i.imgur.com/TtmYVK2.jpg",
           "http://i.imgur.com/EFN7FTv.jpg",
           "http://i.imgur.com/RpD34tu.jpg",
           "http://i.imgur.com/ryCH0b5.jpg",
           "http://i.imgur.com/kzi5kKy.jpg",
           "http://i.imgur.com/bOfNUzK.jpg",
           "http://i.imgur.com/vtb1WCH.jpg",
           "http://i.imgur.com/xrfHjtK.jpg",
           "http://i.imgur.com/z7JCSX8.jpg",
           ]

color = ["#E44040", "#EC21C7", "#8C4C80", "#A41FEC", "#B99ADA"
    , "#4E15E9", "#154EE9", "#4B9CF8", "#65BCD8", "#13EFE4"
    , "#13EFA2", "#13EF63", "#3E7753", "#8DBE1A", "#D6E6AE"
    , "#E8F669", "#949478", "#E4B92C", "#E98915", "#F2802E"]

if __name__ == '__main__':
    print('Start Generator Data......')
    for index in range(1, 201):
        index_name = random.randint(0, len(name) - 1)
        index_pic = random.randint(0, len(picture) - 1)
        index_color = random.randint(0, len(color) - 1)
        insert_data = MapPets(
            Name=name[index_name] + str(index),
            Picture=picture[index_pic],
            Color=color[index_color],
            Longitude=random.uniform(120.47, 121.4),
            Latitude=random.uniform(22.5, 25),
        )
        db.session.add(insert_data)
    db.session.commit()
    print('Generator Data Done')
