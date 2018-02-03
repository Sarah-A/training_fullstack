apt-get -qqy update

# Install PostgreSQL:
apt-get -qqy install postgresql

# Install Python packages:
apt-get -qqy install python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
pip install redis
pip install passlib
pip install itsdangerous
pip install flask-httpauth
pip install python-dateutil

# Set up PostgreSQL:
sudo -u postgres createuser --createdb vagrant
sudo -u postgres createdb vagrant


vagrantTip="The shared directory is located at /vagrant\nTo access your shared files: cd /vagrant"
echo -e $vagrantTip > /etc/motd

