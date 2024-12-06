from abc import ABC, abstractmethod

from core.landing.main_page.dto import MainPageDTO


class IMainPageRepository(ABC):

    @abstractmethod
    def get_main_page(self) -> MainPageDTO:
        pass
