from core.landing.about.dto import AboutDTO
from core.landing.about.repository import IAboutRepository


class AboutService:

    def __init__(self, about_repo: IAboutRepository):
        self.about_repo = about_repo

    def get_about_texts(self) -> AboutDTO:
        return self.about_repo.get_about_texts()