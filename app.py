from fastapi import FastAPI

from routes.upload import router as upload_router
from routes.download import router as download_router
from routes.files import router as file_router

app = FastAPI(
    title="x402-storage",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(download_router)
app.include_router(file_router)


@app.get("/")
def home():

    return {
        "service": "x402-storage",
        "status": "running"
    }
