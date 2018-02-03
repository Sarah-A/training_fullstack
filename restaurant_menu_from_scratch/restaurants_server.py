"""
	restaurants_server.py

"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
import restaurants_controller
import re

STAT_SUCCESS	= 200
STAT_ERR_FILE_NOT_FOUND = 404
STAT_ERR_BAD_PARAMS = 422

HTML_CREATE_NEW_RESTAURANT = """
								<html>
								<body>
									<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>
										<h1>Create a New Restaurant</h1>
										<input name='restaurant_name' type='text' >
										<input type='submit' value='Create'> 
									</form>
								</body>
								</html>
							 """
							 
HTML_EDIT_RESTAURANT = """
								<html>
								<body>
									<form method='POST' enctype='multipart/form-data' action='/{restaurant_id}/edit'>
										<h1>{restaurant_name}</h1>
										<input name='restaurant_name' type='text' >
										<input type='submit' value='Rename'> 
									</form>
								</body>
								</html>
							 """
							 
HTML_DELETE_RESTAURANT = """
								<html>
								<body>
									<form method='POST' enctype='multipart/form-data' action='/{restaurant_id}/delete'>
										<h1>Delete {restaurant_name}</h1>
										<p> Are you sure that you want to delete {restaurant_name}? </p>
										<input type='submit' name="action" value='Delete'>
										<input type='submit' name="action" value='Cancel'> 
									</form>
								</body>
								</html>
							 """
							 
edit_restaurant_re = re.compile("/([0-9]+)/edit")
delete_restaurant_re = re.compile("/([0-9]+)/delete")

class WebserverHandler(BaseHTTPRequestHandler):
	"""
		WebserverHandler class
		Handles all client requests.
	"""
	
	def send_response_header(self,response_status, keyword = "Content-type",value = "text/html"):
		self.send_response(response_status)
		self.send_header(keyword, value)
		self.end_headers()
		
	def get_form_field_contents(self,field_name):
		messagecontent = [""]
		ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
		if ctype == "multipart/form-data":
			fields = cgi.parse_multipart(self.rfile, pdict)
			messagecontent = fields.get(field_name)
		else:
			print("wrong data type: {}".format(ctype))
		return messagecontent
			
			
	def display_all_restaurants_page(self):
		self.send_response_header(STAT_SUCCESS)	
		restaurants = restaurants_controller.get_restaurants()
				
		output = ""
		output += "<html><body>"
		for restaurant in restaurants:
			output += "<h2>{}</h2>".format(restaurant.name)
			output += "<a href = 'restaurants/{}/edit'>Edit</a><br>".format(restaurant.id)
			output += "<a href = 'restaurants/{}/delete'>Delete</a><br>".format(restaurant.id)
		output += "<h3><a href = '/restaurants/new'>Create a New Restaurant</a></h3>"
		output += "</body></html>"

		self.wfile.write(output)
		
	def display_edit_restaurant_page(self):
		match = edit_restaurant_re.search(self.path)
		if match:
			id = match.group(1)
			restaurant = restaurants_controller.get_restaurant(id)
			if restaurant:
				self.send_response_header(STAT_SUCCESS)	
				self.wfile.write(HTML_EDIT_RESTAURANT.format(restaurant_name = restaurant.name,restaurant_id = id))
			else:
				self.send_error(STAT_ERR_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))
		else:
			self.send_error(STAT_ERR_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))

	def display_delete_restaurant_page(self):
		match = delete_restaurant_re.search(self.path)
		if match:
			id = match.group(1)
			restaurant = restaurants_controller.get_restaurant(id)
			if restaurant:
				self.send_response_header(STAT_SUCCESS)
				self.wfile.write(HTML_DELETE_RESTAURANT.format(restaurant_name = restaurant.name, restaurant_id = id))
			else:
				self.send_error(STAT_ERR_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))
		else:
			self.send_error(STAT_ERR_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))
		
				
	def display_new_restaurant_page(self):
		self.send_response_header(STAT_SUCCESS)				
		self.wfile.write(HTML_CREATE_NEW_RESTAURANT)

	def do_restaurant_rename(self):
		messagecontent = self.get_form_field_contents("restaurant_name")
		name = messagecontent[0]
		if len(name) > 0:
			match = edit_restaurant_re.search(self.path)
			if match:
				id = match.group(1)
				restaurants_controller.update_restaurant(id,name)
			else:
				self.send_error(STAT_ERR_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))
		else:
			self.send_error(STAT_ERR_BAD_PARAMS, "Empty Name")
			
	def do_restaurant_create(self):
		messagecontent = self.get_form_field_contents("restaurant_name")
		name = messagecontent[0]
		if len(name) > 0:
			restaurants_controller.add_restaurant(name)
		else:
			self.send_error(STAT_ERR_BAD_PARAMS, "Empty Restaurant Name")
			
	def do_restaurant_delete(self):
		print("in do_restaurant_delete")
		messagecontent = self.get_form_field_contents("action")
		action = messagecontent[0]
		print("action: {}".format(action))
		if (len(action) > 0) and (action == "Delete"):
			match = delete_restaurant_re.search(self.path)
			if match:
				id = match.group(1)
				restaurants_controller.delete_restaurant(id)
			else:
				self.send_error(STAT_ERR_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))
		# Cancel - doesn't have to do anything.
		elif action != "Cancel":
			self.send_error(STAT_ERR_BAD_PARAMS, "Invalid Action: {}".format(action))
			
		
	def do_GET(self):		
		match = None
		try:
			if self.path.endswith("/restaurants"):							
				self.display_all_restaurants_page()							
			elif self.path.endswith("/edit"):
				self.display_edit_restaurant_page()
			elif self.path.endswith("/delete"):
				self.display_delete_restaurant_page()
			elif self.path.endswith("/new"):
				self.display_new_restaurant_page()
		except IOError:
			self.send_error(STAT_ERR_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))

	def do_POST(self):
		try:
			if self.path.endswith("/new"):			
				self.do_restaurant_create()
			elif self.path.endswith("/edit"):
				self.do_restaurant_rename()
			elif self.path.endswith("/delete"):
				self.do_restaurant_delete()
			self.send_response_header(303,"Location","/restaurants")
		except:
			# TODO:
			pass

def main():
	try:
		port = 8080
		server = HTTPServer(('',port), WebserverHandler)
		print("Restaurants Server running on port {}".format(port))
		server.serve_forever()

	except KeyboardInterrupt:		
		print("Ctrl-C was pressed - stopping web server...")
		server.socket.close()


if __name__=='__main__':
	main()
