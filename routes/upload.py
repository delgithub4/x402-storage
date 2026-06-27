from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_file(
    file: UploadFile = File(...)
):

    return {

        "filename": file.filename,

        "content_type": file.content_type

    }
