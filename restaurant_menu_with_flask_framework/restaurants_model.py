"""
	restaurants_model.py
	
	This module is the itnerface to the application model, including the data base
	and all the business logic.

"""
from restaurants_db import Base, Restaurant, MenuItem, DBSession

class Restaurants:
	
	def __init__(self):
		self.session = DBSession()
		
	def get_restaurant(self, id):
		return self.session.query(Restaurant).filter_by(id=id).first()
	
	def get_restaurants(self):
		return self.session.query(Restaurant).all()
		
	def add_restaurant(self, name):
		new_restaurant = Restaurant(name = name)
		self.session.add(new_restaurant)
		self.session.commit()
	
	def update_restaurant(self, id,name):
		restaurant = self.session.query(Restaurant).filter_by(id=id).first()
		if restaurant:
			restaurant.name = name
			self.session.add(restaurant)
			self.session.commit()
			
	def delete_restaurant(self, id):
		#print("delete restaurant: {}".format(id))
		restaurant = self.session.query(Restaurant).filter_by(id=id).first()
		if restaurant:
			self.session.delete(restaurant)
			self.session.commit()
			
	def get_menu_item(self, id):
		return self.session.query(MenuItem).filter_by(id=id).first()
	
	def get_menu_items_of_restaurant(self, restaurant_id):
		return self.session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
	
	
	def add_menu_item(self, name, restaurant_id):
		new_item = MenuItem(name = name, restaurant_id = restaurant_id)
		self.session.add(new_item)
		self.session.commit()
		
	def update_menu_item(self, id,name):
		item = self.session.query(MenuItem).filter_by(id=id).first()
		if item:
			item.name = name
			self.session.add(item)
			self.session.commit()
			
	def delete_menu_item(self, id):
		item = self.session.query(MenuItem).filter_by(id=id).first()
		if item:
			self.session.delete(item)
			self.session.commit()

	def close(self):
		self.session.close()
