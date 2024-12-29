from result import Result, Err, Ok

from .common import upload_and_replace_paths
from ..dto import ArticleUpdateDTO, ArticleUpdateRepoDTO
from ..exceptions import ArticleNotFoundError, ValidationError
from ..repository import IArticleRepository
from core.file.protocol import FileServiceProtocol


class UpdateArticleCommand:
    def __init__(
        self, article_repo: IArticleRepository, file_service: FileServiceProtocol
    ):
        self.article_repo = article_repo
        self.file_service = file_service

    def update_article(
        self, dto: ArticleUpdateDTO
    ) -> Result[None, ArticleNotFoundError | ValidationError]:
        article = self.article_repo.get_article_by_id(dto.id)
        if not article:
            return Err(ArticleNotFoundError())

        if not self._is_slug_valid(dto.slug, article.slug):
            return Err(ValidationError("Slug already exists"))

        file_name = self._process_image(dto.image, article.image)
        text = self._process_text_and_images(dto.text, dto.text_images, article.text)

        repo_dto = self._create_repo_dto(dto, file_name, text)
        self.article_repo.update_article(repo_dto)

        return Ok(None)

    def _is_slug_valid(self, slug: str, current_slug: str) -> bool:
        return slug == current_slug or self.article_repo.is_slug_unique(slug)

    def _process_image(self, new_image: bytes | None, current_image: str) -> str:
        return self.file_service.save_image(new_image) if new_image else current_image

    def _process_text_and_images(
        self, text: str, text_images: dict[str, bytes], current_text: str
    ) -> str:
        return (
            upload_and_replace_paths(self.file_service, text, text_images)
            if text_images
            else current_text
        )

    def _create_repo_dto(
        self, dto: ArticleUpdateDTO, file_name: str, text: str
    ) -> ArticleUpdateRepoDTO:
        return ArticleUpdateRepoDTO(
            **dto.model_dump(exclude={"image", "text_images", "text"}),
            image=file_name,
            text=text
        )
