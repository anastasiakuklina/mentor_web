from fastapi import Depends
from sqlalchemy.orm import Session

from core.admin.category.service import AdminCategoryService
from core.admin.tag.service import AdminTagService
from repositories.admin.category import AdminCategoryRepository
from repositories.admin.tag import AdminTagRepository
from .db import get_db_session


def get_admin_category_repo(session: Session = Depends(get_db_session)) -> AdminCategoryRepository:
    return AdminCategoryRepository(session)


def get_admin_category_service(repo: AdminCategoryRepository = Depends(get_admin_category_repo)) -> AdminCategoryService:
    return AdminCategoryService(repo)


def get_admin_tag_repo(session: Session = Depends(get_db_session)) -> AdminTagRepository:
    return AdminTagRepository(session)


def get_admin_tag_service(repo: AdminTagRepository = Depends(get_admin_tag_repo)) -> AdminTagService:
    return AdminTagService(repo)
