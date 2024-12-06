from core.landing.external_resource.dto import ExternalResourceDTO
from core.landing.external_resource.repository import IExternalResourceRepository


class ExternalResourceService:

    def __init__(self, resource_repo: IExternalResourceRepository):
        self.resource_repo = resource_repo

    def get_resources(self) -> list[ExternalResourceDTO]:
        return self.resource_repo.get_resources()
