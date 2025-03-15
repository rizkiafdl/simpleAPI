from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://rizki_test:muhammadrizkiafdolli@rizkidb.lcdp1.mongodb.net/?retryWrites=true&w=majority&appName=RizkiDB"

async def test_connection():
    client = AsyncIOMotorClient(MONGO_URI)
    try:
        await client.admin.command("ping")
        print("✅ Connected to MongoDB Atlas!")
    except Exception as e:
        print("❌ Connection failed:", e)

import asyncio
asyncio.run(test_connection())