#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey

if models.storage_t == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_t != 'db':
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        def reviews(self):
            """
            An attribute eturns the list of Review instances
            with place_id equals to the current Place.id
            """
            from models import storage
            mylist = []
            returned_reviews = storage.all('Review').values()
            for rev in returned_reviews:
                if self.id == rev.place_id:
                    mylist.append(rev)
            return mylist

    else:
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer(), default=0)
        number_bathrooms = Column(Integer(), default=0)
        max_guest = Column(Integer(), default=0)
        price_by_night = Column(Integer(), default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
# amenities = relationship("Amenity", secondary="place_amenity",
#backref="place_amenities", viewonly=False)
