from typing import List
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Add this import

from app import services
from app.schema import UserIn, BaseResponse, UserListOut

app = FastAPI()

# Add CORS middleware - Add this section
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://192.168.254.144", 
        "https://fusionpact-devops-challenge-z5yk.onrender.com",
        "https://fusionpact-frontend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app, endpoint="/metrics")


@app.get("/")
async def index():
    """
    Index route for our application
    """
    return {"message": "Hello from FastAPI -@kiranrakh155@gmail.com ;)"}


@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    """
    Add user data to json file
    """
    try:
        services.add_userdata(user.dict())
    except:
        return {"success": False}
    return {"success": True}


@app.get("/users", response_model=UserListOut)
async def get_users():
    """
    Read user data from json file
    """
    return services.read_usersdata()
