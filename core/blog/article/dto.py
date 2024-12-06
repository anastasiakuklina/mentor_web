from pydantic import BaseModel


class ArticleListItemDTO(BaseModel):
    title: str
    category_id: int
    tag_ids: list[int]


class ArticleDetailDTO(BaseModel):
    title: str
    category_id: int
    tag_ids: list[int]


class CategoryTagFilter(BaseModel):
    tag_id: int | None = None
    category_id: int | None = None
