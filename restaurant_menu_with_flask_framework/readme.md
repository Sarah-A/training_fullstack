
restaurant_menu_with_flask_framework:
======================================
### Part of 'Full Stack Foundations' Udacity course

In this project I've:
* Used **Flask** and **SQLAlchemy** to create a database using **SQLite** and to manipulate it using CRUD actions.

  
Installation and Requirements:
=======================================
In order to run the tournament code:  
1. Install Git from: <http://git-scm.com/downloads>  
2. Install Virtual Box from: <https://www.virtualbox.org/wiki/Downloads>  
3. Install Vargant from: <https://www.vagrantup.com/downloads>  
4. Clone the repository: 
	```
	$ git clone https://github.com/Sarah-A/training_fullstack
	``` 

How to Run:
========================
1. Open 'Git Bash' (installed with Git) and browse to into the project/vagrant  
2. run:  
	```
	$ vagrant up
	$ vagrant ssh
	```
   Now you are logged into the virtual machine.  
3. run:  
	``` 
	$ cd /vagrant/restaurant_menu_with_flask_framework 
	```  
4. To create and fill the database:
	```
	$ python create_restaurants_database.py --fill
	=> added menu items!
	```
	Note: in order to create an *empty* database, run: `$ python create_restaurants_database.py` instead (with no arguments). 
5. To start the server:
	```
	$ python restaurants_menu_server.py
	```
6. To use the site:
	In a web-browser, enter the following url: "localhost:5000/restaurants/[restaurant-id]" 

How To Run the Unit Tests:
======================================
``` 
cd tst
python -m unittest discover .
```

