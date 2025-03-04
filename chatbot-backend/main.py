from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv
import uvicorn  # Ensure Uvicorn is imported

# Load environment variables from .env file
load_dotenv()

# Fetch API Key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ ERROR: GEMINI_API_KEY not found in environment variables.")

# Define the Gemini API endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Chatbot Backend is Running!"}

@app.get("/ask")
async def ask(query: str):
    try:
        # Construct request payload
        payload = {
            "contents": [{
                "parts": [{"text": query}]
            }]
        }
        
        # Send request to Gemini API
        headers = {"Content-Type": "application/json"}
        response = requests.post(API_URL, json=payload, headers=headers)
        
        # Check response
        if response.status_code == 200:
            data = response.json()
            return {"answer": data["candidates"][0]["content"]["parts"][0]["text"]}
        else:
            return {"error": response.json()}
    
    except Exception as e:
        return {"error": str(e)}

# ✅ Move Uvicorn run command AFTER API definitions
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080
    uvicorn.run(app, host="0.0.0.0", port=port)
