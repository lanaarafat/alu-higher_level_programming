-- create database and user
CREATE IF NOT EXISTS DATABASE 'hbtn_0d_2';
CREATE IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE on * . * TO 'user_0d_2'@'localhost';
GRANT SELECT on 'hbtn_0d_2' TO 'user_0d_2'@'localhost';
