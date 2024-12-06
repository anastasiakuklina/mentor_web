from core.landing.main_page.dto import MainPageDTO
from core.landing.main_page.repository import IMainPageRepository


class MainPageService:

    def __init__(self, main_page_repo: IMainPageRepository):
        self.main_repo = main_page_repo

    def get_main_page(self) -> MainPageDTO:
        return self.main_repo.get_main_page()
