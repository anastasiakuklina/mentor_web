from abc import ABC, abstractmethod

from .dto import ArticleCreateDTO, ArticleListItemDTO, ArticleDetailDTO, ArticleUpdateDTO, AdminArticleFilter, \
    PaginatedArticlesDTO
from ...dto import PaginationDTO


class IArticleRepository(ABC):

    @abstractmethod
    def create_article(self, dto: ArticleCreateDTO) -> int:
        pass

    @abstractmethod
    def get_articles(self, pagination_dto: PaginationDTO,
                     admin_filters: AdminArticleFilter | None = None) -> PaginatedArticlesDTO:
        pass

    @abstractmethod
    def get_article(self, slug: str) -> ArticleDetailDTO:
        pass

    @abstractmethod
    def update_article(self, dto: ArticleUpdateDTO) -> None:
        pass

    @abstractmethod
    def find_articles(self, pagination_dto: PaginationDTO, search_query: str) -> PaginatedArticlesDTO:
        pass

    @abstractmethod
    def is_slug_unique(self, slug: str) -> bool:
        pass

    @abstractmethod
    def get_article_by_id(self, article_id: int) -> ArticleDetailDTO:
        pass
