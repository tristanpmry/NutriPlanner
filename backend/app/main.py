from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import nutrition

app = FastAPI(
    title="NutriPlanner API"
)

app.include_router(
    nutrition.router,
    prefix="/nutrition",
    tags=["nutrition"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message":"NutriPlanner API running"
    }


@app.get("/test")
def test():
    return {
        "status":"ok",
        "message":"Backend connected"
    }