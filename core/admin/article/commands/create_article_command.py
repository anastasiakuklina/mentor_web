from result import Err, Result, Ok

from .common import upload_and_replace_paths
from ..dto import ArticleCreateDTO, ArticleCreateRepoDTO
from ..exceptions import ValidationError
from ..repository import IArticleRepository
from core.file.protocol import FileServiceProtocol


class CreateArticleCommand:
    def __init__(
        self, article_repo: IArticleRepository, file_service: FileServiceProtocol
    ):
        self.article_repo = article_repo
        self.file_service = file_service

    def create_article(self, dto: ArticleCreateDTO) -> Result[int, Exception]:
        if not self.article_repo.is_slug_unique(dto.slug):
            return Err(ValidationError("Slug is already exists"))

        file_name = self.file_service.save_image(dto.image)

        handled_text = upload_and_replace_paths(self.file_service, dto.text, dto.text_images)

        repo_dto = ArticleCreateRepoDTO(**dto.model_dump(exclude={'image', 'text_images', 'text'}),
                                        image=file_name,
                                        text=handled_text
                                        )

        return Ok(self.article_repo.create_article(repo_dto))
