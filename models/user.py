#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place
import models


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.storage_t == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
# reviews = relationship("Review", backref="user", cascade="all, delete")
