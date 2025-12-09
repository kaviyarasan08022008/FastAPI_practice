from fastapi import APIRouter ,FastAPI , Depends
from sqlalchemy.orm import Session
from schemas.user import User_schema
from models.user import User
from dependencies import connect_to_db
User_router = APIRouter(prefix="/user", tags=["user"])

#get all users
@User_router.get("/")
def get_all_Users(dbs:Session=Depends(connect_to_db)):
    user = dbs.query(User).all()
    return user

#get users by id
@User_router.get("/{id}")
def get_user_by_id(id:int, dbs:Session = Depends(connect_to_db)):
    user = dbs.query(User).filter(User.id == id).first()
    if not user:
        return {"message":f"not {id} found"}
    return user

#post add User
@User_router.post("/")
def post_user(new_user:User_schema, dbs:Session = Depends(connect_to_db)):
    new_entry = User(
        cust_name = new_user.customer_name,
        contact_no = new_user.contact_no,
        email = new_user.email,
        location = new_user.location
    )
    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)
    return {"message": f"user added {new_entry}"}

@User_router.put("/{id}")
def edit_user(id:int, user_upd:User_schema, dbs:Session = Depends(connect_to_db)):
    user = dbs.query(User).filter(User.id == id).first()
    if not user:
        return {"message":"food not found"}
    user.customer_name = user_upd.customer_name
    user.contact_no = user_upd.contact_no
    user.email = user_upd. email
    user.location = user_upd.location
    dbs.commit()
    dbs.refresh(user)
    
@User_router.delete("/{id}")
def delete_user(id:int, dbs:Session = Depends(connect_to_db)):
    user = dbs.query(User).filter(User.id == id).first()
    if not user:
        return {"message":"user not found"}
    dbs.delete(user)
    dbs.commit()
    return {"message": "user deleted"}