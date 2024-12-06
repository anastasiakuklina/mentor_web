from pydantic import BaseModel


class AboutDTO(BaseModel):
    texts: list[str]
