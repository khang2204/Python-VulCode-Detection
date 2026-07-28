from flask import Flask, jsonify, make_response, request, g
from flask_restful import Api
from celery import Celery
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from common.utils import unauthorized, headers, not_found
from config import load_env_variables, DevelopmentConfig, ProdConfig
load_env_variables()
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)
print('Reflecting classes...')
Base = automap_base()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_size=20,
    max_overflow=20, pool_pre_ping=True)
Base.prepare(engine, reflect=True)
print('Classes reflected...')
@app.before_request...
"""docstring"""
g.session = Session(engine)
g.Base = Base
@app.after_request...
"""docstring"""
g.session.commit()
g.session.close()
return resp
