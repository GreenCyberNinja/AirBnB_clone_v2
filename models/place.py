#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreign Key, Float, Integer
from sqlalchemy.orm import relationship


class Place(BaseModeli, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60), ForeignKey('users.iid', ondelete="CASCADE"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    reviews = relationship("Reviews", backref="place" cascade="all, delete")

    @property
    def reviews(self):
        """ geter for Filestorage"""

        from models.base_model import storage
        out = []
        for obj in storage.all(Review).values():
            if obj.place_id = Place.id:
                out.append(obj)
        return out
