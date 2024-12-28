from pydantic import BaseModel


class CategoryCreateDTO(BaseModel):
    slug: str
    name: str


class CategoryDTO(BaseModel):
    id: int
    slug: str
    name: str


class CategoryUpdateDTO(BaseModel):
    id: int
    slug: str | None = None
    name: str | None = None


class CategoryFilters(BaseModel):
    name: str | None = None