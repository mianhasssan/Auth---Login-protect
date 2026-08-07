from fastapi import FastAPI
from protected import router as protected_router
import uvicorn

from auth import router
from config import PORT

app = FastAPI(
    title="FlyRank Authentication API",
    version="1.0.0"
)

app.include_router(router)
app.include_router(protected_router)


@app.get("/")
def home():
    return {
        "message": "FlyRank Authentication API is running."
    }


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=PORT,
        reload=True
    )