"""
	insert data into the (previously created) database to test and play with it

"""

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurant_menu.db')

Base.metadata.bind = engine  	# bind the engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

#----------------------------------------------------------------
# Create:
#----------------------------------------------------------------
# pizza_palace = Restaurant(name = "Pizza Palace")
# session.add(pizza_palace)
# session.commit()

#----------------------------------------------------------------
# Read:
#----------------------------------------------------------------
# print(session.query(Restaurant).first())

# cheese_pizza = MenuItem(name = "Cheese Pizza",
# 						description = "Made with fresh mozzarella",
# 						course = "Entry",
# 						price = "$8.99",
# 						restaurant = pizza_palace)

# session.add(cheese_pizza)
# session.commit()
# restaurants = session.query(Restaurant).all()
# for restaurant in restaurants:
# 	print("{}-{}".format(restaurant.id, restaurant.name))


#----------------------------------------------------------------
# Update:
#----------------------------------------------------------------
# veggie_burgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
# for veggie_burger in veggie_burgers:
# 	if veggie_burger != "$2.99":
# 		veggie_burger.price = "$2.99"
# 		session.add(veggie_burger)
# 		session.commit()
# for veggie_burger in veggie_burgers:
# 	print veggie_burger.id
# 	print veggie_burger.name
# 	print veggie_burger.description
# 	print veggie_burger.price
# 	print veggie_burger.restaurant.name
# 	print "\n"

#----------------------------------------------------------------
#Delete:
#----------------------------------------------------------------
# spinach_icecream = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
# print spinach_icecream.restaurant.name
# session.delete(spinach_icecream)
# session.commit()
# spinach_icecream = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()


restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
	print("{}-{}".format(restaurant.id, restaurant.name))





