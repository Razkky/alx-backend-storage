--- Create a table on a database

CREATE TABLE  IF NOT EXISTS user(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
)