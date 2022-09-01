from fastapi import APIRouter
from service.sql import Sql

router = APIRouter(tags=["data"], prefix='/data')

@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}

    
@router.get("/grp", summary="예제입니다.4")
async def data2(item_id: str):
    conn = Sql()
    
    temp = conn.go(item_id)
    return temp