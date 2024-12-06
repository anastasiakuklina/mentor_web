from abc import ABC, abstractmethod

from core.admin.category.dto import CategoryCreateDTO, CategoryDTO, CategoryUpdateDTO, CategoryFilters


class ICategoryRepository(ABC):

    @abstractmethod
    def create_category(self, dto: CategoryCreateDTO):
        pass

    @abstractmethod
    def get_categories(self, dto: CategoryFilters) -> list[CategoryDTO]:
        pass

    @abstractmethod
    def update_category(self, dto: CategoryUpdateDTO):
        pass
