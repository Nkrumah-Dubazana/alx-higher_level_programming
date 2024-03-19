-- creates the MySQL server user_0d_01 and grants all priviledges
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1pwd';
GRANT ALL PRIVILEDGES ON * . * TO user_0d_1@localhost;
