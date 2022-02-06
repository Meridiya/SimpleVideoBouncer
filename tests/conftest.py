import pytest
from sanic_testing.reusable import ReusableClient

from testmoretv.app.app import app


@pytest.fixture
def client():
    app.config.CDN_URL = "cool.cdn"
    client = ReusableClient(
        app,
        port=42100,
    )
    with client:
        yield client
