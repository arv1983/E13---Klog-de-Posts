from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
from app.config.db import db




class productModel(db.Model):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(300), nullable=False)
    author = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)