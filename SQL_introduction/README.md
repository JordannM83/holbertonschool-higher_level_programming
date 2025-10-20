# SQL - Introduction

This project is part of the Holberton School curriculum focusing on SQL (Structured Query Language) basics and MySQL database management.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What's a database
- What's a relational database  
- What does SQL stand for
- What's MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 22.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

### Comments for SQL files
Comments should follow this format:
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## MySQL Installation and Setup

### For Ubuntu 22.04 (Current image on CoD Platform)

1. **Ask for a container Ubuntu 22.04**

2. **Update package list**
   ```bash
   apt update
   ```

3. **Install mysql-server package**
   ```bash
   apt install -y mysql-server
   ```

4. **Check installation**
   ```bash
   mysql --version
   ```

5. **Start MySQL Server service**
   ```bash
   service mysql start
   ```

6. **Connect to MySQL**
   ```bash
   mysql -uroot
   ```

### For Ubuntu 20.04 (Legacy)
In the container, credentials are `root/root`

## Project Structure

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Lists all databases of your MySQL server |
| `1-create_database_if_missing.sql` | Creates the database hbtn_0c_0 if it doesn't exist |
| `2-remove_database.sql` | Deletes the database hbtn_0c_0 |
| `3-list_tables.sql` | Lists all the tables of a database |
| `4-first_table.sql` | Creates a table called first_table |
| `5-full_table.sql` | Prints the full description of the table first_table |
| `6-list_values.sql` | Lists all rows of the table first_table |
| `7-insert_value.sql` | Inserts a new row in the table first_table |
| `8-count_89.sql` | Displays the number of records with id = 89 |
| `9-full_creation.sql` | Creates a table second_table and adds multiple rows |
| `10-top_score.sql` | Lists all records of second_table ordered by score |
| `11-best_score.sql` | Lists all records with a score >= 10 |
| `12-no_cheating.sql` | Updates the score of Bob to 10 |
| `13-change_class.sql` | Removes all records with a score <= 5 |
| `14-average.sql` | Computes the score average of all records |
| `15-groups.sql` | Lists the number of records with the same score |
| `16-no_link.sql` | Lists all records where name is not null |

## Database Concepts

### What is a Database?
A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS).

### What is a Relational Database?
A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, where data is stored in tables with rows and columns.

### What does SQL stand for?
SQL stands for **Structured Query Language**. It's a programming language designed for managing data held in a relational database management system.

### What is MySQL?
MySQL is an open-source relational database management system (RDBMS) that uses SQL. It's one of the most popular database systems used for web applications.

### DDL vs DML

**DDL (Data Definition Language):**
- Used to define database structure
- Commands: CREATE, ALTER, DROP, TRUNCATE
- Examples: Creating tables, modifying table structure

**DML (Data Manipulation Language):**
- Used to manipulate data within database objects
- Commands: SELECT, INSERT, UPDATE, DELETE
- Examples: Adding records, updating data, querying data

## Usage Examples

### Running SQL files
```bash
# Execute a SQL file
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

# With specific database
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
```

### Basic SQL Operations

**Create Database:**
```sql
CREATE DATABASE IF NOT EXISTS database_name;
```

**Create Table:**
```sql
CREATE TABLE table_name (
    id INT,
    name VARCHAR(256)
);
```

**Insert Data:**
```sql
INSERT INTO table_name (id, name) VALUES (1, 'Example');
```

**Select Data:**
```sql
SELECT * FROM table_name;
SELECT column1, column2 FROM table_name WHERE condition;
```

**Update Data:**
```sql
UPDATE table_name SET column1 = value WHERE condition;
```

**Delete Data:**
```sql
DELETE FROM table_name WHERE condition;
```

## Tasks Overview

### 0. List databases
Write a script that lists all databases of your MySQL server.

### 1. Create a database
Write a script that creates the database `hbtn_0c_0` in your MySQL server.

### 2. Delete a database
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

### 3. List tables
Write a script that lists all the tables of a database in your MySQL server.

### 4. First table
Write a script that creates a table called `first_table` in the current database.

### 5. Full description
Write a script that prints the full description of the table `first_table`.

### 6. List all in table
Write a script that lists all rows of the table `first_table`.

### 7. First add
Write a script that inserts a new row in the table `first_table`.

### 8. Count 89
Write a script that displays the number of records with `id = 89`.

### 9. Full creation
Write a script that creates a table `second_table` and adds multiple rows.

### 10. List by best
Write a script that lists all records of the table `second_table` ordered by score.

### 11. Select the best
Write a script that lists all records with a score >= 10.

### 12. Cheating is bad
Write a script that updates the score of Bob to 10.

### 13. Score too low
Write a script that removes all records with a score <= 5.

### 14. Average
Write a script that computes the score average of all records.

### 15. Number by score
Write a script that lists the number of records with the same score.

### 16. Say my name
Write a script that lists all records where the name column is not null.

## Repository Information

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `SQL_introduction`
- **Language:** SQL
- **Database:** MySQL 8.0

## Author

This project is part of the Holberton School curriculum.
