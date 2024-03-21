#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
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
    reviews = relationship("Review", backref="user", cascade="all, delete")

    def reviews(self):
        """
        An attribute eturns the list of Review instances
        with place_id equals to the current Place.id
        """
        from models import storage
        mylist = []
        returned_reviews = storage.all('Review').values()
        for rev in returned_reviews:
            if self.id == reviews.place_id:
                mylist.append(rev)
        return mylist
