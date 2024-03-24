#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """This is the model class for amenities table"""
    if models.storage_t == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)

    else:
        name = ""
