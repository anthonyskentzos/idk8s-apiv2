from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
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
    return {"message": "Why are you here?"}

@app.get("/pawpatrol")
def get_pawpatrol_character():
    random_character = random.choice(paw_patrol_characters)
    return {"character": random_character}

@app.get("/imagetag")
async def version():
    image_tag = os.getenv("IMAGE_TAG", "IMAGE_TAG not set")
    return {"imageTagVer": image_tag}

# To run the app, use: uvicorn main:app --host 0.0.0.0 --port 3001
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
