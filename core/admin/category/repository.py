from abc import ABC, abstractmethod

from .dto import CategoryCreateDTO, CategoryDTO, CategoryUpdateDTO, CategoryFilters


class IAdminCategoryRepository(ABC):
    @abstractmethod
    def create_category(self, dto: CategoryCreateDTO) -> int:
        pass

    @abstractmethod
    def get_categories(self, dto: CategoryFilters) -> list[CategoryDTO]:
        pass

    @abstractmethod
    def update_category(self, dto: CategoryUpdateDTO):
        pass
