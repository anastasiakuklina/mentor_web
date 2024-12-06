from core.landing.offering.dto import OfferingDTO, OfferingDetailDTO
from core.landing.offering.repository import IOfferingRepository


class OfferingService:

    def __init__(self, offering_repo: IOfferingRepository):
        self.offering_repo = offering_repo

    def get_offerings(self) -> list[OfferingDTO]:
        return self.offering_repo.get_offerings()

    def get_offering(self, offering_id: int) -> OfferingDetailDTO:
        return self.offering_repo.get_offering(offering_id)
