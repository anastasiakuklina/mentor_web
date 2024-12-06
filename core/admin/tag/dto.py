from pydantic import BaseModel


class TagCreateDTO(BaseModel):
    slug: str
    name: str


class TagDTO(BaseModel):
    slug: str
    name: str


class TagUpdateDTO(BaseModel):
    slug: str | None = None
    name: str | None = None


class TagFilters(BaseModel):
    name: str | None = None