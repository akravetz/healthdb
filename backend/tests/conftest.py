from unittest.mock import Mock
import pytest


from .test_utils import WrapApp


@pytest.fixture
def client():
    """
    Create a wrapped flask app.
    This is used for unittests that want to mock out all
    underlying singletons (such as DBs).
    Assumes that app.security has been set.
    """

    from flask import Flask
    from src.app import init_app
    from src.models import User, Role
    from .test_utils import WrapApp

    app = Flask("testing")
    init_app(app, ":memory:", "secret key foo", "password salt bar")

    app.config["TESTING"] = True
    bmock = Mock()
    return WrapApp(app, User, Role, mocks={"blog_mock": bmock})
