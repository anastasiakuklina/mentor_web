from abc import ABC
from uuid import UUID

from .dto import CommentCreateDTO, SubCommentCreateDTO, CommentListItemDTO


class ICommentRepository(ABC):

    def new_comment(self, dto: CommentCreateDTO):
        pass

    def new_sub_comment(self, dto: SubCommentCreateDTO):
        pass

    def get_article_comments(self, slug: str) -> list[CommentListItemDTO]:
        pass

    def get_sub_comments(self, comment_id: UUID) -> list[CommentListItemDTO]:
        pass