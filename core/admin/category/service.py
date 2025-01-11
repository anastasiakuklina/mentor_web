from .dto import CategoryCreateDTO, CategoryDTO, CategoryUpdateDTO, CategoryFilters, PaginatedCategoriesDTO, \
    CategoriesFindDTO, CategoriesGetDTO
from .repository import IAdminCategoryRepository


class AdminCategoryService:
    def __init__(self, category_repo: IAdminCategoryRepository):
        self.category_repo = category_repo

    def create_category(self, dto: CategoryCreateDTO) -> int:
        return self.category_repo.create_category(dto)

    def get_categories(self, dto: CategoriesGetDTO) -> PaginatedCategoriesDTO:
        return self.category_repo.get_categories(dto)

    def update_categories(self, dto: CategoryUpdateDTO):
        self.category_repo.update_category(dto)

    def find_categories(self, dto: CategoriesFindDTO) -> PaginatedCategoriesDTO:
        return self.category_repo.find_categories(dto)
