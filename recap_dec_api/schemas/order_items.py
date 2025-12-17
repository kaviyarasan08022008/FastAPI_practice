from sqlalchemy import BaseModel

class OrderItems_schema(BaseModel):
    quantity: int
    order_id: int
    food_id: int