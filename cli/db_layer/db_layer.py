from tinydb import TinyDB, Query
import os


class TinyDBLayer(object):
    def __init__(self, save_folder: str,db_file):
        self.db = TinyDB(os.path.join(save_folder, db_file))

    def insert(self ,row: dict):
        id = self.db.insert(row)
        return {"id": id, **row}

    def all(self):
        return self.db.all()

    def get(self,id: str):
        data = self.db.get(doc_id=id)
        return data

    def delete(self, id: str):
        data = self.db.get(doc_id=id)
        if data:
            # os.remove(os.path.join(save_folder, data["filename"]))
            self.db.remove(doc_ids=[id,])