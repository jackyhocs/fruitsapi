from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Fruits(Resource):
    def get(self, _id):
        return {}, 501


class FruitsQuery(Resource):
    def post(self):
        return {}, 501


api.add_resource(Fruits, '/<_id>')
api.add_resource(FruitsQuery, '/')

if __name__ == "__main__":
    app.run(debug=True, port=80)
