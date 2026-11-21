from sqlalchemy import Column, Integer, String
from src.models.settings.metadata import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    age = Column(Integer)
    uf = Column(String)