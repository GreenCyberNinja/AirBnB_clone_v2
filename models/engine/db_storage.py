#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
classed = [Amenity, City,
           Place, Review, State, User]


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the DBStorage object"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            self.__engine.drop_all()

    def all(self, cls=None):
        """returns everything inside database"""
        out = {}
        for ind in classed:
            if cls is None or ind == cls:
                ls_obj = self.__session.query(cls).all()
                for obj in ls_obj:
                    my_id = obj.__class__.__name__ + "." + obj.id
                    out.update({my_id: obj})
        return out

    def new(self, obj):
        """ creates new table in db"""
        self.__session.add(obj)

    def save(self):
        """ saves the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the database"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """reloads the session"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        master = scoped_session(factory)
        self.__session = master()

    def close(self):
        """closes the session"""
        self.__session.close()
