from fastapi import APIRouter

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.get("/")

def files():

    return {

        "files": []

    }
