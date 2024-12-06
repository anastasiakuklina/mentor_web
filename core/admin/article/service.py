from .dto import ArticleCreateDTO, ArticleListItemDTO, ArticleUpdateDTO, ArticleDetailDTO, AdminArticleFilter
from .repository import IArticleRepository


class AdminArticleService:

    def __init__(self, article_repo: IArticleRepository):
        self.article_repo = article_repo

    def create_article(self, dto: ArticleCreateDTO):
        self.article_repo.create_article(dto)

    def get_articles(self, filters: AdminArticleFilter | None = None) -> list[ArticleListItemDTO]:
        return self.article_repo.get_articles(admin_filters=filters)

    def get_article(self, slug: str) -> ArticleDetailDTO:
        return self.article_repo.get_article(slug)

    def edit_article(self, dto: ArticleUpdateDTO):
        return self.article_repo.update_article(dto)

    def find(self, text: str):
        return self.article_repo.find(text)
