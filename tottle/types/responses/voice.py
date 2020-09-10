from typing import Optional

from pydantic import BaseModel


class Voice(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: Optional[int] = 0

    duration: int
    mime_type: Optional[str] = ""
