from .dto import TagCreateDTO, TagUpdateDTO, TagsGetDTO, PaginatedTagsDTO, TagsFindDTO
from .repository import IAdminTagRepository


class AdminTagService:
    def __init__(self, tag_repo: IAdminTagRepository):
        self.tag_repo = tag_repo

    def create_tag(self, dto: TagCreateDTO) -> int:
        return self.tag_repo.create_tag(dto)

    def get_tags(self, dto: TagsGetDTO) -> PaginatedTagsDTO:
        return self.tag_repo.get_tags(dto)

    def update_tag(self, dto: TagUpdateDTO):
        self.tag_repo.update_tag(dto)

    def find_tags(self, dto: TagsFindDTO) -> PaginatedTagsDTO:
        return self.tag_repo.find_tags(dto)
