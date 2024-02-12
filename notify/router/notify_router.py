from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from database.database import get_db
from notify.dto.notification_insert import NotificationInsert
from notify.service.notify_service import *

router = APIRouter()

auth_scheme = HTTPBearer()


@router.get("/{user_id}", description="알림 조회", response_model=NotificationSearchResponse, tags=["Notify"])
def search(user_id: int
           , token: HTTPAuthorizationCredentials = Depends(auth_scheme)
           , db: Session = Depends(get_db)):
    return search_notification(user_id, token, db)


@router.post("", description="알림 등록 (테스트용)", response_model=NotificationInsertResponse, tags=["Notify"])
def insert(dto: NotificationInsert
           , token: HTTPAuthorizationCredentials = Depends(auth_scheme)
           , db: Session = Depends(get_db)):
    return insert_notification(dto, token, db)
