from fastapi import APIRouter, HTTPException
from models import User
from database import collection
from bson import ObjectId

router = APIRouter()

# Helper function to convert MongoDB documents
def serialize_user(user) -> dict:
    return {"id": str(user["_id"]), "name": user["name"], "email": user["email"], "age": user["age"]}

# Create User
@router.post("/", response_model=dict)
async def create_user(user: User):
    new_user = await collection.insert_one(user.dict())
    return {"id": str(new_user.inserted_id)}

# Get All Users
@router.get("/", response_model=list)
async def get_users():
    users = await collection.find().to_list(100)
    return [serialize_user(user) for user in users]

# Get Single User
@router.get("/{user_id}", response_model=dict)
async def get_user(user_id: str):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return serialize_user(user)

# Update User
@router.put("/{user_id}", response_model=dict)
async def update_user(user_id: str, user: User):
    result = await collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    return {"message": "User updated successfully"}

# Delete User
@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}