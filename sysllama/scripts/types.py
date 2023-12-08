from pydantic import BaseModel
from datetime import datetime


class Response(BaseModel):
    prompt: str
    response: str
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
