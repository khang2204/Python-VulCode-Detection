db
)

app = Flask(__name__)


def config_app(app):
    app.config['SECRET_KEY'] = 'Keep it secret, keep it safe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.config['DEBUG'] = True


def add_jinja_functions(app):
    """Adds desired python functions to be accessible from Jinja templates"""
    app.jinja_env.globals.update(
        hasattr=hasattr,
        enumerate=enumerate,
        len=len
    )
