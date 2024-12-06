from abc import ABC, abstractmethod

from core.landing.about.dto import AboutDTO


class IAboutRepository(ABC):

    @abstractmethod
    def get_about_texts(self) -> AboutDTO:
        pass
