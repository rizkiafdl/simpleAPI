from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

MONGO_URI = "mongodb+srv://rizki_test:muhammadrizkiafdolli@rizkidb.lcdp1.mongodb.net/?retryWrites=true&w=majority&appName=RizkiDB"
client = AsyncIOMotorClient(MONGO_URI)
db = client["user_database"]
collection = db["users"]