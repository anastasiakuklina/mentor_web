from result import Result, Err, Ok

from .common import save_text_files
from ..dto import ArticleUpdateDTO
from ..exceptions import ArticleNotFoundError, ValidationError
from ..repository import IArticleRepository
from core.file.protocol import FileServiceProtocol


class UpdateArticleCommand:

    def __init__(self, article_repo: IArticleRepository, file_service: FileServiceProtocol):
        self.article_repo = article_repo
        self.file_service = file_service

    def update_article(self, dto: ArticleUpdateDTO) -> Result[None, Exception]:
        article = self.article_repo.get_article_by_id(dto.id)
        if not article:
            return Err(ArticleNotFoundError())

        if (dto.slug != article.slug) and (not self.article_repo.is_slug_unique(dto.slug)):
            return Result(ValidationError("Slug is already exists"))

        file_name = self.file_service.save_image(dto.image)

        handled_text = save_text_files(dto)

        return Ok(self.article_repo.update_article(dto))  # TODO another dto