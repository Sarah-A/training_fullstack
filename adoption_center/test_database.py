"""
	insert data into the (previously created) database to test and play with it

"""

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

from puppy_shelter import Base, Shelter, Puppy, Person

from datetime import date

from dateutil import relativedelta
from dateutil.relativedelta import relativedelta

engine = create_engine('sqlite:///puppy_shelter.db')

Base.metadata.bind = engine  	# bind the engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

#----------------------------------------------------------------------------------------------------------
# Just playing around and testing the database:
#----------------------------------------------------------------------------------------------------------

# shelters = session.query(Shelter).all()
# for shelter in shelters:
# 	print("\nShelter: {}\n\tPuppies: ".format(shelter.name)),
# 	for puppy in shelter.puppies:
# 		print("{}, ".format(puppy.name)),
# print("\n")

# puppies = session.query(Puppy).all()
# for puppy in puppies:
# 	print("Puppy: {}-{}, Shelter: {}, Profile: {}, Adopters: {}".format(puppy.id, puppy.name, puppy.shelter.name, puppy.profile.id, puppy.adopters))

# # MANY_TO_MANY relationship:
# lucy = session.query(Puppy).filter_by(name = 'Lucy').one()
# molly = session.query(Puppy).filter_by(name = 'Molly').one()

# james = session.query(Person).filter_by(name = 'James').one()
# james.puppies.append(lucy)
# james.puppies.append(molly)
# session.add(james)

# sue = session.query(Person).filter_by(name = 'Sue').one()
# sue.puppies.append(lucy)
# sue.puppies.append(molly)
# session.add(sue)

# session.commit()

# puppies = session.query(Puppy).all()
# for puppy in puppies:
# 	print("Puppy: {}-{}, Shelter: {}, Profile: {}, Adopters: ".format(puppy.id, puppy.name, puppy.shelter.name, puppy.profile.id)),
# 	for adopter in puppy.adopters:
# 		print("{}, ".format(adopter.name))
# 	print("\n")


print("""
#-----------------------------------------------------------------------------------------------------------
# Instructions for this exercise:
# 		Using SQLAlchemy perform the following queries on your database:
# 		1. Query all of the puppies and return the results in ascending alphabetical order
# 		2. Query all of the puppies that are less than 6 months old organized by the youngest first
# 		3. Query all puppies by ascending weight
# 		4. Query all puppies grouped by the shelter in which they are staying
#----------------------------------------------------------------------------------------------------------
""")

print("""
#-----------------------------------------------------------------------------------------------------------
		Answers:
#-----------------------------------------------------------------------------------------------------------
""")

# 1. Query all of the puppies and return the results in ascending alphabetical order:
print("\n1. Query all of the puppies and return the results in ascending alphabetical order:")
for puppy in session.query(Puppy).order_by(Puppy.name):
	print("{}({},{}): Shelter: {}".format( puppy.name, puppy.id, puppy.date_of_birth , puppy.shelter.name))

# 2. Query all of the puppies that are less than 6 months old organized by the youngest first
print("\n2. Query all of the puppies that are less than 6 months old organized by the youngest first")
today = date.today()
six_months_ago = today + relativedelta(months = -6)
#print("today: {} , six months ago: {}".format(today, six_months_ago))

for puppy in session.query(Puppy).filter(Puppy.date_of_birth > six_months_ago).order_by(Puppy.date_of_birth.desc()):
	print("{}({}): birth date:: {}".format( puppy.name, puppy.id, puppy.date_of_birth))

print("\n3. Query all puppies by ascending weight:")
for puppy in session.query(Puppy).order_by(Puppy.weight):
	print("{}({},{}): weight: {} pounds".format( puppy.name, puppy.id, puppy.date_of_birth , puppy.weight/100))

print("\n3. Query all puppies by ascending weight - return tuples:")
result = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()
for item in result:
	print item[0], item[1]


print("\n4. Query all puppies grouped by the shelter in which they are staying - trivial answer:")
for shelter in session.query(Shelter).order_by(Shelter.name):
	print("Shelter: {}".format(shelter.name))
	for puppy in session.query(Puppy).filter(Puppy.shelter_id == shelter.id).order_by(Puppy.name):
		print("{} ({})".format( puppy.name, puppy.shelter.name))

print("\n4. Query all puppies grouped by the shelter in which they are staying - elegant answer:")
for puppy in session.query(Puppy).join(Shelter).filter(Shelter.id == Puppy.shelter_id).order_by(Shelter.name, Puppy.name):
	print("{} ({})".format( puppy.name, puppy.shelter.name))


print("\n4. Query all puppies grouped by the shelter in which they are staying - with grouping:")
from sqlalchemy import func
result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
for item in result:
	print("{},{},{}".format(item[0].id, item[0].name, item[1]))