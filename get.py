from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource
from flask_cors import CORS
from component import get_covid, country, get_covid_ind, get_state

app = Flask(__name__)
api = Api(app)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return render_template('index.html')


class rest_api(Resource):
    def get(self, country_name="world"):
        Dict, countries = get_covid()

        if country_name == "world":
            return jsonify(Dict)
        else:
            country_name = str(country_name)
            return jsonify(country(country_name, Dict, countries))


class ind_api(Resource):
    def get(self, state_name):
        state_data, state = get_covid_ind()
        state_name = str(state_name)

        return jsonify(get_state(state_name, state_data, state))


api.add_resource(rest_api, "/world", endpoint="")
api.add_resource(rest_api, "/<country_name>", endpoint="country")
api.add_resource(ind_api, "/india/<state_name>", endpoint="state")

if __name__ == "__main__":
    app.run()
