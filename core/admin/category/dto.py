from datetime import datetime

from pydantic import BaseModel, Field

from core.dto import PaginationDTO, SortingDTO


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


class PaginatedCategoriesDTO(BaseModel):
    categories: list[CategoryDTO]
    count: int

class CategorySortingDTO(SortingDTO):
    valid_fields: list[str] = Field(("id", "name", "slug", "created_at"))


class CategoriesGetDTO(BaseModel):
    pagination: PaginationDTO
    sorting: CategorySortingDTO


class CategoriesFindDTO(BaseModel):
    pagination: PaginationDTO
    sorting: CategorySortingDTO
    search_query: str

