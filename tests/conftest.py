import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.app.api.router import router
from backend.app.db.connection import SQLite3DataBase
from backend.app.core.services import init_schema
from backend.storage.repository import Repository

@pytest.fixture
def repository(tmp_path):
    database=SQLite3DataBase(tmp_path/'test.db')
    init_schema(database)

    cache_dir=tmp_path/'cache'
    cache_dir.mkdir()

    return Repository(database, cache_dir)

@pytest.fixture
def api_app():
    app=FastAPI()
    app.include_router(router, prefix='api/v1')

    return app

@pytest.fixture
def client(api_app):
    with TestClient(api_app) as test_client:
        yield test_client


