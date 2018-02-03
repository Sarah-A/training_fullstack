
Tournament:
==================

In tournament project I've:
* Created a database that uses PostgreSQL to manage players and matches in
a tournament.
* Implemented all the python functions for accessing the data in the database
and returning players' pairing (Swiss pairing) for the next competition.
* Udacity provided the description of the required functions and a test file (tournament_test.py) to validate the code.


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
	$ cd /vagrant/tournament
	```
4. To create the database:
    ```
    $ psql -c '\i tournament.sql'
    ```
4. To run the tests:
	```
	$ python tournament_test.py
	```
   This is also a good example on how to use the tournament.py module.



