from .dto import TagCreateDTO, TagDTO, TagUpdateDTO, TagFilters
from .repository import ITagRepository


class TagService:

    def __init__(self, tag_repo: ITagRepository):
        self.tag_repo = tag_repo

    def create_tag(self, dto: TagCreateDTO):
        self.tag_repo.create_tag(dto)

    def get_categories(self, dto: TagFilters) -> list[TagDTO]:
        return self.tag_repo.get_tags(dto)

    def update_categories(self, dto: TagUpdateDTO):
        self.tag_repo.update_tag(dto)
