from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from notify.dto.notification_insert import NotificationInsert, NotificationInsertResponse
from notify.model.models import Notification
from datetime import datetime

from config.reponse.response_model import BaseResponse
from config.reponse.reponse_const import *
from notify.dto.notification_search import NotificationSearchResponse

import logging

# 로그 설정
logging.basicConfig(level=logging.INFO)  # 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)


def search_notification(user_id: int, token: HTTPAuthorizationCredentials, db: Session):
    rows = db.query(Notification).filter(Notification.user_id == user_id).all()

    if not rows:
        response = NotificationSearchResponse(statusCode=NOT_FOUND, message="알림이 없습니다.", data=None)
    else:
        data_list = []
        for n in rows:
            data_list.append(NotificationSearchResponse.NotificationSearchData(**n.__dict__))

        response = NotificationSearchResponse(statusCode=OK, message="Success", data=data_list)
    return response


def insert_notification(dto: NotificationInsert, token: HTTPAuthorizationCredentials, db: Session):
    try:
        new_notification = Notification(user_id=dto.user_id, content=dto.content, reg_dtm=datetime.now())
        db.add(new_notification)
        db.commit()
        db.refresh(new_notification)

        response = NotificationInsertResponse(statusCode=CREATED, message="Success", data=NotificationInsertResponse.NotificationInsertData(notification_id=new_notification.notification_id))
    except Exception as e:
        logging.error("Exception during notification insert: %s", str(e), exc_info=True)
        response = BaseResponse(statusCode=SERVER_ERROR, message="저장에 실패하였습니다.")

    return response
