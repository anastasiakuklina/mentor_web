from result import Result, Err, Ok

from .commands.create_article_command import CreateArticleCommand
from .commands.update_article_command import UpdateArticleCommand
from .dto import ArticleCreateDTO, ArticleUpdateDTO, ArticleDetailDTO, AdminArticleFilter, \
    PaginatedArticlesDTO
from .exceptions import ArticleNotFoundError
from .repository import IArticleRepository
from core.file.protocol import FileServiceProtocol
from ...dto import PaginationDTO


class AdminArticleService:


    def __init__(self, article_repo: IArticleRepository, file_service: FileServiceProtocol):
        self.article_repo = article_repo
        self.file_service = file_service

    def create_article(self, dto: ArticleCreateDTO) -> Result[int, Exception]:
        return CreateArticleCommand(self.article_repo, self.file_service).create_article(dto)

    def get_articles(self, pagination_dto: PaginationDTO,
                     filters: AdminArticleFilter | None = None) -> PaginatedArticlesDTO:
        return self.article_repo.get_articles(pagination_dto, admin_filters=filters)

    def get_article(self, slug: str) -> Result[ArticleDetailDTO, Exception]:
        article =  self.article_repo.get_article(slug)
        if not article:
            return Err(ArticleNotFoundError())
        return Ok(article)

    def update_article(self, dto: ArticleUpdateDTO) -> Result[None, Exception]:
        return UpdateArticleCommand(self.article_repo, self.file_service).update_article(dto)

    def find_articles(self, pagination_dto: PaginationDTO, search_query: str) -> PaginatedArticlesDTO:
        return self.article_repo.find_articles(pagination_dto, search_query)
