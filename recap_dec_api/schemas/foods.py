from pydantic import BaseModel

class foods_schema(BaseModel):
    food_name:str
    price:int
    qty:int
    availability:bool