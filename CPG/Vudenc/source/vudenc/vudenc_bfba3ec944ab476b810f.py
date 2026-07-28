def create_app(config=None):...
app = Flask(__name__)
app.config.from_object(app_config[config])
app.config.from_envvar('BENWAONLINE_SETTINGS', silent=True)
app.config.from_object('secrets')
db.init_app(app)
migrate = Migrate(app, db)
oauth.init_app(app)
login_manager.init_app(app)
@login_manager.user_loader...
return User.get(user_id)
