from abc import ABC, abstractmethod

from .dto import CategoryCreateDTO, CategoryDTO, CategoryUpdateDTO, CategoryFilters, CategoriesGetDTO, \
    PaginatedCategoriesDTO, CategoriesFindDTO


class IAdminCategoryRepository(ABC):
    @abstractmethod
    def create_category(self, dto: CategoryCreateDTO) -> int:
        pass

    @abstractmethod
    def get_categories(self, dto: CategoriesGetDTO) -> PaginatedCategoriesDTO:
        pass

    @abstractmethod
    def update_category(self, dto: CategoryUpdateDTO):
        pass

    @abstractmethod
    def find_categories(self, dto: CategoriesFindDTO) -> PaginatedCategoriesDTO:
        pass
