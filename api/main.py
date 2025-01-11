import uvicorn
from fastapi import FastAPI, APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.config import settings
from .admin import router as admin_router


def create_app():
    app = FastAPI(
        title='Mentor web',
        docs_url="/docs",        # Ensure this line is present
        redoc_url="/redoc",      # Ensure this line is present
        openapi_url="/openapi.json",
        version='1.0.0',
    )
    engine = create_engine(settings.db_psycopg_url,
                           echo=False,
                           pool_size=5,
                           max_overflow=10)
    session_maker = sessionmaker(engine)
    setattr(app.state, 'session_maker', session_maker)
    root_router = APIRouter()
    root_router.include_router(admin_router)
    app.include_router(root_router)
    return app


if __name__ == '__main__':
    uvicorn.run('main:create_app', host='0.0.0.0', port=8005, reload=True)