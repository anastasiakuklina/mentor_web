from fastapi import Query

from core.admin.category.dto import CategorySortingDTO
from core.dto import PaginationDTO


async def get_pagination(limit: int = Query(default=20, ge=0, le=100), offset: int = 0) -> PaginationDTO:
    return PaginationDTO(offset=offset, limit=limit)


async def get_category_sorting(sort_by: str = Query(default="name"), sort_order: str = Query(default="asc")):
    return CategorySortingDTO(
        sort_by=sort_by,
        sort_order=sort_order
    )