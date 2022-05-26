import json

# from bson import json_util
from flask import Flask, abort
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
from main import get_ada_in_wallet

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

words = {}


def abort_if_dosnt_find_word():
    abort(404, message="Ha habido un problema")


"""def parse_json(data):
    return json.loads(json_util.dumps(data))"""


class Stake(Resource):
    def get(self):
        return get_ada_in_wallet()


api.add_resource(Stake, "/stake")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, ssl_context='adhoc')
