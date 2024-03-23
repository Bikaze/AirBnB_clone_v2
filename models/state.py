#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        def cities(self):
            """Returns the list of City instances with state_id equals
               to the State.id"""
            dic_val = storage.all(City).values()
            cty_list = []
            for city in dic_val:
                if city.state_id == self.id:
                    cty_list.append(city)
            return cty_list
