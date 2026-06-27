from fastapi import APIRouter

router = APIRouter(
    prefix="/download",
    tags=["Download"]
)


@router.get("/{filename}")

def download(filename: str):

    return {

        "file": filename

    }
