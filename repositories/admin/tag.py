from sqlalchemy import select, update, or_, func, asc, desc
from sqlalchemy.orm import sessionmaker

from core.admin.tag.dto import TagCreateRepoDTO, TagUpdateRepoDTO, TagListItemDTO, TagDetailDTO, TagsFindDTO, \
    PaginatedTagsDTO, TagsGetDTO
from core.admin.tag.repository import IAdminTagRepository
from repositories.base_repository import BaseRepository
from repositories.models.tag import Tag


class AdminTagRepository(BaseRepository, IAdminTagRepository):

    def create_tag(self, dto: TagCreateRepoDTO) -> int:
        with self.session_factory() as session:
            tag = Tag(**dto.model_dump())
            session.add(tag)
            session.commit()
            session.refresh(tag)
            return tag.id

    def get_tags(self, dto: TagsGetDTO) -> list[TagListItemDTO]:
        with self.session_factory() as session:
            stmt = select(Tag)

            stmt = self.add_order_by(stmt=stmt, sorting_dto=dto.sorting)
            tags_orm, count = self.paginate(stmt, dto.pagination)
            result = [TagListItemDTO.model_validate(row, from_attributes=True) for row in tags_orm]
            return result

    def get_tag(self, tag_id: int) -> TagDetailDTO:
        with self.session_factory() as session:
            tag = session.get(Tag, tag_id)
            return TagDetailDTO.model_validate(tag, from_attributes=True)

    def update_tag(self, dto: TagUpdateRepoDTO):
        with self.session_factory() as session:
            stmt = update(Tag).where(Tag.id == dto.id).values(**dto.model_dump(exclude_unset=True))
            session.execute(stmt)
            session.commit()

    def find_tags(self, dto: TagsFindDTO) -> PaginatedTagsDTO:
        stmt = select(Tag).where(or_(Tag.name.icontains(dto.search_query), Tag.slug.icontains(dto.search_query)))
        stmt = self.add_order_by(stmt=stmt, sorting_dto=dto.sorting)
        tags_orm, count = self.paginate(stmt, dto.pagination)
        tags = [TagListItemDTO.model_validate(row, from_attributes=True) for row in tags_orm]
        result = PaginatedTagsDTO(count=count, tags = tags)
        return result
