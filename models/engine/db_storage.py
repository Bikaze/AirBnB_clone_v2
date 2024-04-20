#!/usr/bin/python3
"""This file contains the definition of the DBStorage class"""

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class defines the database Storage mechanism"""
    __engine = None
    __session = None

    classes = {'State': State, 'City': City, 'Review': Review,
               'Place': Place, 'User': User, 'Amenity': Amenity}

    def __init__(self):
        """The constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects depending of
        the class name (only if not 'None')"""
        obj_list = []
        obj_dic = {}
        if cls:
            cls = DBStorage.classes[cls]
            obj_list = self.__session.query(cls).all()
        else:
            for clss in DBStorage.classes.values():
                obj_list.extend(self.__session.query(clss).all())
        for obj in obj_list:
            if '_sa_instance_state' in obj.__dict__.keys():
                del obj.__dict__['_sa_instance_state']
            obj_dic.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        return obj_dic

    def new(self, obj):
        """Add an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """This function calls remove() on the private session attribute
        """
        self.__session.remove()
