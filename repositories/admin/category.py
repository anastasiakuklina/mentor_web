from sqlalchemy import select, update, or_

from core.admin.category.dto import CategoryCreateDTO, CategoryDTO, CategoryUpdateDTO, \
    CategoriesGetDTO, PaginatedCategoriesDTO, CategoriesFindDTO
from core.admin.category.repository import IAdminCategoryRepository
from repositories.base_repository import BaseRepository
from repositories.models.category import Category


class AdminCategoryRepository(BaseRepository, IAdminCategoryRepository):

    def create_category(self, dto: CategoryCreateDTO) -> int:
        category = Category(**dto.model_dump())
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        return category.id

    def get_categories(self, dto: CategoriesGetDTO) -> PaginatedCategoriesDTO:
        stmt = select(Category)
        stmt = self.add_order_by(stmt=stmt, sorting_dto=dto.sorting)
        result_orm, count = self.paginate(stmt, dto.pagination)
        result = [CategoryDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return PaginatedCategoriesDTO(count=count, categories=result)


    def update_category(self, dto: CategoryUpdateDTO):
        stmt = update(Category).where(Category.id == dto.id).values(**dto.model_dump(exclude_unset=True))
        self.session.execute(stmt)
        self.session.commit()


    def find_categories(self, dto: CategoriesFindDTO) -> PaginatedCategoriesDTO:
        stmt = select(Category).where(or_(Category.name.icontains(dto.search_query),
                                          Category.slug.icontains(dto.search_query)))
        stmt = self.add_order_by(stmt=stmt, sorting_dto=dto.sorting)
        result_orm, count = self.paginate(stmt, dto.pagination)
        result = [CategoryDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return PaginatedCategoriesDTO(count=count, categories=result)
