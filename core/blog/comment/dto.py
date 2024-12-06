from uuid import UUID

from pydantic import BaseModel


class CommentCreateDTO(BaseModel):
    article_id: UUID
    author_id: UUID
    text: str


class SubCommentCreateDTO(BaseModel):
    comment_id: UUID
    author_id: UUID
    text: str


class CommentDetailDTO(BaseModel):
    id: UUID
    text: str


class CommentListItemDTO(BaseModel):
    id: UUID
    text: str