#!/usr/bin/python3
from os import getenv

if getenv("HBNB_TYPE_STORAGE"):
    storage_t = getenv("HBNB_TYPE_STORAGE")
else:
    storage_t = 'file'

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
