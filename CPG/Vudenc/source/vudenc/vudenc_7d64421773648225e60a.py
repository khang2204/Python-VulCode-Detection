def configure_blueprints(app):...
"""docstring"""
from app.questions.api.v1.view import question_blueprint
from .home.views import home_blueprint
from .auth.api.v1.view import auth_blueprint
from .answers.api.v1.view import answers_blueprint
from .votes.api.v1.view import votes_blueprint
from .comments.api.v1.view import comments_blueprint
app_blueprints = [answers_blueprint, question_blueprint, auth_blueprint,
    votes_blueprint, comments_blueprint, home_blueprint]
for bp in app_blueprints:
app.register_blueprint(bp)
