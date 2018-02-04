
restaurant_menu_from_scratch:
======================================
### Part of 'Full Stack Foundations' Udacity course

In this project I've:
* Used SQLAlchemy (ORM library) to create a database using SQLite and to manipulate it using CRUD actions.
* Udacity provided the instructions in `/project_instuctions/restaurant_menu_from_scratch.png`. `/project_instructions/webserver.py` is the example file that we've created in class during the course.

  
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
	$ cd /vagrant/restaurants_list_from_scratch 
	```  
4. To create and fill the database:  
    ```
	$ python create_and_fill_restaurants_database.py
	=> added menu items!
	```
	Note: in order to create an *empty* database, run: `$ python database_setup.py` instead.  
5. To start the server:
	```
	$ python restaurants_server.py
	```
6. To use the site:
	In a web-browser, enter the following url: "localhost:8080/restaurants" 

Tests:
==========================
**tst** directory : contains a few test files that I used to _partially_ test the database and interface.

### How To Run the Unit Tests:
``` 
cd tst
python -m unittest discover .
```


