
from typing import Any, Sequence

from sqlalchemy import Select, select, func, Result, Row, RowMapping, desc, asc
from sqlalchemy.orm import sessionmaker

from core.dto import PaginationDTO, SortingDTO


class BaseRepository:

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def paginate(self, stmt: Select, pagination_dto: PaginationDTO) -> tuple[Sequence, Any]:
        with (self.session_factory() as session):
            result = session.execute(stmt.limit(pagination_dto.limit).offset(pagination_dto.offset)).scalars().all()
            count_stmt = select(func.count()).select_from(stmt.subquery())
            count = session.execute(count_stmt).scalar_one()
            return result, count

    @staticmethod
    def add_order_by(stmt: Select, sorting_dto: SortingDTO) -> Select:
        order_func = asc if sorting_dto.sort_order == "asc" else desc
        stmt = stmt.order_by(order_func(sorting_dto.sort_by))
        return stmt