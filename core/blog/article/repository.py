from abc import ABC, abstractmethod

from .dto import ArticleListItemDTO, ArticleDetailDTO, CategoryTagFilter


class IPublishedArticleRepository(ABC):

    @abstractmethod
    def get_articles(self, filters: CategoryTagFilter | None = None) -> list[ArticleListItemDTO]:
        pass

    @abstractmethod
    def get_article(self, slug: str) -> ArticleDetailDTO:
        pass

    @abstractmethod
    def find_articles(self, search_query: str) -> list[ArticleListItemDTO]:
        pass

    @abstractmethod
    def add_views(self, slug: str, num_view: int):
        pass
