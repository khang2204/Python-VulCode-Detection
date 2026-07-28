""" mysql File

    Arquivo onde se encontra todas as funções para trabalhar com o db
Todo:

    None

"""
import json
import mysql.connector as mysql
import src.settings as conf
"""
        MySQL class:
           	Todas as funções para manipulação do DB
    """
def __init__(self):...
self.__connection = mysql.connect(**conf.DATABASE)
self.cursor = self.__connection.cursor()
def execute(self, query):...
"""docstring"""
self.cursor.execute(query)
print('Error: {}'.format(error))
return self.cursor
