from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)



class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(Date)
    region = Column(String)
    product = Column(String)
    unit_price = Column(Numeric(10, 2))
    quantity = Column(Integer)
    amount = Column(Numeric(10, 2))
    description = Column(String, nullable=True)

    user = relationship('User', backref='sales')