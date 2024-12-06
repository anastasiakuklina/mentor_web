from pydantic import BaseModel


class ArticleCreateDTO(BaseModel):
    title: str
    category_id: int
    tag_ids: list[int]


class ArticleListItemDTO(BaseModel):
    title: str
    category_id: int
    tag_ids: list[int]


class ArticleDetailDTO(BaseModel):
    title: str
    category_id: int
    tag_ids: list[int]

class ArticleUpdateDTO(BaseModel):
    title: str
    category_id: int
    tag_ids: list[int]


class AdminArticleFilter(BaseModel):
    likes_min: int | None = None
    likes_max: int | None = None
    dislikes_min: int | None = None
    dislikes_max: int | None = None
