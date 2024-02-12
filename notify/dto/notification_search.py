from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from config.reponse.response_model import BaseResponse


class NotificationSearchResponse(BaseResponse):
    class NotificationSearchData(BaseModel):
        notification_id: int
        user_id: int
        content: str
        reg_dtm: datetime

    data: Optional[List[NotificationSearchData]] = None
