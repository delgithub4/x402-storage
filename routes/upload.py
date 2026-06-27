from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.storage_service import StorageService
from services.validator import FileValidator
router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

storage = StorageService()
validator = FileValidator()

@router.post("/")
async def upload_file(
    file: UploadFile = File(...)
):

    content = await file.read()

    valid, message = validator.validate(
        file,
        len(content)
    )
    
    if not valid:
    
        return {
            "success": False,
            "message": message
        }
    
    location = storage.upload(
        file.filename,
        content
    )

    return {

        "success": True,

        "file": location
    }
