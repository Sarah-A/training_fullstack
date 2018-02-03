'''
	The configuration file will connect to SQLAlchemy and configure all the parameters and
'''
#===========================================================================================================================
# import sqlAlchemy and create the dclerative_base for our project:
#===========================================================================================================================
import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, backref

from sqlalchemy.schema import Table

from sqlalchemy import create_engine

Base = declarative_base()



#===========================================================================================================================
# 	Create the object representation of the table in a python class
# 	here we will:
# 	* extends the Base class we created in database_setup - for each table we want to create in the database
# 	* inside each class, we'll create the table and mapper code
#===========================================================================================================================


class Shelter(Base):
	__tablename__ = 'shelter'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	address = Column(String(150), nullable = False)
	city = Column(String(80), nullable = False)
	state = Column(String(20), nullable = False)
	zip_code = Column(String(20), nullable = False)
	website = Column(String(150))
	# this relationship is MANY-TO-ONE because every puppy have 1 shelter and every shelter can have many puppies
	puppies = relationship('Puppy', backref='shelter')
	# can also use:
	# puppies = relationship('Puppy', back_populates='shelter') and then, we'll need to add in Puppy:
	# shelter = relationship('Shelter', back_populates='puppies')


class Puppy(Base):
	__tablename__ = 'puppy'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	picture = Column(String(150))
	date_of_birth = Column(Date)
	gender = Column(Enum('male','female'), nullable = False)
	weight = Column(Integer) 									# in 0.01 pounds to avoid floating points.
	shelter_id = Column(Integer,ForeignKey('shelter.id'))

# In this exercise you will create puppy profiles to collect even more information about each puppy.
# Each puppy is allowed up to one profile which can contain a url to the puppy's photo , a description about the puppy
# and any special needs the puppy may have. Implement this table and the foreign key relationship in your code.
class PuppyProfile(Base):
	__tablename__ = 'puppy_profile'

	id = Column(Integer, primary_key = True)
	puppy_id = Column(Integer, ForeignKey('puppy.id'))
	picture = Column(String(150))		# a different picture than puppy.picture. otherwise, will use the puppy field.
	description = Column(String)		# should be foreign key - the description is part of the puppy
	special_needs = Column(String)
	#This relationship is ONE-TO_ONE because of the uselist=False
	puppy = relationship('Puppy',backref=backref('profile',uselist=False))


# Puppies can be adopted by one person, or a family of people.
# Similarly, a person or family can adopt one or several puppies.
# See if you can create a many-to-many relationship between puppies and adopters.
puppy_person_table = Table('association', Base.metadata,
							Column('person_id', Integer, ForeignKey('person.id')),
							Column('puppy_id', Integer, ForeignKey('puppy.id')))

class Person(Base):
	__tablename__ = 'person'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	# This is MANY-TO-MANY relationship. The puppy_person_table maintain the many-to-many relationship and the
	# secondary parameter connects to it:
	puppies = relationship('Puppy',secondary=puppy_person_table, backref='adopters')
