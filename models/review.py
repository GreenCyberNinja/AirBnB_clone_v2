#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey=(Places.id, ondelete="CASCADE"), nullable=False)
    user_id = column(String(60), ForeignKey=(Users.id, ondelete="CASCADE"), nullable=False)
