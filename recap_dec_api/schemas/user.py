from pydantic import BaseModel

class User_schema(BaseModel):
    customer_name = str
    contact_no = str
    email = str
    location = str