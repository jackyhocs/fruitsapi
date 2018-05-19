import uuid
from fruits.dao import FruitsDao


class FruitsModel:
    def find_by_id(self, _id):
        fruit_dao = FruitsDao()
        fruit = fruit_dao.find_by_id(_id)
        return fruit

    def create(self, payload):
        fruit_dao = FruitsDao()
        payload['id'] = uuid.uuid4()
        fruit_dao.create(payload)

    def update(self, _id, payload):
        fruit_dao = FruitsDao()
        fruit_dao.update(_id, payload)

    def delete(self, _id):
        fruit_dao = FruitsDao()
        fruit_dao.delete(_id)

    def get_by_params(self, params):
        fruit_dao = FruitsDao()
        fruits = fruit_dao.get_by_params(params)
        return fruits
