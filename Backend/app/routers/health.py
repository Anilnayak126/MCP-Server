from fastapi import APIRouter

router = APIRouter(tags=["meta"])


@router.get("/health", operation_id="check_health")
async def health():
    return {"status": "ok"}
