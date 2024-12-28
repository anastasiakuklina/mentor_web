from result import Err, Result, Ok

from .common import save_text_files
from ..dto import ArticleCreateDTO
from ..exceptions import ValidationError
from ..repository import IArticleRepository
from core.file.protocol import FileServiceProtocol


class CreateArticleCommand:

    def __init__(self, article_repo: IArticleRepository, file_service: FileServiceProtocol):
        self.article_repo = article_repo
        self.file_service = file_service

    def create_article(self, dto: ArticleCreateDTO) -> Result[int, Exception]:
        if not self.article_repo.is_slug_unique(dto.slug):
            return Err(ValidationError("Slug is already exists"))

        file_name = self.file_service.save_image(dto.image)
        
        handled_text = save_text_files(dto)

        return Ok(self.article_repo.create_article(dto)) # TODO другой dto