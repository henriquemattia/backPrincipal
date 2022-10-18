from database.database import Base, engine, session
from sqlalchemy import Column, String, Integer
# from models.products import ProductsModel


class UsersModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
