from pydantic import BaseModel


class CategoryUpdateModel(BaseModel):
    slug: str
    name: str
