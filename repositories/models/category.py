from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimeStampMixin


class Category(Base, TimeStampMixin):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True,  autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    slug: Mapped[str] = mapped_column(nullable=False, unique=True)
    is_draft: Mapped[bool] = mapped_column(default=False)

