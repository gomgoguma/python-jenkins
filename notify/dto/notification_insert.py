from pydantic import BaseModel

from config.reponse.response_model import BaseResponse


class NotificationInsert(BaseModel):
    user_id: int
    content: str


class NotificationInsertResponse(BaseResponse):
    class NotificationInsertData(BaseModel):
        notification_id: int

    data: NotificationInsertData

