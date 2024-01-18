-- a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 
-- on your server (in localhost).
-- SHOW GRANTS FOR 'user_0d_1' @ 'localhost';
-- SHOW GRANTS FOR 'user_0d_2' @ 'localhost';
SET @user_exists = (SELECT EXISTS(SELECT 1 FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost'));

IF @user_exists THEN
    SHOW GRANTS FOR 'user_0d_1'@'localhost';
ELSE
    SELECT 'User does not exist';
END IF;
SET @user_exists = (SELECT EXISTS(SELECT 1 FROM mysql.user WHERE User = 'user_0d_2' AND Host = 'localhost'));

IF @user_exists THEN
    SHOW GRANTS FOR 'user_0d_2'@'localhost';
ELSE
    SELECT 'User does not exist';
END IF;

