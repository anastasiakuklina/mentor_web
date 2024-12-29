from abc import ABC, abstractmethod

from .dto import (ArticleCreateDTO, ArticleDetailDTO, ArticleUpdateDTO, PaginatedArticlesDTO, ArticlesGetDTO,
                  ArticlesFindDTO)


class IArticleRepository(ABC):

    @abstractmethod
    def create_article(self, dto: ArticleCreateDTO) -> int:
        pass

    @abstractmethod
    def get_articles(self, dto: ArticlesGetDTO) -> PaginatedArticlesDTO:
        pass

    @abstractmethod
    def get_article(self, slug: str) -> ArticleDetailDTO:
        pass

    @abstractmethod
    def update_article(self, dto: ArticleUpdateDTO) -> None:
        pass

    @abstractmethod
    def find_articles(self, dto: ArticlesFindDTO) -> PaginatedArticlesDTO:
        pass

    @abstractmethod
    def is_slug_unique(self, slug: str) -> bool:
        pass

    @abstractmethod
    def get_article_by_id(self, article_id: int) -> ArticleDetailDTO:
        pass
