from core.blog.article.service import ArticleService


class ArticleController:

    def __init__(self, article_service: ArticleService):
        self.article_service = article_service

    def get_articles(self):
        return self.article_service.get_articles()

    def get_article(self, slug: str):
        article = self.article_service.get_article(slug)
        self.article_service.add_views(slug, num_views=1)
        return article
