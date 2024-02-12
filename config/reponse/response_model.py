from typing import Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    statusCode: int
    message: str
