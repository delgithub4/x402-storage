from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.storage_service import StorageService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

storage = StorageService()


@router.post("/")
async def upload_file(
    file: UploadFile = File(...)
):

    content = await file.read()

    location = storage.upload(
        file.filename,
        content
    )

    return {

        "filename": file.filename,

        "location": location,

        "status": "uploaded"

    }
