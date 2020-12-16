#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete")

    @property
    def cities(self):
        """getter for FileStorage use"""
        # potentially need to encase this in an if statement to protect
        from models.base_model import storage
        out = []
        for obj in storage.all(City).values():
            if obj.state_id == self.id:
                out.append(obj)
        return out
