from .dto import CategoryCreateDTO, CategoryDTO, CategoryUpdateDTO, CategoryFilters
from .repository import ICategoryRepository


class CategoryService:
    def __init__(self, category_repo: ICategoryRepository):
        self.category_repo = category_repo

    def create_category(self, dto: CategoryCreateDTO):
        self.category_repo.create_category(dto)

    def get_categories(self, dto: CategoryFilters) -> list[CategoryDTO]:
        return self.category_repo.get_categories(dto)

    def update_categories(self, dto: CategoryUpdateDTO):
        self.category_repo.update_category(dto)
