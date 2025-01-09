from abc import ABC, abstractmethod

from .dto import TagCreateRepoDTO, TagUpdateRepoDTO, TagListItemDTO, TagDetailDTO, TagsFindDTO, TagsGetDTO


class IAdminTagRepository(ABC):
    @abstractmethod
    def create_tag(self, dto: TagCreateRepoDTO) -> int:
        pass

    @abstractmethod
    def get_tags(self, dto: TagsGetDTO) -> list[TagListItemDTO]:
        pass

    @abstractmethod
    def get_tag(self, tag_id: int) -> TagDetailDTO:
        pass

    @abstractmethod
    def update_tag(self, dto: TagUpdateRepoDTO):
        pass

    @abstractmethod
    def find_tags(self, dto: TagsFindDTO) -> list[TagListItemDTO]:
        pass
