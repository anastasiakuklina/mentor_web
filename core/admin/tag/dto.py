from pydantic import BaseModel


class TagCreateDTO(BaseModel):
    slug: str
    name: str


class TagDTO(BaseModel):
    id: int
    slug: str
    name: str


class TagUpdateDTO(BaseModel):
    id: int
    slug: str | None = None
    name: str | None = None


class TagFilters(BaseModel):
    name: str | None = None
