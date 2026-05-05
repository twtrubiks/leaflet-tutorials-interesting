import random

from app import app
from models import MapPets, db

name = ["派派", "阿肥", "咪咪", "妞妞", "胖胖",
        "大頭", "阿寶", "皮皮", "嘟嘟", "妮妮",
        "樂樂", "毛毛", "粉圓", "飯糰", "圓圓",
        "肥肥", "布丁", "妹妹", "小黑", "旺財"]

picture = [
    "https://imgur.com/yI00Ehb.jpg",
    "https://i.imgur.com/TtmYVK2.jpg",
    "https://i.imgur.com/EFN7FTv.jpg",
    "https://i.imgur.com/RpD34tu.jpg",
    "https://i.imgur.com/ryCH0b5.jpg",
    "https://i.imgur.com/kzi5kKy.jpg",
    "https://i.imgur.com/bOfNUzK.jpg",
    "https://i.imgur.com/vtb1WCH.jpg",
    "https://i.imgur.com/xrfHjtK.jpg",
    "https://i.imgur.com/z7JCSX8.jpg",
]

color = ["#E44040", "#EC21C7", "#8C4C80", "#A41FEC", "#B99ADA",
         "#4E15E9", "#154EE9", "#4B9CF8", "#65BCD8", "#13EFE4",
         "#13EFA2", "#13EF63", "#3E7753", "#8DBE1A", "#D6E6AE",
         "#E8F669", "#949478", "#E4B92C", "#E98915", "#F2802E"]


if __name__ == "__main__":
    print("Start Generator Data......")
    with app.app_context():
        for index in range(1, 201):
            db.session.add(MapPets(
                Name=random.choice(name) + str(index),
                Picture=random.choice(picture),
                Color=random.choice(color),
                Longitude=random.uniform(120.47, 121.4),
                Latitude=random.uniform(22.5, 25),
            ))
        db.session.commit()
    print("Generator Data Done")
