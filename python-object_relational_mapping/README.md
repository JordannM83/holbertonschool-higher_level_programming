# Python - Object-relational mapping

## Description
This project focuses on linking two amazing worlds: Databases and Python! In the first part, you will use the module MySQLdb to connect to a MySQL database and execute SQL queries. In the second part, you will use the module SQLAlchemy, an Object Relational Mapper (ORM), to abstract the storage layer.

## Background Context
The biggest difference between using MySQLdb and SQLAlchemy is: no more SQL queries with ORM! The purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be "What can I do with my objects" and not "How this object is stored? where? when?".

## Resources
* Object-relational mappers
* mysqlclient/MySQLdb documentation
* MySQLdb tutorial
* SQLAlchemy tutorial
* SQLAlchemy
* mysqlclient/MySQLdb
* Introduction to SQLAlchemy
* Flask SQLAlchemy
* 10 common stumbling blocks for SQLAlchemy newbies
* Python SQLAlchemy Cheatsheet
* SQLAlchemy ORM Tutorial for Python Developers

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone:
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Requirements
### General
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Files will be executed with MySQLdb version 2.0.x
* Files will be executed with SQLAlchemy version 1.4.x
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A README.md file, at the root of the folder of the project, is mandatory
* Code should use the pycodestyle (version 2.7.*)
* All files must be executable
* The length of files will be tested using wc
* All modules should have documentation
* All classes should have documentation
* All functions should have documentation
* You are not allowed to use execute with sqlalchemy

## Installation
### Install MySQL 8.0
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
```

### Install MySQLdb module version 2.0.x
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==2.0.3
```

### Install SQLAlchemy module version 1.4.x
```bash
$ sudo pip3 install SQLAlchemy==1.4.22
```

## Tasks

### 0. Get all states
Write a script that lists all states from the database hbtn_0e_0_usa
* **File:** `0-select_states.py`

### 1. Filter states
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
* **File:** `1-filter_states.py`

### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
* **File:** `2-my_filter_states.py`

### 3. SQL Injection...
Write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from MySQL injections)
* **File:** `3-my_safe_filter_states.py`

### 4. Cities by states
Write a script that lists all cities from the database hbtn_0e_4_usa
* **File:** `4-cities_by_state.py`

### 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state
* **File:** `5-filter_cities.py`

### 6. First state model
Write a python file that contains the class definition of a State and an instance Base = declarative_base()
* **File:** `model_state.py`

### 7. All states via SQLAlchemy
Write a script that lists all State objects from the database hbtn_0e_6_usa
* **File:** `7-model_state_fetch_all.py`

### 8. First state
Write a script that prints the first State object from the database hbtn_0e_6_usa
* **File:** `8-model_state_fetch_first.py`

### 9. Contains `a`
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
* **File:** `9-model_state_filter_a.py`

### 10. Get a state
Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
* **File:** `10-model_state_my_get.py`

### 11. Add a new state
Write a script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
* **File:** `11-model_state_insert.py`

### 12. Update a state
Write a script that changes the name of a State object from the database hbtn_0e_6_usa
* **File:** `12-model_state_update_id_2.py`

### 13. Delete states
Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
* **File:** `13-model_state_delete_a.py`

### 14. Cities in state
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City
* **Files:** `model_city.py`, `14-model_city_fetch_by_state.py`

## Author
* **Jordan** - Holberton School Higher Level Programming Project

## Repository
* **GitHub repository:** holbertonschool-higher_level_programming
* **Directory:** python-object_relational_mapping
