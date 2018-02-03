import unittest

import os,sys
parentdir = os.path.abspath("./..")
sys.path.insert(0,parentdir) 
print sys.path 

import create_and_fill_restaurats_database
import restaurants_controller

class TestRestaurantsController(unittest.TestCase):
 
    def setUp(self):
        create_and_fill_restaurats_database.create_database() 
        create_and_fill_restaurats_database.add_menu_items()   
    
    def tearDown(self):
        restaurants_controller.close_database()  
         
    def test_get_restaurant_if_valid_id_should_return_restaurant(self):
        restaurant = restaurants_controller.get_restaurant(2)
        self.assertEqual(2, restaurant.id)
        self.assertEqual("Super Stir Fry", restaurant.name)
        
    def test_get_restaurant_if_invalid_id_should_return_none(self):
        restaurant = restaurants_controller.get_restaurant(89)
        self.assertEqual(None, restaurant)
        
    def test_update_restaurant_if_invlid_id_should_not_update_and_not_crash(self):
        restaurants_original = restaurants_controller.get_restaurants()
        restaurants_controller.update_restaurant(78,"New Name")
        restaurants_after_update = restaurants_controller.get_restaurants()
        self.assertListEqual(restaurants_original, restaurants_after_update)
     
    def test_delete_restaurant_if_invalid_id_should_not_delete_and_not_crash(self):
        restaurants_original = restaurants_controller.get_restaurants()
        restaurants_controller.delete_restaurant(78)
        restaurants_after_update = restaurants_controller.get_restaurants()
        self.assertListEqual(restaurants_original, restaurants_after_update)
   
        
    def test_get_restaurants_empty_database_should_return_empty_list(self):
        restaurants = restaurants_controller.get_restaurants()
        for restaurant in restaurants:
            restaurants_controller.delete_restaurant(restaurant.id)
        restaurants = restaurants_controller.get_restaurants()
        self.assertListEqual([], restaurants)
    
    
if __name__ == "__main__":
    unittest.main()
