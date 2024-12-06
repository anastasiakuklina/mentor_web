from abc import abstractmethod, ABC

from .dto import ToggleLikeDTO, ToggleDislikeDTO


class ILikeDislikeRepository(ABC):

    @abstractmethod
    def toggle_like(self, dto: ToggleLikeDTO) -> None:
        pass

    @abstractmethod
    def toggle_dislike(self, dto: ToggleDislikeDTO) -> None:
        pass
