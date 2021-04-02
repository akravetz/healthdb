from flask import Flask, render_template_string, Blueprint
from flask_security import (
    auth_required,
    current_user,
)

test_bp = Blueprint("test_blueprint", __name__)


@test_bp.route("/")
@auth_required()
def home():
    return render_template_string("Hello {{ current_user.email }}")

@test_bp.route("/foo")
def foo():
    return [1,2,3]
