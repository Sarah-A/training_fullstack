'''
	The configuration file will connect to SQLAlchemy and configure all the parameters and
'''
#===========================================================================================================================
# import sqlAlchemy and create the dclerative_base for our project:
#===========================================================================================================================
import os
import sys
import os.path


from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

DATABASE_NAME = "restaurant_menu.db"


Base = declarative_base()


#===========================================================================================================================
# 	Create the object representation of the table in a python class
# 	here we will:
# 	* extends the Base class we created in database_setup - for each table we want to create in the database
# 	* inside each class, we'll create the table and mapper code
#===========================================================================================================================


class Restaurant(Base):
	# Table definition:
	__tablename__ = 'restaurant'
	# Table mappers ( maps the python class members to the database fields):
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)




class MenuItem(Base):
	# Table definition:
	__tablename__ = 'menu_item'
	# Table mappers ( maps the python class members to the database fields):
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	course = Column(String(30))
	price = Column(String(10))
	restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)
	
	
def create_database():

	if os.path.isfile(DATABASE_NAME):
		os.remove(DATABASE_NAME)
	
	# Connect to the data base:	
	engine = create_engine("sqlite:///{}".format(DATABASE_NAME))
	
	Base.metadata.create_all(engine)
	
	#  Now we have a new empty database in the directory


if __name__=="__main__":
    create_database()

