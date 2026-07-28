from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
__tablename__ = 'user'
id = Column(Integer, primary_key=True)
name = Column(String(250), nullable=False)
email = Column(String(250), nullable=False)
picture = Column(String(250))
__tablename__ = 'Grudget'
id = Column(Integer, primary_key=True)
name = Column(String(250), nullable=False)
user_id = Column(Integer, ForeignKey('user.id'))
user = relationship(User)
@property...
"""docstring"""
return {'name': self.name, 'id': self.id}
