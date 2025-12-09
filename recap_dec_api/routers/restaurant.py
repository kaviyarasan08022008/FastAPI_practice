from fastapi import APIRouter ,FastAPI , Depends
from sqlalchemy.orm import Session
from schemas.restaurant import Restaurant_schema
from models.restaurant import Restaurant
from dependencies import connect_to_db
restaurant_router = APIRouter(prefix="/restaurant", tags=["restaurant"])

#get all restaurant
@restaurant_router.get("/")
def get_all_restaurant(dbs:Session=Depends(connect_to_db)):
    restaurant = dbs.query(Restaurant).all()
    return restaurant

#get restaurant by id
@restaurant_router.get("/{id}")
def get_restaurant_by_id(id:int, dbs:Session = Depends(connect_to_db)):
    rest = dbs.query(Restaurant).filter(Restaurant.id == id).first()
    if not rest:
        return {"message":f"not {id} found"}
    return rest

#post add restaurant
@restaurant_router.post("/")
def post_restaurant(new_rest:Restaurant_schema, dbs:Session = Depends(connect_to_db)):
    new_entry = Restaurant(
        restaurant_name = new_rest.restaurant_name,
        location = new_rest.location,
        rating = new_rest.rating,
        online = new_rest.online
    )
    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)
    return {"message": f"restaurent added {new_entry}"}

@restaurant_router.put("/{id}")
def edit_restaurent(id:int, rest_upd:Restaurant_schema, dbs:Session = Depends(connect_to_db)):
    rest = dbs.query(Restaurant).filter(Restaurant.id == id).first()
    if not rest:
        return {"message":"food not found"}
    rest.restaurant_name = rest_upd.restaurant_name
    rest.location = rest_upd. location
    rest.rating = rest_upd. rating
    rest.online = rest_upd.online
    dbs.commit()
    dbs.refresh(rest)
    
@restaurant_router.delete("/{id}")
def delete_restaurant(id:int, dbs:Session = Depends(connect_to_db)):
    rest = dbs.query(Restaurant).filter(Restaurant.id == id).first()
    if not rest:
        return {"message":"restaurent not found"}
    dbs.delete(rest)
    dbs.commit()
    return {"message": "food deleted"}