from pydantic import BaseModel


class MainPageDTO(BaseModel):
    title: str
    description: str
    contact: str
    contact_link: str
