-- DBMS DataBase


-- open Sql Server
> run Xampp 

> open Xampp shell

> mysql -h localhost -u root -p  برای ورود به دیتابیس 

-- shoe all databases names 
-- برای نمایش نام دیتابیس ها
> SHOW databases;


--  create new database
-- ساختن دیتابیس جدید
> CREATE DATABASE users;


-- remove a databases
-- حذف دیتابیس
> DROP DATABASE users;


-- select and change the active database
-- برای تغییر دیتابیس فعال یا اتنخاب دیتابیس مورد نظر
> USE users;


-- show tables;
-- نمایش جدول های دیتابیس
> SHOW TABLES;


-- description database
-- توضیحاتی در مورد یکی از ستونهای دیتابیس فعال
> DESCRIBE users;



-- completely delete a table
-- پاک کردن جدول ها
> DROP Table users;


-- clear a table (delete all records in users)
-- پاک کردن مقادیر درون جدول 
> TRUNCATE TABLE users;




-- جدول از قبل ساخته شده



-- Add a Column
-- اضافه کردن ستون
ALTER TABLE table_name ADD column_name datatype;


-- delete a Column
--حذف کردن ستون
ALTER TABLE table_name DROP COLUMN column_name;


-- MODIFY COLUMN (My Sql / Oracle (prior version 10G)
-- ویرایش ستون ها 
ALTER TABLE table_name MODIFY COLUMN column_name datatype;
-- #------------------------------------------------------------------------------------------------


-- add new Records (with custom order)
-- زمانی که میخوایم یک ردیف جدید ایجاد کنیم با ستون ها و مقادیر مشخص
INSERT INTO table_name(column1, column2, column3, ...);
VALUES (value1, value2, value3, ...);


-- add new Records (set all columns, order is important)
-- زمانی که میخوایم یک ردیف جدید ایجاد کنیم با ستون های از قبل تعیین شده و مقادیر جدید
INSERT INTO table_name
VALUES (value1, value2, value3, ...);

-- #------------------------------------------------------------------------------------------------


-- Delete Command Syntax
-- برای حذف یک یا چند ستون 
DELETE FROM table_name WHERE Condition;

-- Examples
DELETE FROM users WHERE age > 40; 
DELETE FROM users WHERE age BETWEEN 18 AND 30;
DELETE FROM users WHERE fullname LIKE "%trump%";
DELETE FROM products WHERE price = 0 and category = 'mobile';
DELETE FROM locations WHERE lat IS NULL or long IS NULL; 


-- #------------------------------------------------------------------------------------------------


-- update Syntax
--اپدیت کردن
UPDATE table_name SET column1=value1, column2=value2
WHERE Condition;


-- Exampeles
UPDATE users SET email = "z.akdjvk@gmail.com"
WHERE id = 4;

UPDATE products SET price = 1.2 * price -- ( No condition, for all )

UPDATE users SET isActive = 0, password = "*7D*^vmdklfjbnsl"
WHERE registered_data < '2022-12-7'


-- #------------------------------------------------------------------------------------------------


--------------------IMPORTANT-----------------------

-- SELECT Syntax
-- برای گزاش گیری
SELECT columns FROM table_name where condition;


-- Exampel
SELECT fullname FROM users where age > 40;
SELECT * FROM users WHERE fullname LIKE 'ali%' and age < 10;
SELECT id,age FROM users;
SELECT * FROM users where email LIKE '%@yahoo%';
SELECT * FROM products where category = 'mobile' and price < 5000:
SELECT ip,access_data FROM access_log where use_id = 7458;

-- use distinc to select unique values (remove duplicate values)
SELECT distinct city FROM addresses



-- where Operators

    =               EQUAL
    >               Greater than
    <               Last than
    >=              Greater than or equal
    <=              Less than or equal
    <>, !=          NOT equal
    BETWEEN         Between a certain range
    LIKE            Search for a pattern
    IN              To sepecify multiple possible values for a column
    IS [NOT]NULL    Check if value is null or not



-- SELECT Syntax (OrderTypes: ASC|DESC)
-- برای مرتب سازی اطلاعات ذخیره شده
SELECT columns FROM table_name where condition
ORDER BY column1 order_type, column2 order_type, ...



-- order user bay age (young first)
SELECT * FROM users ORDER BY age ASC;

-- order posts bay date (lastest first)
SELECT * FROM posts ORDER BY publish_date DESC;

-- order PRODUCTS (cheapest)
SELECT * FROM products ORDER BY price ASC;

-- order products (most expensive)
SELECT * FROM products ORDER BY price DESC, created_at DESC;





-- Aggregate Functions

-- Aggregate Functions syntax
SELECT agger(column) FROM table where ..


AVG(column)         Calculates the average of a set of values.
MIN(column)         Gets the minimum value in a set of valuses.
MAX(column)         Gets the maximum value in a set of valuses.
SUM(column)         Calculates the sum of values.
COUNT(column)       Counts rows a sepified table or view.






-- #------------------------------------------------------------------------------------------------

-- limit syntax

> SELECT * FROM table_name LIMIT start, length;



-- Exampel
> SELECT * FROM Cuostomers LIMIT 5, 10;


-- pagination
> SELECT * FROM Cuostomers LIMIT start_point, PAGE_SIZE;
>> start_point = (page-1) * PAGE_SIZE



-- #------------------------------------------------------------------------------------------------

-- join

--ANSI SQL-89
--  SELECT * FROM Products, Suppliers
--  where Products.SuppliersID = Suppliers.SuppliersID


--ANSI SQL-92
SELECT * FROM Products JOIN Suppliers
ON Products.SuppliersID = Suppliers.SuppliersID




-- #------------------------------------------------------------------------------------------------



-- CREATE TABLE Syntax

CREATE TABLE table_name (
    column1 datatype,  -- column1 -> ستون اول   datatype-> نوع ستون اول
    column2 datatype,
    column3 datatype,
    column4 datatype,
    ...
);


-- Exampel: users
CREATE TABLE users (
    id int;
    fullname varchar(64),
    email varchar(120),
);



-- Create Table Constraints
CREATE TABLE table_name (
    column1 datatype constraints,  -- column1 -> ستون اول   datatype-> نوع ستون اول    constraints-> محدودیت قرار دادن
    column2 datatype constraints,
    column3 datatype constraints,
    column4 datatype constraints,
    ...
);


-- Exampel Create Table Constraints
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);


-- Constraints
NOT NULL
UNIQUE
PRIMARY KEY
FOREIGN KEY
CHECK