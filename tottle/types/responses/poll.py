from typing import Optional, List

from pydantic import BaseModel, Field

from .user import User
from tottle.types.responses.entity import Entity


class PollAnswer(BaseModel):
    id: str = Field(alias="poll_id")
    user: User
    option_ids: Optional[List[int]] = None


class PollOption(BaseModel):
    text: str
    voter_count: int


class Poll(BaseModel):
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: Optional[int] = 0
    explanation: Optional[str] = ""
    explanation_entities: Optional[List[Entity]] = []
    open_period: Optional[int] = 0
    close_date: Optional[int] = 0

