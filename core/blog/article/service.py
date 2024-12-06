from .dto import ArticleListItemDTO, ArticleDetailDTO, CategoryTagFilter
from .repository import IPublishedArticleRepository


class ArticleService:
    def __init__(self, article_repo: IPublishedArticleRepository):
        self.article_repo = article_repo

    def get_articles(self, filters: CategoryTagFilter | None = None) -> list[ArticleListItemDTO]:
        return self.article_repo.get_articles(filters=filters)

    def get_article(self, slug: str) -> ArticleDetailDTO:
        return self.article_repo.get_article(slug)

    def find(self, text: str) -> list[ArticleListItemDTO]:
        return self.article_repo.find(text)

    def add_views(self, slug: str, num_views: int) -> None:
        self.article_repo.add_views(slug, num_views)