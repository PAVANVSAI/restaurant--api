from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Restaurant
from schemas import RestaurantCreate, RestaurantUpdate
from auth_helper import get_current_user

router = APIRouter()
cache={}
@router.get("/restaurants")
def get_restaurants(db:Session=Depends(get_db)):
    if "restaurants" in cache:
        print("Cache hit-not touching database")
        return {"restaurants":cache["restaurants"],"source":"cache"}
    print("Cache miss-reading from database")
    data=db.query(Restaurant).all()
    cache["restaurants"]=[{'id':r.id,'name':r.name,'rating':r.rating} for r in data]
    return {"restaurants":cache["restaurants"],"source":"database"}


# POST add new restaurant
@router.post("/restaurants")
def add_restaurant(data: RestaurantCreate, db: Session = Depends(get_db),user_id:int=Depends(get_current_user)):
    new = Restaurant(name=data.name, rating=data.rating)
    db.add(new)
    db.commit()
    return {"message": f"Restaurant added by User {user_id}"}

# PUT update rating
@router.put("/restaurants/{restaurant_id}")
def update_rating(restaurant_id: int, data: RestaurantUpdate, db: Session = Depends(get_db),user_id:int=Depends(get_current_user)):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404,detail="Restaurant not found!")
    restaurant.rating = data.rating
    db.commit()
    cache.clear()
    return {"message": "Rating updated!", "new_rating": data.rating}

# DELETE remove restaurant
@router.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db),user_id:int=Depends(get_current_user)):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404,detail="Restaurant not found!")
    db.delete(restaurant)
    db.commit()
    cache.clear()
    return {"message": "Restaurant deleted!"}