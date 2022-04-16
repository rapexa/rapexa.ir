# rapexa.ir
rapexa.ir website

/97E0848778679DE516AEFF12986FF261CCEF0D692397B45017DDD62D492FCC64                       
'admin panel : RAPEXA_MGSTUDIO88409304910631'

/logout                 'logout'
/sign_up                'add user'
/sign_in                'login'
/ok                     'api for test system'


/packages/GIT/          'git package page'
/packages/python1/      'python 1 package page'
/packages/python2/      'python 2 package page'

CREATE DATABASE rapexa;
CREATE USER 'RAPEXA'@'localhost' IDENTIFIED BY 'mgstudio88409304910631';
GRANT ALL PRIVILEGES ON rapexa.* TO 'RAPEXA'@'localhost';
USE rapexa;
DROP TABLE IF EXISTS messages;
CREATE TABLE messages (name VARCHAR(100), email VARCHAR(100), phone VARCHAR(100),title VARCHAR(100),message VARCHAR(250));
DROP TABLE IF EXISTS users;
CREATE TABLE users (name VARCHAR(100), email VARCHAR(100), phone VARCHAR(100),password VARCHAR(250));

TODO: think about admin page and normal and admin use login
TODO: think about domain
TODO: think about how to run project on host
TODO: think about selling courses
TODO: think about play videos online

$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo apt-get install apache2
$ sudo apt-get install libapache2-mod-wsgi-py3
$ sudo pip3 install flask, numpy, pandas, virtualenv