"""
    contain all the code required to open a session with the database
"""
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

from database_setup import Base, Restaurant, MenuItem, DATABASE_NAME



 # # create_engine tells our program which database we want to communicate with 
engine = create_engine('sqlite:///{}'.format(DATABASE_NAME))

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine      # bind the engine


# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
DBSession = sessionmaker(bind=engine)