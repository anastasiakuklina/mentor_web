from pydantic import BaseModel


class ExternalResourceDTO(BaseModel):
    description: str
    link: str
