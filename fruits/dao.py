from pymongo import MongoClient


class FruitsDao:
    def __init__(self):
        client = MongoClient('mongo')
        self.db = getattr(client, 'fruits')

    def find_by_id(self, _id):
        db = self.db.fruits

