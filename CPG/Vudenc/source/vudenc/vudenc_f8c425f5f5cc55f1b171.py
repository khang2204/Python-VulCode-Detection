""" Api Controller

    Arquivo onde se encontra toda a lógica que rodará na rota '/api'

Todo:

    None

"""
import cgi
import json
import src.models.mysql as mysql
def getFields(environ):...
"""docstring"""
data_env = environ.copy()
data_env['QUERY_STRING'] = ''
data = cgi.FieldStorage(fp=environ['wsgi.input'], environ=data_env,
    keep_blank_values=True)
return data
