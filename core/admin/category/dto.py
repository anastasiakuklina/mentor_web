from datetime import datetime

from pydantic import BaseModel


class CategoryCreateDTO(BaseModel):
    slug: str
    name: str
    is_draft: bool = False


class CategoryDTO(BaseModel):
    id: int
    slug: str
    name: str
    is_draft: bool
    created_at: datetime

class CategoryUpdateDTO(BaseModel):
    id: int
    slug: str | None
    name: str


class CategoryFilters(BaseModel):
    name: str | None = None
