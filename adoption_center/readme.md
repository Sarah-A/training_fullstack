
adoption_center:
==================

adoption_center project is an exercise in the Full Stack nano-degree.
In this project, I've:
* Used SQLAlchamy and SQLite to create a database for a puppy adoption center, according to the supplied model. 
* Experimented with the database and answered the questions of the course in test_database.py
* Udacity suppplied the model for the database and the puppypopulator.py that fills the database with test-data.

Installation and Requirements:
=======================================
In order to run the tournament code:  
1. Install Git from: <http://git-scm.com/downloads>  
2. Install Virtual Box from: <https://www.virtualbox.org/wiki/Downloads>  
3. Install Vargant from: <https://www.vagrantup.com/downloads>  
4. Clone the repository: 
	```
	git clone https://github.com/Sarah-A/training_fullstack
	``` 
  

How to run:
========================
To run the tests:  
1. Open 'Git Bash' (installed with Git) and browse to into the project/vagrant  
2. run:  
	```  
	$ vagrant up   
	$ vagrant ssh 
	```  
   Now you are logged into the virtual machine.  
3. run:  
	``` 
	$ cd /vagrant/adoption_center 
	```  
4. To create the empty database:  
    ``` 
    $ python database_setup.py
    ```  
5. To fill the database with test-data:
	```
	$ python puppypopulator.py
	```
6. To run the tests:  
	```
	$ python test_database.py
	```
   
   


