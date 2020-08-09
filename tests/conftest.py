import os
import sys
import pytest

_cwd = os.path.dirname(os.path.abspath(__file__))
_root_dir = os.path.dirname(_cwd)

sys.path.append(_root_dir)

from scripts import app as flask_app


@pytest.fixture(scope="session")
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
