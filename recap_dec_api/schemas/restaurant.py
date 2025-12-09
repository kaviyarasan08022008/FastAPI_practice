from pydantic import BaseModel

class Restaurant_schema(BaseModel):
    restaurant_name : str
    location : str
    rating : float
    online : bool