import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=True, nullable=False)
    email = Column(String(50),nullable=False)
    password = Column(String(20),nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=True, nullable=False)
    homeworld= Column(String(250), ForeignKey('planetas.name'),nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=True, nullable=False)
             

class Favoritospersonajes(Base):
    __tablename__ = 'favoritospersonajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250),ForeignKey('user.name'))
    namepersonaje = Column(String(250), ForeignKey('personajes.name'))

class Favoritosplanetas(Base):
    __tablename__ = 'favoritosplanetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250),ForeignKey('user.name'))
    nameplanetas = Column(String(250), ForeignKey('planetas.name'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')