from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from core.admin.category.dto import CategoryCreateDTO, CategoryFilters, CategoryDTO, CategoryUpdateDTO
from core.admin.category.repository import IAdminCategoryRepository
from repositories.models.category import Category


class AdminCategoryRepository(IAdminCategoryRepository):

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def create_category(self, dto: CategoryCreateDTO) -> int:
        with self.session_factory() as session:
            category = Category(**dto.model_dump())
            session.add(category)
            session.commit()
            session.refresh(category)
            return category.id

    def get_categories(self, dto: CategoryFilters | None = None) -> list[CategoryDTO]:
        with self.session_factory() as session:
            stmt = select(Category)
            result_orm = session.execute(stmt).scalars().all()
            result = [CategoryDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result


    def update_category(self, dto: CategoryUpdateDTO):
        with self.session_factory() as session:
            stmt = update(Category).where(Category.id == dto.id).values(**dto.model_dump(exclude_unset=True))
            session.execute(stmt)
            session.commit()
