from pydantic import BaseModel

class Order_schema(BaseModel):
    total_amount: int
    user_id: int
    rest_id: int
