from pydantic import BaseModel


class OfferingDTO(BaseModel):
    id: int
    title: str
    description: str
    price: float

class OfferingDetailDTO(BaseModel):
    id: int
    title: str
    description: str
    detailed_description: str
    price: float
