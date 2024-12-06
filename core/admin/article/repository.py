from abc import ABC, abstractmethod

from .dto import ArticleCreateDTO, ArticleListItemDTO, ArticleDetailDTO, ArticleUpdateDTO, AdminArticleFilter


class IArticleRepository(ABC):

    @abstractmethod
    def create_article(self, dto: ArticleCreateDTO):
        pass

    @abstractmethod
    def get_articles(self, admin_filters: AdminArticleFilter | None = None) -> list[ArticleListItemDTO]:
        pass

    @abstractmethod
    def get_article(self, slug: str) -> ArticleDetailDTO:
        pass

    @abstractmethod
    def update_article(self, dto: ArticleUpdateDTO) -> ArticleDetailDTO:
        pass

    @abstractmethod
    def find(self, text: str):
        pass
