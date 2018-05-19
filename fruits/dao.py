from pymongo import MongoClient
from util.exceptions import DBException, ResultNotFound


class FruitsDao:
    def __init__(self):
        client = MongoClient('mongo')
        self.db = getattr(client, 'fruits')

    def find_by_id(self, _id):
        db = self.db.fruits

        try:
            fruit = db.find_one({"id": _id})
        except Exception as e:
            raise DBException from e

        if not fruit:
            raise ResultNotFound

        return fruit

    def create(self, payload):
        db = self.db.fruits

        try:
            db.insert_one(payload)
        except Exception as e:
            raise DBException from e

    def update(self, _id, payload):
        db = self.db.fruits

        try:
            updated = db.update_one({'id': _id}, {"$set": payload}, upsert=False)
        except Exception as e:
            raise DBException from e

        if not updated.modified_count:
            return ResultNotFound

    def delete(self, _id):
        db = self.db.fruits
        try:
            deleted = db.delete_one({'id': _id})
        except Exception as e:
            raise DBException from e

        if not deleted.deleted_count:
            raise ResultNotFound

    def get_by_params(self, params):
        db = self.db.fruits

        try:
            fruits = db.find(params)
        except Exception as e:
            raise DBException from e

        return fruits
