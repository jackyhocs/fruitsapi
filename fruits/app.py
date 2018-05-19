import uuid

from flask import Flask
from flask_restful import Resource, request
from util.validation import validate_payload, validate_params
from util.fruits_validation import post_schema, get_schema, put_schema
from util.exception_utils import ApiCustomErrorHandler, errors
from util.exceptions import DBException, ResultNotFound, ApiException

from fruits.model import FruitsModel


app = Flask(__name__)
api = ApiCustomErrorHandler(app)
app.register_blueprint(errors)


class Fruits(Resource):
    def get(self, _id, **kwargs):
        fruits_model = FruitsModel()

        try:
            uuid.UUID(_id, version=4)
            fruit = fruits_model.find_by_id(_id)
        except DBException as e:
            raise ApiException(
                message='Internal Server Error',
                status=500
            ) from e
        except ResultNotFound as e:
            raise ApiException(
                message="Result not found",
                status=404
            ) from e
        except ValueError as e:
            raise ApiException(
                message="Invalid ID entered",
                status=400
            ) from e

        return fruit, 200

    @validate_payload(put_schema)
    def put(self, _id, **kwargs):
        fruits_model = FruitsModel()
        payload = kwargs['payload']
        try:
            uuid.UUID(_id, version=4)
            fruits_model.update(_id, payload)
        except DBException as e:
            raise ApiException(
                message='Internal Server Error',
                status=500
            ) from e
        except ResultNotFound as e:
            raise ApiException(
                message="Result not found",
                status=404
            ) from e
        except ValueError as e:
            raise ApiException(
                message="Invalid ID entered",
                status=400
            ) from e

        return {}, 204

    def delete(self, _id, **kwargs):
        fruits_model = FruitsModel()

        try:
            uuid.UUID(_id, version=4)
            fruits_model.delete(_id)
        except DBException as e:
            raise ApiException(
                message='Internal Server Error',
                status=500
            ) from e
        except ResultNotFound as e:
            raise ApiException(
                message="Result not found",
                status=404
            ) from e
        except ValueError as e:
            raise ApiException(
                message="Invalid ID entered",
                status=400
            ) from e

        return {}, 204


class FruitsQuery(Resource):
    @validate_payload(post_schema)
    def post(self, **kwargs):
        fruits_model = FruitsModel()
        payload = kwargs['payload']
        try:
            fruits_model.create(payload)
        except DBException as e:
            raise ApiException(
                message='Internal Server Error',
                status=500
            ) from e

        return {}, 204

    @validate_params(get_schema)
    def get(self, **kwargs):
        fruits_model = FruitsModel()
        params = request.args.to_dict()
        try:
            fruits = fruits_model.get_by_params(params)
        except DBException as e:
            raise ApiException(
                message='Internal Server Error',
                status=500
            ) from e

        return fruits, 200


api.add_resource(Fruits, '/<_id>')
api.add_resource(FruitsQuery, '/')

if __name__ == "__main__":
    app.run(debug=True, port=80)
