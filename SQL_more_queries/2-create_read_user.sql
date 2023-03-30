-- create database and user
CREATE IF NOT EXISTS DATABASE 'hbtn_0d_2';
CREATE IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT on * . * TO 'user_0d_2'@'localhost';
