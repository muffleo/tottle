from pydantic import BaseModel

from tottle.types.responses.user import User


class ProximityAlertTriggered(BaseModel):
    traveler: User
    watcher: User
    distance: int
