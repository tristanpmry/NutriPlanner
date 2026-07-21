from fastapi import FastAPI


app = FastAPI(
    title="NutriPlanner API"
)


@app.get("/")
def root():

    return {
        "message": "NutriPlanner API running"
    }