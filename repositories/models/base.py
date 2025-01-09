from datetime import datetime
from typing import Optional

from sqlalchemy import func, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TimeStampMixin:
    created_at: Mapped[Optional[datetime]] = mapped_column(server_default=func.now())
