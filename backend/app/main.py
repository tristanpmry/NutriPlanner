from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import nutrition

app = FastAPI(title="NutriPlanner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    nutrition.router,
    prefix="/nutrition",
    tags=["Nutrition"],
)


@app.get("/")
def root():
    return {"message": "NutriPlanner API running"}