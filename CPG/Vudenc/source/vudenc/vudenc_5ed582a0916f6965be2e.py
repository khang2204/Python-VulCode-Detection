import os
BASE = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = BASE
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOADED_IMAGES_DEST = '/static/'
UPLOADED_BENWA_DIR = os.path.join(BASE, 'static', 'tempbenwas')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE, 'db',
    'benwaonline.db')
DEBUG = True
SECRET_KEY = 'not-so-secret'
SQLALCHEMY_DATABASE_URI = 'sqlite://'
TESTING = True
TWITTER_CONSUMER_KEY = 'consume'
TWITTER_CONSUMER_SECRET = 'secret'
WTF_CSRF_ENABLED = False
SECRET_KEY = 'not-so-secret'
DEBUG = False
app_config = {'dev': DevConfig, 'test': TestConfig, 'prod': ProdConfig}
