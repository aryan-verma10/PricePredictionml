from flask import Flask, request, jsonify
from flask_cors import CORS
import util
# following command used to create an app
app = Flask(__name__)


@app.route("/get_location_name", methods=["GET"])
def get_location_name():
    response = jsonify(
        {
            'locations': util.get_location()
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/predict_home_price", methods=['GET', 'POST'])
def predict_home_price():
    location = request.form["location"]
    area = int(request.form["area"])
    bhk = int(request.form["bhk"])
    print(util.get_estimated_price(location, area, bhk))
    response = jsonify({
        "estimated_price": util.get_estimated_price(location, area, bhk)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    print("Starting Python flask server for Home price prediction")
    CORS(app)
    app.run(debug = False, host='0.0.0.0')  # this makes website visibel publicalygit
