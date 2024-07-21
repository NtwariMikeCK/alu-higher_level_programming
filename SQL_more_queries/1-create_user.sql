-- script for creating a new user and granting them all the priveledges
DROP USER IF EXISTS user_0d_1;
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- granting priveledges
GRANT ALL PRIVILEGES *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
