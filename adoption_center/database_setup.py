'''
	This file creates the database
'''
from puppy_shelter import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///puppy_shelter.db')

Base.metadata.create_all(engine)


#---------------------------------------------------------------------------------------------------------------------
#  After running this file, we have a new empty database in the directory
#  Now we can populate it with data.
#---------------------------------------------------------------------------------------------------------------------
