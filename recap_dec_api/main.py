from fastapi import FastAPI
from db.database import Base, engine
from routers.foods import food_router
from routers.restaurant import restaurant_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(food_router)
app.include_router(restaurant_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
