-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- Password should be set to user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost;
SET PASSWORD FOR user_0d_2@localhost = 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* to user_0d_2@localhost;
