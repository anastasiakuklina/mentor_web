from abc import ABC, abstractmethod

from .dto import TagCreateDTO, TagDTO, TagUpdateDTO, TagFilters


class ITagRepository(ABC):

    @abstractmethod
    def create_tag(self, dto: TagCreateDTO):
        pass

    @abstractmethod
    def get_tags(self, dto: TagFilters) -> list[TagDTO]:
        pass

    @abstractmethod
    def update_tag(self, dto: TagUpdateDTO):
        pass
