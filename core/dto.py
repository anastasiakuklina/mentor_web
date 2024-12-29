from typing import Optional, Literal, Annotated

from pydantic import BaseModel, Field, model_validator


class PaginationDTO(BaseModel):
    limit: int = 20
    offset: int = 0


class SortingDTO(BaseModel):
    sort_by: Optional[str] =  Field(None)
    sort_order: Annotated[Literal["asc", "desc"], Field("asc")]
    valid_fields: list[str] = Field(None)

    @model_validator(mode="after")
    def validate_sorting(self):
        sort_by = self.sort_by
        valid_fields = self.valid_fields

        if sort_by and sort_by not in valid_fields:
            raise ValueError(f"Invalid sort field: '{sort_by}'. Valid fields are: {', '.join(valid_fields)}")
        return self
