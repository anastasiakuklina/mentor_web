from sqlalchemy.orm import Mapped, mapped_column

from repositories.models.base import TimeStampMixin, Base


class Tag(Base, TimeStampMixin):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    slug: Mapped[str] = mapped_column(nullable=False, unique=True)
    is_draft: Mapped[bool] = mapped_column(default=False)
    icon_base64: Mapped[str] = mapped_column(nullable=False)
