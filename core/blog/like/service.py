from core.blog.like.dto import ToggleLikeDTO
from core.blog.like.repository import ILikeDislikeRepository


class LikeDislikeService:

    def __init__(self, like_dislike_repo: ILikeDislikeRepository):
        self.like_repo = like_dislike_repo

    def toggle_like(self, dto: ToggleLikeDTO):
        self.like_repo.toggle_like(dto)

    def toggle_dislike(self, dto: ToggleLikeDTO):
        self.like_repo.toggle_dislike(dto)
