from uuid import UUID

from .dto import CommentCreateDTO, SubCommentCreateDTO, CommentListItemDTO
from .repository import ICommentRepository


class CommentService:

    def __init__(self, comment_repo: ICommentRepository):
        self.comment_repo = comment_repo

    def new_comment(self, dto: CommentCreateDTO):
        self.comment_repo.new_comment(dto)

    def new_sub_comment(self, dto: SubCommentCreateDTO):
        return self.comment_repo.new_sub_comment(dto)

    def get_article_comments(self, article_slug: str) -> list[CommentListItemDTO]:
        return self.comment_repo.get_article_comments(article_slug)

    def get_sub_comments(self, comment_id: UUID) -> list[CommentListItemDTO]:
        return self.comment_repo.get_sub_comments(comment_id)
