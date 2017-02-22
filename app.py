from flask import *
from dbModel import *

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(debug=True)
