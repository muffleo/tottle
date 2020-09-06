from pydantic import BaseModel
from typing import Optional, List

from tottle.types.objects.message import MessageEntity


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
    explanation_entities: Optional[List[MessageEntity]] = []
    open_period: Optional[int] = 0
    close_date: Optional[int] = 0

