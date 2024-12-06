from uuid import UUID

from pydantic import BaseModel


class ToggleLikeDTO(BaseModel):
    article_slug: str
    user_id: UUID
    is_set: bool

class ToggleDislikeDTO(ToggleLikeDTO):
    pass