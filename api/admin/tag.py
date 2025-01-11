from fastapi import Depends, APIRouter

from api.dependencies.admin import get_admin_tag_service
from core.admin.tag.dto import TagSortingDTO, TagsGetDTO
from core.admin.tag.service import AdminTagService
from core.dto import PaginationDTO

router = APIRouter(
    prefix='/tags',
    tags=['admin/tags']
)

@router.get('')
async def get_tags(tag_service: AdminTagService = Depends(get_admin_tag_service)):
    dto = TagsGetDTO(pagination=PaginationDTO(limit=5, offset=0),
                     sorting=TagSortingDTO(sort_by="name", sort_order="asc"))
    return tag_service.get_tags(dto)
