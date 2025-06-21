from fastapi import APIRouter, HTTPException, status
from ..models import UserIn, UserOut

router = APIRouter(prefix="/users", tags=["users"])


_fake_db: dict[int, UserOut] = {}  # memory‑only demo
_seq = 1


@router.post("/", response_model=UserOut, operation_id="create_user")
async def create_user(payload: UserIn):
    global _seq
    user = UserOut(id=_seq, email=payload.email, full_name=payload.full_name)
    _fake_db[_seq] = user
    _seq += 1
    return user


@router.get("/{user_id}", response_model=UserOut, operation_id="get_user")
async def get_user(user_id: int):
    user = _fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return user
