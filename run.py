import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)