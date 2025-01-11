import base64

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from api.config import settings
from core.admin.category.dto import CategoryCreateDTO, CategoryUpdateDTO, CategoriesGetDTO, CategorySortingDTO, \
    CategoriesFindDTO
from core.admin.category.service import AdminCategoryService
from core.admin.tag.dto import TagCreateRepoDTO, TagsFindDTO, TagSortingDTO, TagsGetDTO
from core.dto import PaginationDTO
from repositories.admin.category import AdminCategoryRepository
from repositories.admin.tag import AdminTagRepository

engine = create_engine(settings.db_psycopg_url,
                       echo=False,
                       pool_size=5,
                       max_overflow=10)

session_factory = sessionmaker(engine)
print(type(session_factory))


### CATEGORY
repo = AdminCategoryRepository(session_factory)
service = AdminCategoryService(repo)
# dto = CategoryCreateDTO(name="Go", slug="go")
# repo.create_category(dto)
# res = repo.get_categories()
# print(f"categories: {res}")
# repo.update_category(CategoryUpdateDTO(id=1, name="Python4", slug=None))
sorting_dto = CategorySortingDTO(sort_by="name", sort_order="desc")
get_dto = CategoriesGetDTO(pagination=PaginationDTO(limit=5, offset=0),
                           sorting=sorting_dto)
# res = repo.get_categories(get_dto)
res = service.get_categories(get_dto)
print(f"categories: {res}")
find_dto = CategoriesFindDTO(search_query="go", pagination=PaginationDTO(limit=2, offset=0), sorting=sorting_dto)
# res = repo.find_categories(find_dto)
res = service.find_categories(find_dto)
print(f"find_categories: {res}")
### TAG

repo = AdminTagRepository(session_factory)
# with open("sample.webp", "rb") as f:
#     icon = f.read()
#     icon_base64 = base64.b64encode(icon).decode('utf-8')
# dto = TagCreateRepoDTO(name="sync", slug="sync", icon_base64=icon_base64)
# print(repo.create_tag(dto))
# dto = TagCreateRepoDTO(name="OOP", slug="oop", icon_base64=icon_base64)
# print(repo.create_tag(dto))
# dto = TagCreateRepoDTO(name="FP", slug="fp", icon_base64=icon_base64)
# print(repo.create_tag(dto))

# get_dto = TagsGetDTO(pagination=PaginationDTO(limit=5, offset=0),
#                      sorting=TagSortingDTO(sort_by="name", sort_order="desc"))
# tags = repo.get_tags(get_dto)
# print(f"all_tags: {tags}")
# find_dto = TagsFindDTO(search_query="Sync", pagination=PaginationDTO(limit=2, offset=0),
#                        sorting=TagSortingDTO(sort_by="created_at", sort_order="desc"))
# tags = repo.find_tags(find_dto)
# print(f"sync_tags: {tags}")



# with engine.connect() as conn:
#     res = conn.execute(text("SELECT 1, 2, 3 UNION SELECT 4, 5, 6"))
#     print(res.all())

