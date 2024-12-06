from abc import ABC, abstractmethod

from core.landing.offering.dto import OfferingDTO, OfferingDetailDTO


class IOfferingRepository(ABC):

    @abstractmethod
    def get_offerings(self) -> list[OfferingDTO]:
        pass

    @abstractmethod
    def get_offering(self, offering_id: int) -> OfferingDetailDTO:
        pass
