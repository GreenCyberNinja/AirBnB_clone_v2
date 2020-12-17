#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import sqlalchemy


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the DBStorage object"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            self.__engine.drop_all()

    def all(self, cls=None):
        """x"""
        if cls is None:
            cls = [User, State, City, Amenity, Place, Review]
        out = {}
        for obj in self.__session.query(cls):
            my_id = obj.__classname__ + "." + obj.id
            out.update({my_id: obj})
        return out

    def new(self, obj):
        """x"""
        self.__session.add(obj)

    def save(self):
        """x"""
        self.__session.commit()

    def delete(self, obj=None):
        """x"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """x"""
        from models import User, State, City, Amenity, Place, Review
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        master = scoped_session(factory)
        self.__session = master()
