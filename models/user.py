#!/usr/bin/python3
"""This module creates a User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing User objects."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
