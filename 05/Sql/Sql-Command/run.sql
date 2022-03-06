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



NOT NULL 
UNIQUE
PRIMARY KEY
FOREIGN KEY
CHECK















