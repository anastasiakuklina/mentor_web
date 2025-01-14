import re
from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field, AfterValidator

from core.admin import CategoryDTO, TagListItemDTO
from core.dto import PaginationDTO, SortingDTO


def is_slug(slug: str) -> str:
    pattern = r"^[a-z0-9-]+$"
    if not re.fullmatch(pattern, slug):
        raise ValueError(
            "Slug must contain only lowercase letters, numbers, and hyphens."
        )
    return slug


class ArticleCreateDTO(BaseModel):
    image: bytes
    title: str = Field(min_length=5, max_length=40)
    slug: Annotated[str, AfterValidator(is_slug)]
    text: str = Field(min_length=1)
    text_images: dict[str, bytes]
    category_id: int
    tag_ids: list[int]
    author_id: UUID
    publish_at: datetime
    is_draft: bool = Field(False)


class ArticleCreateRepoDTO(BaseModel):
    image: str
    title: str = Field(min_length=5, max_length=40)
    slug: Annotated[str, AfterValidator(is_slug)]
    text: str = Field(min_length=1)
    category_id: int
    tag_ids: list[int]
    author_id: UUID
    publish_at: datetime
    is_draft: bool = Field(False)



class ArticleListItemDTO(BaseModel):
    id: int
    title: str
    slug: str
    category: CategoryDTO
    tags: list[TagListItemDTO]
    publish_at: datetime
    created_at: datetime
    is_draft: bool
    num_views: int
    num_comments: int
    num_likes: int
    num_dislikes: int


class AdminArticleFilter(BaseModel):
    likes_min: int | None = None
    likes_max: int | None = None
    dislikes_min: int | None = None
    dislikes_max: int | None = None


class ArticleSortingDTO(SortingDTO):
    valid_fields: list[str] = Field(
        (
            "id",
            "title",
            "slug",
            "category",
            "author",
            "tag",
            "views",
            "comments",
            "likes",
            "dislikes",
            "created_at",
            "publish_at",
            "is_draft",
        )
    )


class ArticlesGetDTO(BaseModel):
    pagination: PaginationDTO
    sorting: ArticleSortingDTO
    filters: AdminArticleFilter


class ArticlesFindDTO(BaseModel):
    pagination: PaginationDTO
    sorting: ArticleSortingDTO
    search_query: str


class PaginatedArticlesDTO(BaseModel):
    articles: list[ArticleListItemDTO]
    count: int


class ArticleDetailDTO(BaseModel):
    id: int
    image: str
    title: str
    slug: Annotated[str, AfterValidator(is_slug)]
    text: str
    category: CategoryDTO
    tags: list[TagListItemDTO]
    author_id: UUID
    publish_at: datetime
    created_at: datetime
    is_draft: bool
    num_views: int
    num_comments: int
    num_likes: int
    num_dislikes: int


class ArticleUpdateDTO(BaseModel):
    id: int
    image: bytes | None = Field(None)
    title: str = Field(min_length=5, max_length=40)
    slug: Annotated[str, AfterValidator(is_slug)]
    text: str = Field(min_length=1)
    text_images: dict[str, bytes] | None = Field(None)
    category_id: int
    tag_ids: list[int]
    author_id: UUID
    publish_at: datetime
    is_draft: bool


class ArticleUpdateRepoDTO(BaseModel):
    id: int
    image: str
    title: str = Field(min_length=5, max_length=40)
    slug: Annotated[str, AfterValidator(is_slug)]
    text: str = Field(min_length=1)
    category_id: int
    tag_ids: list[int]
    author_id: UUID
    publish_at: datetime
    is_draft: bool
