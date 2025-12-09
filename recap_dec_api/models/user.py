from sqlalchemy import String, Column, Integer
from db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    contact_no = Column(String)
    email = Column(String)
    location = Column(String)
    