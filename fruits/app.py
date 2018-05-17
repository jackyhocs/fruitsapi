from flask import Flask
from flask_restful import Resource
from util.validation import validate_payload
from util.fruits_validation import post_schema
from util.exception_utils import ApiCustomErrorHandler, errors
from util.exceptions import DBException, ResultNotFound, ApiException

from fruits.model import FruitsModel


app = Flask(__name__)
api = ApiCustomErrorHandler(app)
app.register_blueprint(errors)


class Fruits(Resource):
    def get(self, _id):
        fruits_model = FruitsModel()
        try:
            fruit = fruits_model.find_by_id(_id)
        except DBException as e:
            raise ApiException(
                message='Internal Server Error',
                status=500
            ) from e
        return fruit, 5200


class FruitsQuery(Resource):
    @validate_payload(post_schema)
    def post(self):
        return {}, 501


api.add_resource(Fruits, '/<_id>')
api.add_resource(FruitsQuery, '/')

if __name__ == "__main__":
    app.run(debug=True, port=80)
