
from sqlalchemy import Column, String, Float, Integer, Boolean, JSON
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    thumb_src = Column(String)
    thumb_alt = Column(String)
    title = Column(String, index=True)
    price = Column(Float)
    description = Column(String, nullable=True)
    color = Column(String, nullable=True)
    colors = Column(JSON, nullable=True)
    rating = Column(Float, nullable=True)
    reviews = Column(Integer, nullable=True)
    stock = Column(Boolean, default=True)
    images = Column(JSON, nullable=True)
    full_description = Column(String, nullable=True)
    highlights = Column(JSON, nullable=True)
    details = Column(String, nullable=True)
    sizes = Column(JSON, nullable=True)
    data = Column(JSON, nullable=True)
    featuresDetails = Column(JSON, nullable=True)

class Category(Base):
    __tablename__ = "categories"

    id = Column(String, primary_key=True, index=True)
    thumb_src = Column(String)
    title = Column(String, index=True)
    collection = Column(String)
