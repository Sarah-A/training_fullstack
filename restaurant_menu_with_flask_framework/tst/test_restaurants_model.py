import unittest

import os,sys
root_dir = os.path.abspath("..")
sys.path.insert(0,root_dir) 
print("Root Dir: {}".format(root_dir))
print sys.path

import restaurants_db
import create_restaurats_database
import restaurants_model

class TestRestaurantsController(unittest.TestCase):
 
    def setUp(self):
        restaurants_db.create_database() 
        create_restaurats_database.add_menu_items()   
        self.restaurants = restaurants_model.Restaurants()
    
    def tearDown(self):
        self.restaurants.close()  
         
    def test_get_restaurant_if_valid_id_should_return_restaurant(self):
        restaurant = self.restaurants.get_restaurant(2)
        self.assertEqual(2, restaurant.id)
        self.assertEqual("Super Stir Fry", restaurant.name)
        
    def test_get_restaurant_if_invalid_id_should_return_none(self):
        restaurant = self.restaurants.get_restaurant(89)
        self.assertEqual(None, restaurant)
        
    def test_update_restaurant_if_invlid_id_should_not_update_and_not_crash(self):
        restaurants_original = self.restaurants.get_restaurants()
        self.restaurants.update_restaurant(78,"New Name")
        restaurants_after_update = self.restaurants.get_restaurants()
        self.assertListEqual(restaurants_original, restaurants_after_update)
     
    def test_delete_restaurant_if_invalid_id_should_not_delete_and_not_crash(self):
        restaurants_original = self.restaurants.get_restaurants()
        self.restaurants.delete_restaurant(78)
        restaurants_after_update = self.restaurants.get_restaurants()
        self.assertListEqual(restaurants_original, restaurants_after_update)
   
        
    def test_get_restaurants_empty_database_should_return_empty_list(self):
        restaurants = self.restaurants.get_restaurants()
        for restaurant in restaurants:
            self.restaurants.delete_restaurant(restaurant.id)
        restaurants = self.restaurants.get_restaurants()
        self.assertListEqual([], restaurants)
    
    
if __name__ == "__main__":
    unittest.main()
