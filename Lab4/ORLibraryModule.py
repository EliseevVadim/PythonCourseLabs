import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
#from sqlalchemy.orm import relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'Authors'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    country = Column(String)
    years = Column(String)
    
class Book(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key = True)
    authors_id = Column(Integer, ForeignKey('Authors.id', ondelete='CASCADE'))
    name = Column(String)
    pages = Column(Integer)
    publisher = Column(String)
    publishing_year = Column(Integer)
    
def create_tables():
    engine = sqlalchemy.create_engine('sqlite:///db/ORLibrary.db', echo = False)
    Base.metadata.create_all(engine)
    
  