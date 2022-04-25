# rapexa.ir
rapexa.ir website

/97E0848778679DE516AEFF12986FF261CCEF0D692397B45017DDD62D492FCC64
'admin panel : RAPEXA_MGSTUDIO88409304910631'

/logout                 'logout'
/sign_up                'buy'
/ok                     'api for test system'
/                       'main page'

CREATE DATABASE rapexa;
CREATE USER 'RAPEXA'@'localhost' IDENTIFIED BY 'mgstudio88409304910631';
GRANT ALL PRIVILEGES ON rapexa.* TO 'RAPEXA'@'localhost';
USE rapexa;
DROP TABLE IF EXISTS messages;
CREATE TABLE messages (name VARCHAR(100), email VARCHAR(100), phone VARCHAR(100),title VARCHAR(100),message VARCHAR(250));
DROP TABLE IF EXISTS users;
CREATE TABLE users (name VARCHAR(100), email VARCHAR(100), phone VARCHAR(100),password VARCHAR(250));

TODO: deploy projecy again and think about call and payments
TODO: spotplayer for courses

chmod +x yourPythonScriptName.py
nohup /path/to/yourPythonScriptName.py &