from ..database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True)
    email_id = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    logged_in = Column(Boolean)
    order_details = relationship("Orders", back_populates="user")  # make a relationship with two tables using sqlalchemy orm method

    def __repr__(self) -> str:
        return f'<User {self.username} : {self.id}>'


class Orders(Base):
    __tablename__ = 'orders'

    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('INTRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large')
    )

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=True)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default='PENDING')
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default='SMALL')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='order_details')

    def __repr__(self) -> str:
        return f'<Order {self.id}>'
