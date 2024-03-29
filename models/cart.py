from datetime import datetime, timedelta
from app import db
from models.base import BaseModel
from models.order import OrderModel


class CartModel(db.Model, BaseModel):
    # table name
    __tablename__ = "carts"
    # table data
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    expire_date = db.Column(db.DateTime, default=datetime.utcnow() + timedelta(days=1))
    # relationships
    products = db.relationship("CartItemModel", back_populates="cart", cascade="all, delete-orphan")
    user = db.relationship("UserModel", back_populates="carts")
    order = db.relationship("OrderModel", back_populates="cart", cascade="all, delete", uselist=False)
    # methods
    def is_expired(self, time_now):
        if time_now > self.expire_date:
            self.is_active = False
            self.save()
        return time_now > self.expire_date
