from pydantic import BaseModel, Field

from core.dto import PaginationDTO, SortingDTO


class TagCreateDTO(BaseModel):
    slug: str
    name: str
    icon: bytes


class TagCreateRepoDTO(BaseModel):
    slug: str
    name: str
    icon_base64: str


class TagListItemDTO(BaseModel):
    id: int
    slug: str
    name: str


class TagDetailDTO(BaseModel):
    id: int
    slug: str
    name: str
    icon_base64: str


class PaginatedTagsDTO(BaseModel):
    count: int
    tags: list[TagListItemDTO]


class TagUpdateDTO(BaseModel):
    id: int
    slug: str
    name: str
    icon: bytes | None = None


class TagUpdateRepoDTO(BaseModel):
    id: int
    slug: str
    name: str
    icon_base64: str | None = None


class TagSortingDTO(SortingDTO):
    valid_fields: list[str] = Field(("id", "name", "slug", "created_at"))


class TagsFindDTO(BaseModel):
    pagination: PaginationDTO
    sorting: TagSortingDTO
    search_query: str


class TagsGetDTO(BaseModel):
    pagination: PaginationDTO
    sorting: TagSortingDTO
