from fastapi import APIRouter

router = APIRouter()


# /api/events/
@router.get("/")
def read_events():
    return {
        "results": [1,2,3]
    }