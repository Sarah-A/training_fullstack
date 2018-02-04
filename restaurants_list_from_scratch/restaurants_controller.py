"""
	restaurants_control.py
	
	This module connect the restaurants_server with the restaurant_menu database.

"""
from database_setup import Base, Restaurant, MenuItem
from database_session import DBSession

session = DBSession()
		
def get_restaurant(id):
	return session.query(Restaurant).filter_by(id=id).first()

def get_restaurants():
	return session.query(Restaurant).all()
	
def add_restaurant(name):
	new_restaurant = Restaurant(name = name)
	session.add(new_restaurant)
	session.commit()

def update_restaurant(id,name):
	restaurant = session.query(Restaurant).filter_by(id=id).first()
	if restaurant:
		restaurant.name = name
		session.add(restaurant)
		session.commit()
		
def delete_restaurant(id):
	#print("delete restaurant: {}".format(id))
	restaurant = session.query(Restaurant).filter_by(id=id).first()
	if restaurant:
		session.delete(restaurant)
		session.commit()

def close_database():
	session.close()
