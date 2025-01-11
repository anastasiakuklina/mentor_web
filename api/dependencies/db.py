from typing import Generator

from fastapi import FastAPI
from sqlalchemy.orm import Session
from starlette.requests import HTTPConnection


def get_db_session(request: HTTPConnection):
    app: FastAPI = request.app
    session_maker = getattr(app.state, 'session_maker')
    with session_maker() as session:
        yield session
