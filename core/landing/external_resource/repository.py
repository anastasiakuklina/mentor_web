from abc import ABC, abstractmethod

from core.landing.external_resource.dto import ExternalResourceDTO


class IExternalResourceRepository(ABC):

    @abstractmethod
    def get_resources(self) -> list[ExternalResourceDTO]:
        pass