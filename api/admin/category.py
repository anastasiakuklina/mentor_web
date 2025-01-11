from fastapi import APIRouter, Depends

from api.admin.dto import CategoryUpdateModel
from api.dependencies.admin import get_admin_category_service
from api.dependencies.common import get_pagination, get_category_sorting
from core.admin.category.dto import PaginatedCategoriesDTO, CategoriesGetDTO, CategorySortingDTO, CategoryCreateDTO, \
    CategoryUpdateDTO, CategoriesFindDTO
from core.admin.category.service import AdminCategoryService
from core.dto import PaginationDTO

router = APIRouter(
    prefix='/categories',
    tags=['admin/categories']
)


@router.get("", response_model=PaginatedCategoriesDTO)
async def get_categories(
        pagination: PaginationDTO = Depends(get_pagination),
        sorting: CategorySortingDTO = Depends(get_category_sorting),
        category_service: AdminCategoryService = Depends(get_admin_category_service)
        ):
    get_dto = CategoriesGetDTO(pagination=pagination,
                               sorting=sorting)
    return category_service.get_categories(get_dto)


@router.post("", response_model=int)
async def create_category(
        dto: CategoryCreateDTO,
        category_service: AdminCategoryService = Depends(get_admin_category_service)
        ):
    return category_service.create_category(dto)


@router.post("/{category_id}", response_model=None)
async def update_category(
        category_id: int,
        data: CategoryUpdateModel,
        category_service: AdminCategoryService = Depends(get_admin_category_service)
):
    dto = CategoryUpdateDTO(id=category_id, **data.model_dump())
    return category_service.update_categories(dto)


@router.get("/find", response_model=PaginatedCategoriesDTO)
async def find_categories(
        search_query: str,
        pagination: PaginationDTO = Depends(get_pagination),
        sorting: CategorySortingDTO = Depends(get_category_sorting),
        category_service: AdminCategoryService = Depends(get_admin_category_service)
        ):
    dto = CategoriesFindDTO(pagination=pagination, sorting=sorting,
                            search_query=search_query)
    return category_service.find_categories(dto)
