from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# List of Paw Patrol characters
paw_patrol_characters = [
    'Chase',
    'Marshall',
    'Skye',
    'Rubble',
    'Zuma',
    'Rocky',
    'Everest',
    'Tracker',
    'Ryder'
]

@app.get("/")
def read_root():
    return "Why are you here?"

@app.get("/pawpatrol")
def get_pawpatrol_character():
    random_character = random.choice(paw_patrol_characters)
    return {"character": random_character}

# To run the app, use: uvicorn main:app --host 0.0.0.0 --port 3001
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
