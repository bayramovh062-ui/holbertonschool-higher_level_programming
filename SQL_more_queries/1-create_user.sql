-- we creates a new user in this code and if the user exists code should'nt fail then we give all permissions to user

CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENDIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
