from sqlalchemy import Column, Integer , String , Boolean , Float
from db.database import Base

class Restaurant(Base):
    __tablename__ = "restaurant"
    
    id = Column(Integer, primary_key=True, index=True)
    restaurant_name = Column(String)
    location = Column(String)
    rating = Column(Float)
    online = Column(Boolean)